import sys
import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Navbar update
    content = re.sub(
        r'<a href="#soluciones">Integración.*?</a>\s*<a href="#ingenieria">Servicios.*?</a>',
        '<a href="#sistemas">División Sistemas</a>\n                <a href="#equipos">Venta de Equipos</a>',
        content,
        flags=re.DOTALL
    )

    # 2. Hero button update
    content = content.replace(
        '<a href="#soluciones" class="btn-primary">Ver Tecnologías</a>',
        '<a href="#sistemas" class="btn-primary">Descubrir Sistemas</a>'
    )

    # 3. Main block update
    pattern = r'<!-- SOLUTIONS MATRIX -->\s*<section id="soluciones" class="solutions">.*?(?=    <!-- PR & MEDIA SECTION -->)'
    new_block = """    <!-- 1. DIVISIÓN: SISTEMAS E INTEGRACIÓN -->
    <section id="sistemas" class="solutions" style="background: var(--bg-page);">
        <div class="container">
            <div class="section-header">
                <h2>División de Sistemas</h2>
                <p>Nuestros departamentos de ingeniería aplicada para la resolución de desafíos normativos operativos y la optimización de procesos industriales complejos.</p>
            </div>

            <!-- Sub-sección: Sistemas Eléctricos y Normativos -->
            <h3 style="margin-bottom: 32px; font-size: 1.5rem; color: var(--brand-blue); border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">Integración de Minería y Sector Eléctrico (CEN/CNE)</h3>
            <div class="grid-solutions" style="margin-bottom: 64px;">
                <!-- SCADA Nivel 2 -->
                <div class="sol-card">
                    <div class="sol-icon">💻</div>
                    <h3>Sistemas SCADA Eléctrico</h3>
                    <p>Integración y programación de redes O.T. con sistemas SCADA Nivel 2 (Subestación y Planta), e implementación llave en mano de centros de control corporativos.</p>
                    <a href="#" class="sol-link">Ver Arquitecturas SCADA →</a>
                </div>

                <!-- Retrofit y Servicios Normativos -->
                <div class="sol-card">
                    <div class="sol-icon">🛡️</div>
                    <h3>Retrofit Eléctrico y Normativa</h3>
                    <p>Modernización de relés obsoletos, auditorías técnicas, homologación SITR y consultoría experta para cumplimiento exigido por el Coordinador Eléctrico.</p>
                    <a href="#" class="sol-link">Ver Casos de Retrofit →</a>
                </div>

                <!-- Sincrofasores PMUS -->
                <div class="sol-card">
                    <div class="sol-icon">⚡</div>
                    <h3>Sincrofasores (PMUS)</h3>
                    <p>Diseño corporativo e integración de armarios PMUS (C37.118-2018) para Parques PMGD y subestaciones que requieren control centralizado de inyección.</p>
                    <a href="#" class="sol-link">Soluciones PMUS →</a>
                </div>
            </div>

            <!-- Sub-sección: Sistemas de Procesos (SUPCON) -->
            <h3 style="margin-bottom: 32px; font-size: 1.5rem; color: var(--brand-blue); border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">Integración de Procesos Industriales</h3>
            <div class="grid-solutions">
                <!-- Control Distribuido -->
                <div class="sol-card">
                    <div class="sol-icon">🏭</div>
                    <h3>Control Distribuido (DCS/SIS)</h3>
                    <p>Sistemas Inteligentes integrados con tecnología avanzada para control continuo y discreto de procesos de manufactura, minería y energía (Misión Crítica).</p>
                    <div class="sol-brands"><span class="sol-brand-tag">DCS / SIS</span></div>
                    <a href="#" class="sol-link">Explorar Plataformas →</a>
                </div>
                
                <!-- Soluciones IA -->
                <div class="sol-card">
                    <div class="sol-icon">🧠</div>
                    <h3>Inteligencia Artificial (IA) O.T.</h3>
                    <p>Implementación de gemelos digitales y modelos predictivos impulsados para migrar hacia plantas de proceso totalmente autónomas y eficientes.</p>
                    <div class="sol-brands"><span class="sol-brand-tag">Algoritmos Integrados</span></div>
                    <a href="#" class="sol-link">Innovación IA →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. DIVISIÓN: VENTA DE EQUIPOS -->
    <section id="equipos" class="solutions" style="background: #ffffff; border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light);">
        <div class="container">
            <div class="section-header">
                <h2>División Comercial: Equipamiento Industrial</h2>
                <p>Representantes exclusivos y distribuidores oficiales. Venta y provisión directa de las marcas de clase mundial que soportan nuestra ingeniería.</p>
            </div>

            <div class="grid-solutions">
                <!-- Instrumentación SUPCON -->
                <div class="sol-card" style="border-top: 4px solid #d32f2f;">
                    <div class="sol-icon" style="color:#d32f2f; background: rgba(211,47,47,0.1);">🔭</div>
                    <h3>Instrumentación Inteligente</h3>
                    <p>Venta de caudalímetros, transmisores de presión y sensores de alta exactitud para control estricto de cualquier tipo de proceso físico en terreno.</p>
                    <div class="sol-brands"><span class="sol-brand-tag">SUPCON</span></div>
                    <a href="#" class="sol-link" style="color:#d32f2f;">Catálogo SUPCON →</a>
                </div>

                <!-- NovaTech -->
                <div class="sol-card" style="border-top: 4px solid #0033a0;">
                    <div class="sol-icon" style="color:#0033a0; background: rgba(0,51,160,0.1);">🖥️</div>
                    <h3>Controladores y Gateways</h3>
                    <p>Suministro de la familia OrionLX, RTUs avanzadas y gateways multiprotocolo para automatización y digitalización en subestaciones (IEC 61850).</p>
                    <div class="sol-brands"><span class="sol-brand-tag">NovaTech Automation</span></div>
                    <a href="#" class="sol-link" style="color:#0033a0;">Catálogo NovaTech →</a>
                </div>

                <!-- FRACTAL -->
                <div class="sol-card" style="border-top: 4px solid #10b981;">
                    <div class="sol-icon" style="color:#10b981; background: rgba(16,185,129,0.1);">🔋</div>
                    <h3>Sistemas BESS (EMS/ELPROS)</h3>
                    <p>Representación comercial de hardware y software controlador ELPROS para arbitraje de energía y control de frecuencia coordinado para parque de baterías.</p>
                    <div class="sol-brands"><span class="sol-brand-tag">FRACTAL EMS</span><span class="sol-brand-tag">ELPROS</span></div>
                    <a href="#" class="sol-link" style="color:#10b981;">Catálogos EMS →</a>
                </div>

                <!-- Redes -->
                <div class="sol-card" style="border-top: 4px solid #f26522;">
                    <div class="sol-icon" style="color:#f26522; background: rgba(242,101,34,0.1);">📡</div>
                    <h3>Switches O.T. y Fibra Óptica</h3>
                    <p>Suministro de routers, switches industriales IEC 61850 y cables especializados para otorgar la máxima flexibilidad y robustez en redes críticas.</p>
                    <div class="sol-brands">
                        <span class="sol-brand-tag">Hirschmann</span>
                        <span class="sol-brand-tag">Belden</span>
                    </div>
                    <a href="#" class="sol-link" style="color:#f26522;">Catálogo de Redes →</a>
                </div>

                <!-- NR Electric / Vizimax -->
                <div class="sol-card" style="border-top: 4px solid #004b87;">
                    <div class="sol-icon" style="color:#004b87; background: rgba(0,75,135,0.1);">🛡️</div>
                    <h3>Relés de Protección y Maniobra</h3>
                    <p>Venta de equipos de protección secundaria y gabinetes para MT/AT emparejados con soluciones de maniobra controlada Vizimax, probadas en fábrica.</p>
                    <div class="sol-brands"><span class="sol-brand-tag">NR Electric</span><span class="sol-brand-tag">Vizimax</span></div>
                    <a href="#" class="sol-link" style="color:#004b87;">Catálogo NR & Vizimax →</a>
                </div>
            </div>
        </div>
    </section>
\n"""
    
    content = re.sub(pattern, new_block, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

try:
    update_file('index.html')
    print("Updated local 1")
except Exception as e:
    print(f"Error local 1: {e}")

try:
    update_file('/Users/victorvilche/OpenCode/Conecta-Web-Corporativa/index.html')
    print("Updated local 2")
except Exception as e:
    print(f"Error local 2: {e}")
