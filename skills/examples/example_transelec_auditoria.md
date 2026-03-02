# Ejemplo Real: Auditoría SITR/SCADA — Empresa Transmisora STN (Basado en Transelec 2025)

**Skill utilizada:** `skill_transmision` + `skill_base_sitr` + `skill_vigilancia_normativa`
**Contexto real:** Auditoría técnica realizada post-apagón 25-feb-2025 encontró 38 hallazgos de alta criticidad
**Tipo de caso:** Diagnóstico preventivo completo de una transmisora STN

> 💡 Este ejemplo simula el servicio que CONECTA podría ofrecer a una transmisora para hacer este diagnóstico **antes** de que ocurra el evento.

---

## Datos de la Empresa Analizada

| Dato | Valor |
|---|---|
| Tipo de coordinado | Transmisora STN (Sistema de Transmisión Nacional) |
| Instalaciones | 12 subestaciones AT (110–500 kV); 3.200 km de líneas |
| Centro de Control principal | Ciudad X — SCADA propio con 1.200 puntos de medición |
| Centro de Control respaldo | Ciudad Y — SCADA espejo |
| SITR | Protocolo ICCP hacia el CEN; 85 puntos de medición |

---

## Workflow Ejecutado

```markdown
- [x] Inventario de sistemas SCADA (principal + respaldo)
- [x] Verificación de tiempos de conmutación a respaldo
- [x] Revisión de Hot Line y voz operativa
- [x] Verificación disponibilidad SITR 12 meses
- [x] Revisión de planes de mantenimiento preventivo
- [x] Prueba de telecontrol remoto en condiciones de falla
- [x] Evaluación de puntos de falla única en telecomunicaciones
- [x] Clasificación de hallazgos por criticidad
- [x] Plan de acción priorizando hallazgos de alta criticidad
```

---

## Verificación SITR 12 Meses

| S/E | Disponibilidad promedio 12 meses | Mes peor | Disponibilidad mes peor | Estado |
|---|---|---|---|---|
| S/E Norte 500 kV | 99.72% | Jul-2024 | 99.01% | ✅ OK |
| S/E Centro 220 kV | 99.61% | Nov-2024 | 98.92% | ✅ OK (límite) |
| S/E Sur 110 kV | **97.84%** | Ago-2024 | **95.21%** | ❌ Crítico |
| S/E Costa 110 kV | **99.32%** | Feb-2025 | **98.10%** | ❌ Incumple |
| Promedio global | 99.12% | — | — | ❌ No cumple 99.5% |

---

## Verificación Sistema SCADA y Respaldo

| Ítem | Requisito | Estado encontrado | Hallazgo |
|---|---|---|---|
| SCADA principal operativo | 24/7 | ✅ Operativo (99.9%) | — |
| SCADA respaldo disponible | 24/7 activo/listo | ⚠️ En modo "frío" (requiere arranque manual) | H-01 |
| Tiempo conmutación a respaldo | Recomendado: <= 5 min | **82 minutos** en prueba realizada | H-02 🔴 |
| Pruebas periódicas de respaldo | Mensual recomendado | Última prueba: 14 meses atrás | H-03 🔴 |
| Sincronización SCADA-respaldo | Datos en tiempo real | Solo sincroniza cada 6 horas | H-04 🟠 |
| Configuración actualizaciones | Automática | Manual — requiere intervención operador | H-05 🟠 |

---

## Verificación Comunicaciones Operacionales

| Canal | Requisito | Estado | Hallazgo |
|---|---|---|---|
| Hot Line principal (voz) | >= 99.5% disponible | 98.9% — 3 puntos con falla batería | H-06 🔴 |
| Hot Line respaldo (celular) | Operativo | Sin plan celular activo en 2 S/E rurales | H-07 🔴 |
| Canal ICCP principal | Operativo | ✅ 99.72% disponibilidad | — |
| Canal ICCP respaldo | Requerido | ❌ Solo canal principal activo | H-08 🔴 |
| Grabación de voz >= 6 meses | Requerida | Solo 3 meses de retención configurados | H-09 🟠 |
| Sincronización grabación +/- 1 s | Requerida | +/- 3.2 s — fuera de rango | H-10 🟠 |

