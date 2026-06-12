# CONECTA Ingeniería — Web Corporativa

Sitio web corporativo de CONECTA Ingeniería. Single-page app con catálogos
de producto, whitepapers técnicos y sistema de diseño premium.

**URL**: [conecta.cl](https://conecta.cl) | **Deploy**: Netlify

## Estructura

```
├── index.html              ← Landing page principal
├── styles.css              ← Sistema de diseño completo
├── catalogo_supcon.html    ← Catálogo SUPcon (6 productos)
├── catalogo_novatech.html  ← Catálogo Novatech
├── whitepaper_*.html       ← Whitepapers técnicos (PMGD, ECAP, etc.)
├── skills/                 ← Skills de ingeniería para agentes IA
├── normativa/              ← Documentos regulatorios CNE/CEN
├── assets/                 ← Imágenes (WebP optimizado)
├── archive/                ← Backups de versiones anteriores
├── landing_ejemplos.html   ← Ejemplos de landing pages
└── index_*_storybrand.html ← Variantes A/B testing
```

## Contenido

### Páginas principales
- **Landing**: Hero con propuesta de valor, servicios, productos, casos de éxito
- **SUPcon**: 6 productos (DCS, SIS, SCADA, RTU, Gateway, Instrumentación)
- **Novatech**: Bitronics, OrionLX, Kronos

### Whitepapers
- Estrategia PMUS 2025
- Estudio ECAP Eólico
- PMGD + BESS
- Visita a Terreno
- Apagón Febrero 2025
- Auditoría SITR/STN

### Skills de ingeniería (17 documentos)
Cálculo de cortocircuito, revisión de planos, coordinación de protecciones,
estudios ECAP, memorias de cálculo, vigilancia normativa, y más.

### Normativa
- CNE: AT SITR, NTCO PMGD, NTSyCS, NTCSD, NTSSCC
- CEN: SE Riesgo PMUS, listado MMF

## Deploy

```bash
# Local dev
python3 -m http.server 8080

# Deploy a Netlify
netlify deploy --prod
```

## Diseño

Sistema de diseño propio con variables CSS:
- **Paleta**: Navy profundo + azul B2B + amarillo alerta normas
- **Tipografía**: Inter (body) + Outfit (headings) + IBM Plex Mono (código)
- **Componentes**: Cards, stats, hero, grid de productos, timeline

---

> CONECTA Ingeniería — Digitalización de Subestaciones, Procesos y Remotas
