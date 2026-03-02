import zipfile
import xml.etree.ElementTree as ET
import os
import glob

def extract_text_from_pptx(pptx_path):
    text_runs = []
    try:
        with zipfile.ZipFile(pptx_path) as z:
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort(key=lambda x: int(x.replace('ppt/slides/slide', '').replace('.xml', '')))
            
            for slide_idx, filename in enumerate(slide_files):
                text_runs.append(f"\n--- SLIDE {slide_idx + 1} ---")
                with z.open(filename) as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    # XML namespaces in PPTX
                    ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
                    for node in root.findall('.//a:t', ns):
                        if node.text:
                            text_runs.append(node.text)
    except Exception as e:
        return f"Error reading {pptx_path}: {e}"
    return "\n".join(text_runs)

pptx_files = glob.glob('presentaciones_corporativas/*.pptx')
for f in pptx_files:
    print(f"========== EXTRACTING {f} ==========")
    print(extract_text_from_pptx(f))
    print("="*40)
