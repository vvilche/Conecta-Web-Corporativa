import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_pptx(pptx_path):
    text_runs = []
    try:
        with zipfile.ZipFile(pptx_path) as z:
            # Get all slide files and sort them to read in order
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
            
            for slide_idx, filename in enumerate(slide_files):
                text_runs.append(f"\n--- SLIDE {slide_idx + 1} ---")
                with z.open(filename) as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    for node in root.iter():
                        if node.tag.endswith('}t') and node.text:
                            text_runs.append(node.text)
    except Exception as e:
        return str(e)
    return "\n".join(text_runs)

print("----- EXTRACTION OF _Conecta Ingenieria SA .pptx -----")
print(extract_text_from_pptx('presentaciones_corporativas/_Conecta Ingenieria SA .pptx'))
