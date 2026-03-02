import re

files_to_update = [
    '/Users/victorvilche/OpenCode/Conecta-Web-Corporativa/catalogo_supcon.html',
    '/Users/victorvilche/OpenCode/Creador Skils/.agent/skills/creador-de-skills/AgenteNormativoConecta/Agentes CONECTA/Ingenieria-Diseño/catalogo_supcon.html'
]

new_catalog = """    <!-- CATALOG SECTION -->
    <section id="catalogo" class="catalog-section">
        <div class="container">

            <div class="section-header">
                <h2>Catálogo de Tecnologías SUPCON</h2>
                <p>Respaldo tecnológico para la industria petroquímica, minería, generación eléctrica y manufactura avanzada.</p>
            </div>

            <!-- CATEGORY 1: SISTEMAS DE CONTROL -->
            <h3 class="product-category-title"><span>01.</span> Sistemas de Control Integrado (DCS/UCS)</h3>
            <div class="product-grid">

                <!-- ECS-700X -->
                <div class="product-card">
                    <div class="product-icon">💻</div>
                    <h3>WebField OMC / ECS-700X (DCS)</h3>
                    <p>El sistema de control distribuido insignia. Arquitectura de hardware altamente confiable, redundante y escalable, diseñada para instrumentación a gran escala.</p>
                    <ul class="feature-list">
                        <li>Controladores redundantes sin impactos (Bumpless)</li>
                        <li>Integración nativa IEC 61850 / Foundation Fieldbus</li>
                        <li>Ciberseguridad industrial certificada ISASecure</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Solicitar Arquitectura DCS</a>
                </div>

                <!-- Nyx UCS -->
                <div class="product-card">
                    <div class="product-icon">☁️</div>
                    <h3>Nyx Universal Control System (UCS)</h3>
                    <p>La revolución del control. Un sistema de control definido por software que elimina los armarios tradicionales, utilizando tecnología nativa en la nube (Cloud-based).</p>
                    <ul class="feature-list">
                        <li>Arquitectura óptica de red plana (Fibers to the Edge)</li>
                        <li>Colaboración ágil en ingeniería remota descentralizada</li>
                        <li>Integración con redes APL e I/O virtuales</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Explorar UCS Nyx</a>
                </div>

                <!-- TCS-900 SIS -->
                <div class="product-card">
                    <div class="product-icon">🛡️</div>
                    <h3>TCS-900 (SIS) & Controladores Híbridos</h3>
                    <p>Sistemas Instrumentados de Seguridad (SIL3) y Controladores PLC de la serie InPlant, listos para integrarse mediante switches y RTUs a todo nivel.</p>
                    <ul class="feature-list">
                        <li>Certificación SIL3 integral Quadruple (QMR)</li>
                        <li>Soporta protocolos redundantes DNP3/Modbus</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Especificaciones Control</a>
                </div>
            </div>

            <!-- CATEGORY 2: INSTRUMENTACIÓN -->
            <h3 class="product-category-title"><span>02.</span> Instrumentación Industrial Inteligente</h3>
            <div class="product-grid">

                <!-- Transmisores CXT -->
                <div class="product-card">
                    <div class="product-icon">⏱️</div>
                    <h3>Transmisores de Presión Serie CXT/CJT</h3>
                    <p>Sensores capacitivos y piezorresistivos de alta exactitud (0.05% F.S.) para presión diferencial, absoluta y manométrica.</p>
                    <ul class="feature-list">
                        <li>Salida (4~20)mA + HART 7.0 / Soporte APL</li>
                        <li>Certificación ATEX / Exd IIC T6 Gb antiexplosión</li>
                        <li>Silicio monocristalino con aleaciones 316/316L</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Cotizar Transmisores</a>
                </div>

                <!-- Radar SL900 -->
                <div class="product-card">
                    <div class="product-icon">📡</div>
                    <h3>Nivel por Radar Serie SL900</h3>
                    <p>Medición de nivel continua sin contacto, incluyendo la versión SL903 de 80GHz de altísima frecuencia y precisión (±1mm).</p>
                    <ul class="feature-list">
                        <li>Opciones: 80GHz, 26GHz y Onda Guiada</li>
                        <li>Lentes recubiertas en PTFE para fluidos densos</li>
                        <li>Rango de hasta 120 metros sin parásitos</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Cotizar Radares</a>
                </div>

                <!-- Caudalímetros SFE900 -->
                <div class="product-card">
                    <div class="product-icon">💧</div>
                    <h3>Medidores de Flujo SFE900 / SFM800</h3>
                    <p>Caudalímetros electromagnéticos (SFE) y de masa pura tipo Coriolis (SFM) para pulpas mineras, gases y fluidos corrosivos.</p>
                    <ul class="feature-list">
                        <li>Revestimientos en PTFE/Teflón y Electrodos 316L</li>
                        <li>Excelente linealidad desde (1~10) m3/h</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Cotizar Caudalímetros</a>
                </div>

                <!-- Válvulas y CVP2000 -->
                <div class="product-card">
                    <div class="product-icon">🎛️</div>
                    <h3>Válvulas de Control & CVP2000</h3>
                    <p>Extensa línea de válvulas globo de control LN8100 y bolas SN5100, impulsadas por el innovador posicionador electro-neumático CVP2000.</p>
                    <ul class="feature-list">
                        <li>Posicionador CVP2000 con Auto-Tuning optimizado</li>
                        <li>Calibrador universal de pantalla táctil X600 (HART)</li>
                    </ul>
                    <a href="#cotizar" class="btn-outline">Cotizar Actuación</a>
                </div>
            </div>

            <!-- CATEGORY 3: IA & SOFTWARE -->
            <h3 class="product-category-title"><span>03.</span> Industria 4.0: Plataforma supOS & PRIDE</h3>
            <div class="product-grid">

                <!-- supOS -->
                <div class="product-card">
                    <div class="product-icon">🧠</div>
                    <h3>supOS: Industrial Operating System</h3>
                    <p>Plataforma IIoT nativa concebida como el "sistema operativo" de la fábrica digital. Aglomera variables DCS/PLC para análisis profundo y optimización InPlant (APC).</p>
                    <a href="#cotizar" class="btn-outline">Demo Técnica supOS</a>
                </div>

                <!-- PRIDE -->
                <div class="product-card">
                    <div class="product-icon">📈</div>
                    <h3>PRIDE Dynamic Equipment Server</h3>
                    <p>Hardware y software enfocado al diagnóstico y predicción de fallas en activos rotativos pesados (motores/bombas) mediante sensores triaxiales WS300 (Vibración/Temperatura).</p>
                    <a href="#cotizar" class="btn-outline">Consulta PRIDE Analytics</a>
                </div>
            </div>

        </div>
    </section>"""

for fpath in files_to_update:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex to replace everything from <!-- CATALOG SECTION --> till </section> (first occurrence after that comment)
        pattern = re.compile(r'<!-- CATALOG SECTION -->.*?</section>', re.DOTALL)
        new_content = pattern.sub(new_catalog, content)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fpath}")
    except Exception as e:
        print(f"Failed {fpath}: {e}")

