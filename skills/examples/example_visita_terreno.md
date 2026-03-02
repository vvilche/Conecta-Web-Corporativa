# Ejemplo: Inspección en Terreno — S/E Industrial Puerto Montt

**Skill utilizada:** `skill_visita_terreno`
**Objetivo:** Diagnóstico general instalación eléctrica MT/BT
**Fecha:** 2025-02-18 | **Asistentes:** Ingeniero CONECTA + Jefe mantenimiento cliente

---

## 1. Datos de la Visita

| Campo | Dato |
|---|---|
| Empresa | Acuícola Los Canales SpA |
| Instalación | Planta Puerto Montt, S/E 23/0.4 kV, 1000 kVA |
| Objetivo | Diagnóstico previo a ampliación eléctrica |
| EPP utilizado | Casco + guantes dieléctricos Clase 2 + calzado dieléctrico + lentes |
| LOTO aplicado | Sí — interruptores Q1 (MT) y Q2 (BT) bloqueados para inspección visual |

---

## 2. Resumen Ejecutivo

La instalación presenta un estado general **aceptable con observaciones mayores** que deben resolverse antes de la ampliación. Se identificaron 1 observación crítica, 3 mayores y 4 menores. La más urgente es la ausencia de protección a tierra en el tablero de alumbrado exterior (riesgo de electrocución).

---

## 3. Registro de Mediciones

| Punto | Medición | Valor | Límite | Estado |
|---|---|---|---|---|
| Barra BT | Tensión L1-L2 | 402 V | 380–415 V | ✅ |
| Barra BT | Corriente L1/L2/L3 | 285/290/288 A | 400 A máx | ✅ |
| Barra BT | Desequilibrio corriente | 0.9% | <= 10% | ✅ |
| Electrodo tierra 1 | Resistencia | 18.4 Ω | <= 25 Ω | ✅ |
| Motor bomba A | Temperatura carcasa | 62°C | <= 75°C (Clase F) | ✅ |
| Transformador T1 | Temperatura aceite | 58°C | <= 95°C | ✅ |
| Tablero alumbrado ext. | Resistencia tierra | sin tierra | — | ❌ |

---

## 4. Tabla de Observaciones

| N° | Área | Observación | Evidencia | Categoría | Recomendación | Plazo |
|---|---|---|---|---|---|---|
| OBS-001 | Tablero alumbrado ext. | Circuitos sin conductor de tierra — riesgo electrocución | Foto 023 | 🔴 Crítico | Instalar conductor PE y diferencial 30 mA | Inmediato |
| OBS-002 | Celda MT entrada | Empaque de sello en tapa posterior deteriorado — posible ingreso de humedad | Foto 008 | 🟠 Mayor | Reemplazar empaque y revisar interior | 15 días |
| OBS-003 | Bandeja cable BT | Bandeja al 85% de llenado — supera el 40% recomendado IEC para BT | Foto 015 | 🟠 Mayor | Ampliar bandeja o instalar bandeja adicional | 30 días |
| OBS-004 | Interruptor Q-08 | Sin etiqueta de circuito actualizada: dice "bomba 2" pero ahora alimenta línea proceso | Foto 019 | 🟠 Mayor | Reetiquetado según unifilar aprobado | 15 días |
| OBS-005 | Tablero TGBT | Extintor vencido (caducó ene-2025) | Foto 031 | 🟡 Menor | Recargar/reemplazar extintor | 7 días |
| OBS-006 | Puesta a tierra | Unión equipotencial del transformador con corrosión visible | Foto 006 | 🟡 Menor | Limpiar y retorcar la unión, aplicar grasa antioxidante | 30 días |
| OBS-007 | Sala eléctrica | Iluminación de emergencia sin funcionar (batería descargada) | Foto 033 | 🟡 Menor | Reemplazar batería luminaria emergencia | 15 días |
| OBS-008 | General | No se encontró el plano unifilar as-built actualizado en sala | — | 🟡 Menor | Actualizar y plastificar plano vigente en sala | 30 días |

---

## 5. Plan de Acción

| Prioridad | N° obs. | Responsable | Fecha límite |
|---|---|---|---|
| 🔴 Inmediato | OBS-001 | Contratista eléctrico + cliente | 2025-02-25 |
| 🟠 15 días | OBS-002, OBS-004, OBS-007 | Mantenimiento cliente | 2025-03-05 |
| 🟡 30 días | OBS-003, OBS-005, OBS-006, OBS-008 | Mantenimiento cliente | 2025-03-20 |

---

## 6. Conclusión

La instalación puede operar con las condiciones actuales, pero **OBS-001 debe resolverse antes de cualquier trabajo eléctrico adicional y antes de la ampliación prevista**. Se recomienda una re-inspección tras cierre de observaciones críticas y mayores.
