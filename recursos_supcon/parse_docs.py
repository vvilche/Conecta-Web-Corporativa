import zipfile
import xml.etree.ElementTree as ET
import os
import glob

def extract_text_from_pptx(pptx_path, out_path):
    namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
    text_runs = []
    
    with zipfile.ZipFile(pptx_path) as z:
        slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        slide_files.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
        
        for slide_name in slide_files:
            slide_xml = z.read(slide_name)
            root = ET.fromstring(slide_xml)
            slide_text = []
            for node in root.iter(f"{{{namespaces['a']}}}t"):
                if node.text:
                    slide_text.append(node.text)
            if slide_text:
                text_runs.append(f"--- Slide {slide_name} ---")
                text_runs.append('\n'.join(slide_text))
                text_runs.append('')
                
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_runs))
    print(f"Extracted PPTX to {out_path}")

def extract_strings_from_xlsx(xlsx_path, out_path):
    # Simplest way: extract sharedStrings.xml and just dump all text.
    text_chunks = []
    try:
        with zipfile.ZipFile(xlsx_path) as z:
            if 'xl/sharedStrings.xml' in z.namelist():
                strings_xml = z.read('xl/sharedStrings.xml')
                root = ET.fromstring(strings_xml)
                namespaces = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                for node in root.findall('.//ns:t', namespaces):
                    if node.text:
                        text_chunks.append(node.text)
                
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(text_chunks))
        print(f"Extracted XLSX strings to {out_path}")
    except Exception as e:
        print(f"Error extracting XLSX: {e}")

if __name__ == "__main__":
    pptx_files = glob.glob("*.pptx")
    for p in pptx_files:
        extract_text_from_pptx(p, p + ".txt")
        
    xlsx_files = glob.glob("*.xlsx")
    for x in xlsx_files:
        extract_strings_from_xlsx(x, x + ".txt")
