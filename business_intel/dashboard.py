#!/usr/bin/env python3
"""CONECTA Business Intelligence Dashboard Generator.

Reads all markdown intel reports from ~/.hermes/intel/ and generates
a self-contained HTML dashboard with the CONECTA design system.
"""

import re, json, os, glob
from datetime import datetime
from pathlib import Path
from html import escape

INTEL_DIR = Path.home() / ".hermes" / "intel"
OUTPUT_FILE = INTEL_DIR / "dashboard.html"

# ── Design tokens (CONECTA brand) ──────────────────────────────────────────
CSS = """
:root {
    --navy: #071324;
    --blue: #1e3a8a;
    --accent: #2563eb;
    --accent-hover: #1d4ed8;
    --bg: #f8fafc;
    --card: #ffffff;
    --text: #1e293b;
    --muted: #64748b;
    --border: #e2e8f0;
    --radius-card: 20px;
    --radius-btn: 100px;
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
    --shadow-lg: 0 20px 25px -5px rgba(0,0,0,0.08);
    --green: #10b981;
    --amber: #eab308;
    --red: #ef4444;
}
* { margin:0; padding:0; box-sizing:border-box; }
body { background:var(--bg); color:var(--text); font-family:'Inter',-apple-system,sans-serif; line-height:1.6; }
header { background:var(--navy); color:white; padding:2rem 3rem; }
header h1 { font-family:'Outfit',sans-serif; font-size:1.8rem; font-weight:800; }
header h1 span { color:var(--accent); }
header .sub { color:#94a3b8; font-size:0.85rem; margin-top:0.25rem; }
.stats { display:flex; gap:2rem; margin-top:1.5rem; flex-wrap:wrap; }
.stat { background:rgba(255,255,255,0.08); border-radius:12px; padding:1rem 1.5rem; min-width:120px; }
.stat .num { font-family:'IBM Plex Mono',monospace; font-size:2rem; font-weight:700; color:var(--accent); }
.stat .label { font-size:0.7rem; color:#94a3b8; text-transform:uppercase; letter-spacing:0.05em; }
.container { max-width:1280px; margin:0 auto; padding:2rem; }
h2 { font-family:'Outfit',sans-serif; font-size:1.4rem; color:var(--navy); margin-bottom:1rem; margin-top:2rem; }
h2:first-of-type { margin-top:0; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(380px,1fr)); gap:1.5rem; }
.card { background:var(--card); border:1px solid var(--border); border-radius:var(--radius-card); padding:1.5rem; box-shadow:var(--shadow); transition:all 0.2s; }
.card:hover { border-color:rgba(37,99,235,0.3); transform:translateY(-2px); box-shadow:var(--shadow-lg); }
.card .source { font-size:0.7rem; color:var(--muted); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.5rem; }
.card h3 { font-family:'Outfit',sans-serif; font-size:1.05rem; color:var(--navy); margin-bottom:0.5rem; line-height:1.3; }
.card p { font-size:0.9rem; color:var(--muted); margin-bottom:0.75rem; }
.card .tags { display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.5rem; }
.tag { font-size:0.65rem; padding:0.25rem 0.75rem; border-radius:var(--radius-btn); font-weight:600; text-transform:uppercase; letter-spacing:0.05em; }
.tag-urgent { background:var(--red); color:white; }
.tag-high { background:#fef3c7; color:#92400e; }
.tag-medium { background:#dbeafe; color:#1e40af; }
.tag-low { background:#f1f5f9; color:var(--muted); }
.tag-segment { background:rgba(37,99,235,0.1); color:var(--blue); }
.tag-competitor { background:#fee2e2; color:#991b1b; }
.tag-opportunity { background:#d1fae5; color:#065f46; }
.tag-signal { background:#fef3c7; color:#92400e; }
.timeline { display:flex; flex-direction:column; gap:0.5rem; }
.timeline-item { display:flex; gap:1rem; align-items:baseline; padding:0.75rem 1rem; background:var(--card); border:1px solid var(--border); border-radius:12px; transition:all 0.2s; }
.timeline-item:hover { border-color:var(--accent); }
.timeline-item .date { font-family:'IBM Plex Mono',monospace; font-size:0.8rem; color:var(--accent); white-space:nowrap; font-weight:600; min-width:85px; }
.timeline-item .summary { font-size:0.9rem; color:var(--text); }
.timeline-item .counts { font-size:0.7rem; color:var(--muted); margin-left:auto; white-space:nowrap; }
.actions { background:var(--card); border:2px solid var(--accent); border-radius:var(--radius-card); padding:1.5rem; margin-top:1.5rem; }
.actions h3 { color:var(--accent); font-family:'Outfit',sans-serif; margin-bottom:0.75rem; }
.actions ol { padding-left:1.2rem; }
.actions li { margin-bottom:0.5rem; font-size:0.9rem; }
.footer { text-align:center; padding:2rem; color:var(--muted); font-size:0.75rem; border-top:1px solid var(--border); margin-top:3rem; }
.footer a { color:var(--accent); }
.empty { text-align:center; padding:3rem; color:var(--muted); }
.report-meta { display:flex; gap:1rem; flex-wrap:wrap; align-items:center; margin-bottom:1.5rem; color:var(--muted); font-size:0.8rem; }
.nav-tabs { display:flex; gap:0.5rem; margin-bottom:1.5rem; flex-wrap:wrap; }
.nav-tab { padding:0.5rem 1.2rem; border-radius:var(--radius-btn); border:1px solid var(--border); background:white; cursor:pointer; font-size:0.8rem; font-weight:500; transition:all 0.2s; }
.nav-tab:hover, .nav-tab.active { background:var(--accent); color:white; border-color:var(--accent); }
.card-link { display:inline-block; font-size:0.75rem; color:var(--accent); margin-bottom:0.5rem; font-weight:600; }
.card-link:hover { text-decoration:underline; }
.cta-contact { display:flex; gap:1.5rem; flex-wrap:wrap; margin-top:1rem; }
.cta-contact a { display:inline-flex; align-items:center; gap:0.4rem; padding:0.6rem 1.2rem; background:var(--accent); color:white; border-radius:var(--radius-btn); font-size:0.8rem; font-weight:600; text-decoration:none; }
.cta-contact a:hover { background:var(--accent-hover); }
@media (max-width:768px) {
    header { padding:1.5rem; }
    .container { padding:1rem; }
    .grid { grid-template-columns:1fr; }
    .stats { gap:1rem; }
    .stat { flex:1; min-width:80px; }
}
"""


