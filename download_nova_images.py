import urllib.request, os, re, urllib.parse

os.makedirs('assets/novatech_img', exist_ok=True)

queries = {
    'OrionLX.jpg': 'NovaTech OrionLX Automation Platform',
    'OrionLXm.jpg': 'NovaTech OrionLXm Automation Platform',
    'OrionIO.jpg': 'NovaTech Orion I/O module',
    'Bitronics-M650.jpg': 'Bitronics M650 Panel Meter',
    'Bitronics-M871.jpg': 'Bitronics M871 PMU'
}

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

for filename, query in queries.items():
    print(f"Buscando: {query}")
    try:
        url_search = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query + ' filetype:jpg')}"
        req = urllib.request.Request(url_search, headers={'User-Agent': user_agent})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        imgs = re.findall(r'src="//external-content\.duckduckgo\.com/iu/\?u=([^&"]+)', html)
        if imgs:
            # DuckDuckGo URL Encodes the target URL
            img_url = urllib.parse.unquote(imgs[0])
            print(f"Descargando de: {img_url}")
            
            img_req = urllib.request.Request(img_url, headers={'User-Agent': user_agent})
            with urllib.request.urlopen(img_req, timeout=10) as response:
                with open(f'assets/novatech_img/{filename}', 'wb') as out_file:
                    out_file.write(response.read())
            print(f"Guardado {filename}")
        else:
            print(f"No imagenes para {query}")
    except Exception as e:
        print(f"Error {filename}: {e}")
