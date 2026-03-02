# Caso Real: Apagón Masivo Chile — 25 de Febrero de 2025

**Fuente:** CEN — Estudio de Análisis de Falla (EAF) publicado 19-mar-2025 + informes SEC
**Referencia:** https://www.coordinador.cl/ + reportes auditores externos (EPRI + universidades)
**Fecha del evento:** 25-Feb-2025, 14:32 UTC aprox.

> ⚠️ Este es un caso real de múltiples fallas de SITR, SCADA y EDAC que derivaron en el peor apagón de la historia moderna de Chile.

---

## Contexto del Evento

| Dato | Valor |
|---|---|
| Fecha | 25 de febrero de 2025 |
| Zona afectada | Arica → Chiloé (todo Chile continental) + Mendoza y San Juan (Argentina) |
| Causa origen | Intervención no autorizada en línea 2×500 kV Nueva Maitencillo–Nueva Pan de Azúcar |
| Empresa responsable | ISA Interchile (transmisora) |
| Pérdida económica estimada | ~USD 1.000 millones |
| Duración promedio de corte | Varias horas (variable por zona) |

---

## Cadena de Fallas

### 1. Origen — ISA Interchile (Transmisión 500 kV)

| Falla | Descripción |
|---|---|
| Acción no autorizada | Reinicio del módulo de comunicaciones de la protección diferencial 87L **sin avisar ni pedir autorización al CEN** |
| Protocolo incumplido | Modificación de equipo de comunicaciones sin aviso >= 20 días al Coordinador (AT-SITR-1) |
| Consecuencia | Desconexión intempestiva de ambos circuitos 500 kV |
| Propagación | Falla se expandió al sistema paralelo 220 kV → división del SEN en dos islas |

**Skill relevante:** `skill_transmision.md` — obligatoriedad de aviso previo ante cambios en equipos de comunicación/protección

---

### 2. Agravante — Transelec (Transmisión 220 kV / Centro de Control)

| Falla | Descripción |
|---|---|
| SCADA principal perdido | Centro de Control Transelec perdió visibilidad SCADA durante el evento |
| Telecontrol perdido | Sin capacidad de maniobra remota de equipos |
| Hot Line perdida | Sin comunicación de voz operativa con el CEN |
| SCADA respaldo tardó | +1 hora 20 min en activarse |
| SITR hacia CEN | CEN no recibía señales SITR actualizadas de Transelec durante la crisis |
| Hallazgos auditoría | 38 hallazgos de alta criticidad en SCADA y telecomunicaciones |

**Skills relevantes:**
- `skill_base_sitr.md` — disponibilidad SITR debe ser >= 99.5%; durante el evento fue 0%
- `skill_transmision.md` — redundancia de sistemas y comunicaciones requerida
- `skill_vigilancia_normativa.md` — mantenimiento preventivo de sistemas SCADA

---

### 3. EDAC — Desempeño Deficiente

| Situación | Descripción |
|---|---|
| EDAC actuaron | Sí, varios esquemas se activaron ante la caída de frecuencia |
| Desempeño | Desempeño deficiente en algunos esquemas — no lograron estabilizar el sistema |
| Causa probable | Configuraciones no actualizadas, o tiempos de operación fuera de rango |
| Desbalance inicial | ~1.800 MW desconectados del norte → 25% de la demanda del sistema centro-sur |

**Skill relevante:** `skill_edac_edag_erag.md`

---

## Brechas Normativas Identificadas (Real)

| Empresa | Brecha | Normativa incumplida |
|---|---|---|
| ISA Interchile | Modificación de protección sin aviso al CEN | AT-SITR-1: aviso >= 20 días |
| ISA Interchile | Sin plan de acción ni comunicación previa | Procedimientos CEN |
| Transelec | SCADA sin redundancia efectiva (respaldo tardó +80 min) | NTSyCS: redundancia de sistemas |
| Transelec | Hot Line indisponible durante emergencia | NTSyCS: voz operativa >= 99.5% |
| Transelec | SITR sin envío de datos al CEN durante crisis | SITR dic-2019: disponibilidad >= 99.5% |
| Múltiples | EDAC sin desempeño en rango correcto | EDAC/EDAG jun-2015: 80-120%, <= 200 ms |

---

## Lecciones para Coordinados (Aplicación en CONECTA)

| Lección | Skill asociada | Acción preventiva |
|---|---|---|
| NUNCA modificar protecciones sin aviso al CEN | skill_base_sitr + skill_transmision | Implementar proceso formal de cambios con aviso >= 20 días |
| SCADA de respaldo debe estar siempre listo | skill_base_sitr | Probar respaldo mensualmente; medir tiempo de conmutación |
| Hot Line debe estar operativa 24/7 | skill_base_sitr | Incluir en reporte de disponibilidad mensual |
| EDAC debe probarse y calibrarse periódicamente | skill_edac_edag_erag | Programar pruebas periódicas y registrar resultados |
| SITR debe tener redundancia de comunicaciones | skill_base_sitr | Enlace primario + respaldo siempre activos |

---

## Consecuencias Legales y Regulatorias

- **SEC formuló cargos** contra ISA Interchile y Transelec
- **CEN inició auditorías técnicas** a ambas empresas (SCADA, protecciones, telecomunicaciones)
- **EPRI + 3 universidades chilenas** realizaron análisis independiente
- **Actualizaciones normativas** esperadas como consecuencia del evento

---

## Ejemplo de Diagnóstico que CONECTA Podría Ofrecer (Post-Evento)

Si CONECTA fuera contratada como asesora de Transelec post-evento, los skills a activar serían:

```
1. skill_diagnostico_rapido     → Identificar: transmisión STN, con SITR y EDAC
2. skill_transmision            → Verificar disponibilidad SITR, SCADA y PDC
3. skill_base_sitr              → Diagnosticar brechas de disponibilidad y redundancia
4. skill_edac_edag_erag         → Revisar configuraciones y registros de eventos
5. skill_vigilancia_normativa   → Monitorear resoluciones SEC post-apagón
6. skill_informe_tecnico        → Generar informe para reguladores (SEC/CEN)
```

## Fuentes Verificables
- CEN: https://www.coordinador.cl/publicaciones/ (EAF publicado mar-2025)
- Prensa técnica: ex-ante.cl, reporteminero.cl
- Universidad de Chile: análisis sistémico publicado ago-2025