def parse_intel_report(filepath: Path) -> dict:
    """Parse a CONECTA intel markdown report into structured data."""
    text = filepath.read_text()

    # Extract date from title
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', text)
    report_date = date_match.group(1) if date_match else None

    def extract_table(section_text):
        """Extract rows from a markdown table."""
        rows = []
        in_table = False
        header = []
        for line in section_text.split('\n'):
            line = line.strip()
            if line.startswith('|') and '---' not in line:
                cells = [c.strip() for c in line.strip('|').split('|')]
                if not in_table:
                    header = cells
                    in_table = True
                else:
                    if len(cells) == len(header):
                        rows.append(dict(zip(header, cells)))
        return rows

    # Extract sections
    sections = {}
    section_pattern = re.compile(r'^## (.+?)(?:\s*\((\d+)\))?$', re.MULTILINE)
    matches = list(section_pattern.finditer(text))

    for i, m in enumerate(matches):
        title = m.group(1).strip()
        count = int(m.group(2)) if m.group(2) else None
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        content = text[start:end]
        sections[title] = {
            'count': count,
            'rows': extract_table(content),
            'text': content
        }

    return {
        'date': report_date,
        'sections': sections,
        'file': filepath.name
    }


def generate_dashboard():
    """Generate the full dashboard HTML."""
    reports = []
    for f in sorted(INTEL_DIR.glob("*.md"), reverse=True):
        try:
            report = parse_intel_report(f)
            if report['date']:
                reports.append(report)
        except Exception:
            continue

    if not reports:
        return "<html><body><div class='empty'>No reports yet. Run the intel scan first.</div></body></html>"

    latest = reports[0]

    # ── Build stats ────────────────────────────────────────────────────────
    total_opps = sum(
        s['count'] or len(s['rows'])
        for r in reports
        for name, s in r['sections'].items()
        if 'opportunit' in name.lower() or 'oportunidad' in name.lower()
    )
    total_competitors = sum(
        s['count'] or len(s['rows'])
        for r in reports
        for name, s in r['sections'].items()
        if 'competit' in name.lower()
    )
    # Unique dates
    unique_dates = len(set(r['date'] for r in reports))

    def build_tag(urgency):
        u = urgency.lower() if urgency else ''
        if 'alta' in u or 'high' in u or 'urgente' in u:
            return 'tag-urgent'
        elif 'media' in u or 'med' in u:
            return 'tag-medium'
        return 'tag-low'

    def render_rows(rows, section_name):
        html = '<div class="grid">'
        tag_class = 'tag-opportunity' if 'opportunit' in section_name.lower() else (
            'tag-competitor' if 'competit' in section_name.lower() else 'tag-signal'
        )
        tag_label = 'OPORTUNIDAD' if 'opportunit' in section_name.lower() else (
            'COMPETIDOR' if 'competit' in section_name.lower() else 'SEÑAL'
        )

        for row in rows:
            # Find the description column (varies by section)
            desc = row.get('Description', row.get('Descripción', row.get('Que Hizo',
                   row.get('Signal', row.get('Implicancia', '')))))
            source = row.get('Source', row.get('Fuente', ''))
            segment = row.get('Segment', row.get('Segmento', ''))
            urgency = row.get('Urgency', row.get('Amenaza', row.get('Threat Level', '')))
            link = row.get('Link', row.get('Enlace', ''))
            title_col = row.get('#', row.get('Competidor', row.get('Competitor', '')))

            # Strip markdown bold markers and HTML
            title = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc)
            title = re.sub(r'<[^>]+>', '', title)
            title = title.strip()[:150]
            if not title:
                title = next((v for v in row.values() if len(v) > 20), 'Sin descripcion')

            html += f'''<div class="card">
                <div class="source">{escape(source)}</div>
                <h3>{escape(title[:150])}</h3>'''
            if link and link.startswith('http'):
                html += f'<a href="{escape(link)}" target="_blank" rel="noopener" class="card-link">🔗 Ver fuente original →</a>'
            html += f'''<div class="tags">
                    <span class="tag {tag_class}">{tag_label}</span>'''
            if segment:
                html += f'<span class="tag tag-segment">{escape(segment)}</span>'
            if urgency:
                html += f'<span class="tag {build_tag(urgency)}">{escape(urgency)}</span>'
            html += '</div></div>'
        html += '</div>'
        return html

    # ── Build timeline ─────────────────────────────────────────────────────
    timeline = '<div class="timeline">'
    for r in reports:
        opps = sum(s['count'] or len(s['rows']) for name, s in r['sections'].items() if 'opportunit' in name.lower())
        comps = sum(s['count'] or len(s['rows']) for name, s in r['sections'].items() if 'competit' in name.lower())
        sigs = sum(s['count'] or len(s['rows']) for name, s in r['sections'].items() if 'signal' in name.lower() or 'señal' in name.lower())
        timeline += f'''<div class="timeline-item">
            <span class="date">{r['date']}</span>
            <span class="summary">{r['file']}</span>
            <span class="counts">🔵 {opps} oportunidades &nbsp; 🔴 {comps} competidores &nbsp; 🟡 {sigs} señales</span>
        </div>'''
    timeline += '</div>'

    # ── Render latest report ───────────────────────────────────────────────
    latest_html = ''
    section_order = [k for k in latest['sections'] if 'opportunit' in k.lower()]
    section_order += [k for k in latest['sections'] if 'competit' in k.lower()]
    section_order += [k for k in latest['sections'] if 'signal' in k.lower() or 'señal' in k.lower()]
    section_order += [k for k in latest['sections'] if k not in section_order and 'search' not in k.lower() and 'action' not in k.lower() and 'conecta' not in k.lower()]

    for section_name in section_order:
        s = latest['sections'][section_name]
        count_str = f" ({s['count']})" if s['count'] else f" ({len(s['rows'])})"
        latest_html += f'<h2>{escape(section_name)}{count_str}</h2>'
        if s['rows']:
            latest_html += render_rows(s['rows'], section_name)
        else:
            # Text-only section
            text = s['text'].strip()
            if text and len(text) < 2000:
                latest_html += f'<div class="card"><p>{escape(text)}</p></div>'

    # ── Actions section ────────────────────────────────────────────────────
    actions_html = ''
    if 'Recommended Actions' in latest['sections'] or 'Acciones Recomendadas' in latest['sections']:
        key = next(k for k in latest['sections'] if 'Action' in k or 'Accion' in k)
        actions = latest['sections'][key]
        if actions['rows']:
            actions_html = '<div class="actions"><h3>🎯 Acciones Recomendadas</h3><ol>'
            for row in actions['rows']:
                desc = row.get('Description', row.get('Descripción', row.get('Acción', next(iter(row.values())))))
                actions_html += f'<li>{escape(desc[:200])}</li>'
            actions_html += '</ol></div>'

    # ── Assemble full page ─────────────────────────────────────────────────
    generated_at = datetime.now().strftime('%Y-%m-%d %H:%M')
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>CONECTA Business Intelligence</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header>
    <h1>CONECTA <span>Business Intelligence</span></h1>
    <div class="sub">Radar competitivo y de oportunidades — Chile industrial</div>
    <div class="stats">
        <div class="stat">
            <div class="num">{total_opps}</div>
            <div class="label">Oportunidades detectadas</div>
        </div>
        <div class="stat">
            <div class="num">{total_competitors}</div>
            <div class="label">Movimientos competidores</div>
        </div>
        <div class="stat">
            <div class="num">{unique_dates}</div>
            <div class="label">Semanas escaneadas</div>
        </div>
        <div class="stat">
            <div class="num">{latest['date']}</div>
            <div class="label">Ultimo reporte</div>
        </div>
    </div>
