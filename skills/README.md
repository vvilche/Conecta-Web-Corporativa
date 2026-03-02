# 📚 Índice de Skills — CONECTA Ingeniería/Diseño

## 🏗️ Skills de Diagnóstico Inicial
| Skill | Cuándo usar |
|---|---|
| [skill_diagnostico_rapido](skill_diagnostico_rapido.md) | **Empezar siempre aquí** — identifica tipo de coordinado y activa skill correcto |

---

## ⚡ Skills Normativas CEN
> Aplicar según tipo de coordinado. Siempre revisar `skill_base_sitr` primero.

| Skill | Coordinado | Normativa clave |
|---|---|---|
| [skill_base_sitr](skill_base_sitr.md) | **Todos** los coordinados | SITR dic-2019, AT-SITR-1, NTSyCS |
| [skill_generacion](skill_generacion.md) | Generación >= 9 MW | PMUS 2025, EDAG/ERAG |
| [skill_transmision](skill_transmision.md) | Transmisión STN/STE/STR | MMF 2025, PDC |
| [skill_distribucion_clientes](skill_distribucion_clientes.md) | Distribución y clientes | AT-SITR-1 |
| [skill_pmgd_pmg](skill_pmgd_pmg.md) | PMGD / PMG | AT-SITR-1, PMUS 2025 |
| [skill_sscc](skill_sscc.md) | Prestadores SSCC | NTSyCS, AT-SITR-1 |
| [skill_edac_edag_erag](skill_edac_edag_erag.md) | Coordinados con esquemas | EDAC/EDAG/ERAG jun-2015 |
| [skill_vigilancia_normativa](skill_vigilancia_normativa.md) | Monitoreo continuo | CEN, SEC, CNE |

---

## 🔧 Skills de Ingeniería
> Usar para diseño, cálculo, revisión y documentación técnica.

| Skill | Uso principal | Salida |
|---|---|---|
| [skill_estudio_ecap](skill_estudio_ecap.md) | Estudios de conexión al SEN | Informe ECAP |
| [skill_calculo_cortocircuito](skill_calculo_cortocircuito.md) | Análisis de fallas eléctricas | Tabla Icc por barra |
| [skill_coordinacion_protecciones](skill_coordinacion_protecciones.md) | Ajuste y coordinación de relés | Curvas y tabla de ajustes |
| [skill_revision_planos](skill_revision_planos.md) | Revisión de planos y unifilares | Lista de comentarios RFI |
| [skill_memoria_calculo](skill_memoria_calculo.md) | Dimensionamiento eléctrico | Memoria de cálculo formal |
| [skill_visita_terreno](skill_visita_terreno.md) | Inspección y levantamiento | Informe de terreno |
| [skill_informe_tecnico](skill_informe_tecnico.md) | Generación de informes formales | Informe CON-ING-YYYY-NNN |

---

## 🔗 Dependencias entre Skills

```
skill_diagnostico_rapido
    ├─► skill_base_sitr ──────────────► skill_generacion
    │                                 ├─► skill_transmision
    │                                 ├─► skill_distribucion_clientes
    │                                 ├─► skill_pmgd_pmg
    │                                 ├─► skill_sscc
    │                                 └─► skill_edac_edag_erag
    │
    └─► skill_estudio_ecap ──────────► skill_calculo_cortocircuito
                                     └─► skill_coordinacion_protecciones

skill_memoria_calculo ──────────────► skill_informe_tecnico
skill_visita_terreno ───────────────► skill_informe_tecnico
```

---

## 📂 Estructura del Repositorio

```
Ingenieria-Diseño/
├── README.md                          ← Este archivo
├── agente_ingenieria_disenio.md       ← Definición del agente
├── skills/                            ← Skills activas
│   ├── skill_*.md                     ← 16 skills
│   └── examples/                      ← Casos de uso reales
│       └── example_*.md
└── documentos/                        ← Fuentes normativas (PDFs/OCR)
```

---

## 📋 Ejemplos de Uso Disponibles
| Ejemplo | Skill relacionada |
|---|---|
| [Caso central solar 50 MW](examples/example_sitr.md) | skill_base_sitr + skill_generacion |
| [Caso PMUS generación](examples/example_generacion.md) | skill_generacion |
| [Caso PMU en STN](examples/example_transmision.md) | skill_transmision |
| [Caso empresa distribuidora](examples/example_distribucion.md) | skill_distribucion_clientes |
| [Caso PMGD >20 MW](examples/example_pmgd.md) | skill_pmgd_pmg |
| [Caso AGC regulación secundaria](examples/example_sscc.md) | skill_sscc |
| [Caso EDAC post-evento](examples/example_edac.md) | skill_edac_edag_erag |
| [Caso conexión PMGD 5 MW](examples/example_ecap.md) | skill_estudio_ecap |
| [Caso subestación industrial Icc](examples/example_cortocircuito.md) | skill_calculo_cortocircuito |
| [Caso revisión plano unifilar](examples/example_revision_planos.md) | skill_revision_planos |
| [Caso tablero industrial 400 A](examples/example_memoria_calculo.md) | skill_memoria_calculo |
| [Caso inspección subestación](examples/example_visita_terreno.md) | skill_visita_terreno |
| [Caso informe ECAP formal](examples/example_informe_tecnico.md) | skill_informe_tecnico |
