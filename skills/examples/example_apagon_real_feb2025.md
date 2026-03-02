# Ejemplo Real: Diagnóstico Post-Apagón 25-Feb-2025 — Empresa Transmisora

**Skill utilizada:** `skill_transmision` + `skill_base_sitr` + `skill_edac_edag_erag`
**Fuente:** CEN — EAF publicado 19-mar-2025; informes SEC; prensa técnica verificada
**Tipo de caso:** Post-mortem de fallas normativas reales de una empresa transmisora

> ⚠️ Este es un ejemplo basado en datos y hechos públicos del apagón del 25 de febrero de 2025 en Chile. Es el mayor apagón de la historia moderna del país.

---

## Contexto del Evento

| Dato | Valor |
|---|---|
| Fecha | 25-Feb-2025, ~14:32 UTC |
| Empresa analizada | Transelec S.A. (transmisora STN, mayor de Chile) |
| Rol en el evento | Agravante: sus fallas de SCADA y comunicación dificultaron la recuperación |
| Causa raíz del apagón | ISA Interchile — reinicio no autorizado de protección 87L en línea 500 kV |

---

## Diagnóstico de Cumplimiento SITR al Momento del Evento

| Parámetro | Requisito | Estado durante evento | Estado |
|---|---|---|---|
| Disponibilidad SITR | >= 99.5% | **0%** — sin señales válidas durante la crisis | ❌ |
| SCADA principal | Operativo | **Perdido totalmente** durante el evento | ❌ |
| SCADA respaldo | Disponible en <= X min | **+80 minutos** sin activar | ❌ |
| Hot Line voz operativa | >= 99.5% | **Perdida** — sin comunicación con el CEN | ❌ |
| Telecontrol remoto | Operativo | **Perdido** — sin capacidad de maniobra | ❌ |
| Señales SITR al CEN | Actualizadas | **CEN sin datos de Transelec** durante crisis | ❌ |

---

## Hallazgos de Auditoría (Real)

La auditoría externa posterior encontró **38 hallazgos de alta criticidad** en sistemas SCADA y telecomunicaciones de Transelec, incluyendo:

| Categoría | Descripción |
|---|---|
| Mantenimiento preventivo | Deficiencias en mantenimiento de equipos SCADA |
| Mantenimiento correctivo | Deficiencias en corrección oportuna de fallas detectadas |
| Redundancia | Sistema de respaldo no disponible en el tiempo crítico |
| Telecomunicaciones | Sistemas de voz (Hot Line) con puntos de falla únicos |

---

## Tabla de Brechas Normativas Identificadas

| ID | Brecha | Normativa incumplida | Criticidad |
|---|---|---|---|
| T01 | SCADA sin redundancia efectiva (respaldo tardó > 80 min) | NTSyCS — redundancia requerida | 🔴 Crítico |
| T02 | Hot Line de voz operativa perdida | NTSyCS — disponibilidad voz >= 99.5% | 🔴 Crítico |
| T03 | SITR sin datos válidos durante evento (SITR 0%) | SITR dic-2019 — edad datos <= 5 s | 🔴 Crítico |
| T04 | Telecontrol remoto perdido | NTSyCS — control operativo remoto | 🔴 Crítico |
| T05 | Mantenimiento preventivo insuficiente (38 hallazgos) | NTSyCS — mantenimiento obligatorio | 🟠 Alta |
| T06 | Sin plan de contingencia efectivo para pérdida de SCADA | Procedimientos CEN | 🟠 Alta |

---

## Plan de Remediación (Lo que CONECTA Recomendaría)

| Prioridad | Acción | Plazo | Skill |
|---|---|---|---|
| 🔴 Inmediato | Activar y probar SCADA respaldo mensualmente | 30 días | skill_transmision |
| 🔴 Inmediato | Auditar y reparar Hot Line en todos los sit. de CC | 30 días | skill_base_sitr |
| 🔴 Inmediato | Verificar tiempo de conmutación SCADA respaldo (< 5 min) | 30 días | skill_base_sitr |
| 🟠 30 días | Implementar plan de mantenimiento preventivo SCADA | 30 días | skill_vigilancia_normativa |
| 🟠 60 días | Auditar todos los puntos de falla única en telecom | 60 días | skill_transmision |
| 🟡 90 días | Actualizar procedimientos de emergencia ante pérdida de SCADA | 90 días | skill_informe_tecnico |

---

## Consecuencias Regulatorias

| Acción SEC/CEN | Descripción |
|---|---|
| Cargos SEC | Formulados contra Transelec por fallas criticas de operación y supervisión |
| Auditoría CEN | CEN instruyó auditoría técnica SCADA y telecomunicaciones |
| EPRI + Universidades | Análisis independiente de causas y mejoras del sistema |
| Pérdida económica | ~USD 1.000 millones en el país por el apagón total |

---

## Lección Clave Para CONECTA

> **Este caso demuestra que el riesgo regulatorio del incumplimiento SITR no es abstracto.** Una transmisora con infraestructura de clase mundial puede perder toda su visibilidad en minutos si no mantiene correctamente sus sistemas de respaldo. CONECTA puede ofrecer diagnósticos preventivos exactamente para evitar este escenario.

**Propuesta de valor concreta:**
"Diagnóstico preventivo de redundancia SITR y SCADA: 4 semanas, entregamos tabla de brechas con 38 puntos de verificación basados en los hallazgos reales del apagón del 25-feb-2025."
