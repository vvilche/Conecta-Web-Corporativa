# Ejemplo: Cumplimiento PMUS — Empresa Transmisión STN

**Skill utilizada:** `skill_transmision`
**Tipo de coordinado:** Empresa de transmisión nacional (STN), 4 subestaciones

---

## Inputs del caso

- Empresa: Transmisora Cordillera S.A.
- Instalaciones STN: 4 subestaciones (Arrayán 220 kV, Melipilla 220 kV, Las Vegas 110 kV, Pelequén 110 kV)
- PDC Local: Instalado en S/E Arrayán (Schweitzer SEL-3373)
- Estado actual: PMU instaladas en Arrayán y Melipilla; Las Vegas y Pelequén sin PMU

---

## Revisión Estudio MMF 2025

| Subestación | Incluida en MMF 2025 | PMU requerida | PMU instalada | Estado |
|---|---|---|---|---|
| Arrayán 220 kV | ✅ Sí | Sí | ✅ Sí (SEL-421) | ✅ OK |
| Melipilla 220 kV | ✅ Sí | Sí | ✅ Sí (SEL-421) | ✅ OK |
| Las Vegas 110 kV | ✅ Sí | Sí | ❌ No | 🔴 Brecha crítica |
| Pelequén 110 kV | ✅ Sí | Sí | ❌ No | 🔴 Brecha crítica |

---

## Verificación SITR Base

| Parámetro | Requisito | Valor actual | Estado |
|---|---|---|---|
| Disponibilidad mensual | >= 99.5% | 99.7% | ✅ OK |
| GPS todas las S/E | +/- 100 µs | Solo Arrayán y Melipilla con GPS | ⚠️ Parcial |
| Edad de datos | <= 5 s | 2 s promedio | ✅ OK |
| Respaldo alimentación SITR | >= 6 h | 8 h en todas las S/E | ✅ OK |

---

## Verificación Integración PDC

| Elemento | Estado | Observación |
|---|---|---|
| PDC Local (Arrayán) | ✅ Operativo | Conectado al SuperPDC del CEN |
| Segundo enlace PDC-CEN | ❌ No implementado | Solo enlace primario activo |
| PMU Arrayán → PDC | ✅ Integrada | IEEE C37.118, 50 mps |
| PMU Melipilla → PDC | ✅ Integrada | IEEE C37.118, 50 mps |

---

## Tabla de Brechas

| ID | Brecha | Criticidad | Plazo | Inversión estimada |
|---|---|---|---|---|
| T01 | PMU no instalada en Las Vegas 110 kV | 🔴 Alta | 6 meses | ~USD 45,000 |
| T02 | PMU no instalada en Pelequén 110 kV | 🔴 Alta | 6 meses | ~USD 45,000 |
| T03 | Segundo enlace PDC-CEN no implementado | 🟠 Media | 3 meses | ~USD 8,000 |
| T04 | GPS no instalado en Las Vegas y Pelequén | 🟠 Media | 3 meses (junto con PMU) | Incluido en T01/T02 |

---

## Plan de Acción Propuesto

1. **Mes 1-2:** Ingeniería básica PMU Las Vegas y Pelequén + cotizaciones
2. **Mes 2-3:** Implementar segundo enlace PDC-CEN (acción más rápida)
3. **Mes 3-5:** Adquisición e instalación PMU según dossier PES
4. **Mes 5-6:** Pruebas de integración y comisionamiento con el CEN
5. **Mes 6:** Cierre formal de brechas T01–T04

**Nota:** El plazo máximo es 31 de julio de cada año (actualización estudio MMF). Si el estudio MMF 2025 fue publicado en julio-2025, el plazo de implementación máximo según AT-SITR-1 es 12 meses desde publicación en D.O.