---

## Verificación Mantenimiento Preventivo

| Sistema | Frecuencia req. | Última ejecución | Próxima prog. | Hallazgo |
|---|---|---|---|---|
| UPS salas de control | 6 meses | 22 meses atrás | No programada | H-11 🔴 |
| Baterías Hot Line | 12 meses | 18 meses atrás | No programada | H-12 🔴 |
| Equipos GPS (calibración) | 12 meses | 8 meses — OK | Jun-2025 | ✅ |
| RTUs y equipos SITR | 12 meses | 14 meses atrás | No programada | H-13 🟠 |
| Pruebas protecciones 87L | 24 meses | 31 meses atrás | No programada | H-14 🔴 |
| Revisión firmware SCADA | 18 meses | 36 meses atrás | No programada | H-15 🟠 |

---

## Resumen de Hallazgos (Top 15 — de 38 totales)

| ID | Sistema | Descripción resumida | Criticidad |
|---|---|---|---|
| H-01 | SCADA Respaldo | Modo frío — requiere arranque manual | 🔴 Alta |
| H-02 | SCADA Respaldo | Tiempo conmutación 82 min (>> 5 min) | 🔴 Alta |
| H-03 | SCADA Respaldo | Sin prueba periódica (14 meses sin probar) | 🔴 Alta |
| H-04 | SCADA Respaldo | Sincronización solo cada 6 h (no tiempo real) | 🟠 Media |
| H-05 | SCADA | Actualizaciones de configuración manuales | 🟠 Media |
| H-06 | Hot Line | 3 puntos con batería sin carga | 🔴 Alta |
| H-07 | Hot Line | Sin enlace de voz respaldo en 2 S/E | 🔴 Alta |
| H-08 | SITR/ICCP | Sin canal ICCP respaldo | 🔴 Alta |
| H-09 | Grabación voz | Retención 3 meses (< 6 meses requerido) | 🟠 Media |
| H-10 | Grabación voz | Sincronización +/- 3.2 s (requiere +/- 1 s) | 🟠 Media |
| H-11 | UPS | Sin mantenimiento en 22 meses | 🔴 Alta |
| H-12 | Baterías Hot Line | Sin mantenimiento en 18 meses | 🔴 Alta |
| H-13 | RTUs/SITR | Sin mantenimiento en 14 meses | 🟠 Media |
| H-14 | Protección 87L | Sin prueba en 31 meses | 🔴 Alta |
| H-15 | Firmware SCADA | Sin actualización en 36 meses | 🟠 Media |

**Totales:** 9 hallazgos 🔴 Alta + 6 hallazgos 🟠 Media (en top 15)  
*(38 hallazgos totales como encontró la auditoría real post-apagón)*

---

## Plan de Acción Priorizado por CONECTA

| Plazo | Hallazgos | Acción principal |
|---|---|---|
| **Inmediato (0–15 días)** | H-01, H-02, H-03 | Pasar SCADA respaldo a modo "caliente"; hacer prueba de conmutación |
| **15–30 días** | H-06, H-07, H-08 | Reemplazar baterías Hot Line; activar canal ICCP respaldo |
| **30–45 días** | H-11, H-12 | Mantenimiento UPS y baterías; programar calendario semestral |
| **45–60 días** | H-14 | Prueba protección 87L; actualizar firmware SCADA |
| **60–90 días** | H-04, H-05, H-09, H-10, H-13, H-15 | Mejoras de proceso y configuración |

---

## Impacto Normativo Mitigado

Al resolver los 38 hallazgos, la empresa:
- Evita cargos SEC por indisponibilidad SCADA y comunicaciones
- Lleva disponibilidad SITR promedio de 99.12% → >= 99.5% en todas las S/E
- Cumple con NTSyCS para voz operativa (>= 99.5%)
- Cumple con AT-SITR-1 para canal respaldo ICCP

**Propuesta de valor CONECTA:** *"Diagnóstico en 4 semanas antes de que el CEN o la SEC te auditen"*
