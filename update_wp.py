import os
import re

files = [
    "whitepaper_ecap_eolico.html",
    "whitepaper_auditoria_sitr_stn.html",
    "whitepaper_visita_terreno.html"
]

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # 1. Update body tipografía
    content = re.sub(
        r"body\{font-family:'Inter',sans-serif;background:var\(--bg\);color:var\(--ink\);line-height:1\.7;\}",
        "body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--ink);font-size:1.0625rem;line-height:1.75;}",
        content
    )
    
    # 2. Update cover padding & width
    content = re.sub(
        r"\.cover\{background:(.*?);color:#fff;padding:(.*?);\}",
        r".cover{background:\1;color:#fff;padding:80px 0;width:100%;position:relative;overflow:hidden;}",
        content
    )
    
    # 3. Update doc-body
    content = re.sub(
        r"\.doc-body\{max-width:\d+px;margin:0 auto;padding:.*?;\}",
        ".doc-body{max-width:900px;margin:0 auto;padding:60px 60px 80px;}",
        content
    )
    
    # 4. Update the cover inner div
    content = re.sub(
        r'<div style="max-width:6\d0px">',
        '<div style="max-width:900px;margin:0 auto;padding:0 60px;position:relative;z-index:1;">',
        content
    )
    
    # 5. Add responsive if not exists
    if "@media (max-width: 900px)" not in content:
        responsive_css = "@media (max-width: 900px){.layout{grid-template-columns:1fr;}.sidebar{position:relative;height:auto;}.cover{padding:48px 0;}.doc-body{padding:40px 32px 60px;} .cover > div {padding: 0 32px !important;} }"
        content = content.replace("    @media print{", responsive_css + "\n    @media print{")
    
    with open(f, "w") as file:
        file.write(content)

print("Actualización completada en archivos minificados.")