</header>

<div class="container">
    <div class="report-meta">
        <strong>Reporte actual:</strong> {latest['date']} &nbsp;|&nbsp;
        <strong>Historial:</strong> {len(reports)} reportes &nbsp;|&nbsp;
        <strong>Generado:</strong> {generated_at}
    </div>

    <div class="nav-tabs">
        <button class="nav-tab active" onclick="showSection('latest')">📊 Ultimo Reporte</button>
        <button class="nav-tab" onclick="showSection('timeline')">📅 Historial</button>
    </div>

    <div id="section-latest">
        {latest_html}
        {actions_html}
    </div>

    <div id="section-timeline" style="display:none">
        <h2>Historial de Reportes</h2>
        {timeline}
    </div>
</div>

<footer class="footer">
    <div style="margin-bottom:1rem;font-size:1rem;">¿Ves una oportunidad? Actúa:</div>
    <div class="cta-contact">
        <a href="mailto:victor@conecta.cl">📧 victor@conecta.cl</a>
        <a href="https://wa.me/569" target="_blank">💬 WhatsApp</a>
        <a href="https://conecta.cl" target="_blank">🌐 conecta.cl</a>
    </div>
    <div style="margin-top:1.5rem;">
        CONECTA Ingeniería S.A. — Business Intelligence automatizado con <a href="https://hermes-agent.nousresearch.com">Hermes Agent</a> &nbsp;|&nbsp; Próximo escaneo: cada lunes 08:00 CLT
    </div>
</footer>

<script>
function showSection(name) {{
    document.getElementById('section-latest').style.display = name==='latest'?'block':'none';
    document.getElementById('section-timeline').style.display = name==='timeline'?'block':'none';
    document.querySelectorAll('.nav-tab').forEach((t,i) => {{
        t.classList.toggle('active', (name==='latest'&&i===0)||(name==='timeline'&&i===1));
    }});
}}
</script>
</body>
</html>'''

    return html


if __name__ == '__main__':
    dashboard = generate_dashboard()
    OUTPUT_FILE.write_text(dashboard)
    print(f"Dashboard written to {OUTPUT_FILE} ({len(dashboard)} bytes)")
