import os
import sys

# Intenta importar PyPDF2, si no instalarlo
try:
    import PyPDF2
except ImportError:
    print("Instalando dependencias necesarias...")
    os.system("pip install PyPDF2 pypdf")
    import PyPDF2

file_path = "/Users/victorvilche/OpenCode/Creador Skils/.agent/skills/creador-de-skills/AgenteNormativoConecta/Agentes CONECTA/Ingenieria-Diseño/fuentes_externas/Informe-Estudio-Modulo-de-Medicion-Fasorial-2025 (1).pdf"

if not os.path.exists(file_path):
    print("El archivo PDF no se encontró en la ruta especificada.")
    sys.exit(1)

out_text = []

with open(file_path, "rb") as f:
    pdf_reader = PyPDF2.PdfReader(f)
    print(f"Número total de páginas: {len(pdf_reader.pages)}")
    
    # Extraer texto de todas las páginas para buscar '20 MW' o subestaciones
    for i, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if text:
            # Filtrar lineas que contengan "MW" o "Subestación"
            lines = text.split('\n')
            for line in lines:
                if '20' in line or 'MW' in line or 'Subestac' in line or 'S/E' in line:
                    out_text.append(f"Pag {i+1}: {line.strip()}")

# Escribir el resultado en un archivo temporal de texto para analizarlo
with open("pdf_extracted_lines.txt", "w", encoding='utf-8') as f_out:
    for line in out_text:
        f_out.write(line + "\n")

print(f"Extracción completada. Se guardaron {len(out_text)} líneas con posibles coincidencias.")
print("Primeras 20 coincidencias:\n")
for line in out_text[:20]:
    print(line)
