# Ejemplo: Cumplimiento CEN — PMGD Parque Solar 28 MW (Umbral PMUS)

**Skill utilizada:** `skill_pmgd_pmg`
**Tipo de coordinado:** PMGD solar fotovoltaico — evaluación umbral PMUS

---

## Inputs del caso

- Empresa: Solar Atacama PMGD SpA
- Instalación: Parque solar 5 unidades PMGD de 5.6 MW c/u = 28 MW total
- Punto de conexión: S/E distribuidora "Los Álamos" 23 kV, Antofagasta
- Distribuidora: Distribuidora Norte S.A.
- Enlace SITR: Vía sistema comunicaciones Distribuidora Norte

---

## Evaluación del Umbral PMUS

> **Regla clave:** Si en una S/E de distribución se concentran PMGD con potencia total > 20 MW, puede requerirse PMU.

```
Total PMGD en S/E Los Álamos: 28 MW > 20 MW → EVALUAR en estudio MMF
```

| Pregunta | Respuesta |
|---|---|
| ¿Supera 20 MW en la S/E? | ✅ Sí — 28 MW |
| ¿Aparece S/E Los Álamos en estudio MMF 2025? | ⚠️ Verificar con CEN |
| ¿PMU instalada actualmente? | ❌ No |

**Acción requerida:** Solicitar al Coordinador si S/E Los Álamos está en el estudio MMF vigente.

---

## Verificación SITR vía Distribuidora

| Parámetro | Estado | Evidencia |
|---|---|---|
| Acuerdo formal con Distribuidora Norte | ✅ Firmado mar-2024 | Contrato ref. DN-2024-089 |
| Protocolo SITR acordado | ✅ DNP3 TCP/IP | Aprobado por CEN |
| Disponibilidad mensual | 99.6% | Reporte feb-2025 |
| Medidas para Coordinador | ✅ P, Q, V, estado | En tiempo real |
| Medidas para Distribuidora | ✅ P, Q, V, estado | En tiempo real |
| Diagrama de conexión aprobado | ✅ | Rev. 2, ene-2025 |

---

## Tabla de Brechas

| ID | Brecha | Criticidad | Acción | Plazo |
|---|---|---|---|---|
| P01 | Verificar si S/E aparece en estudio MMF 2025 (posible obligación PMUS) | 🟠 Media | Consultar al Coordinador y revisar estudio MMF | 15 días |
| P02 | Si MMF incluye S/E: instalar PMU con specs requeridas | 🔴 Alta (si aplica) | Planificar ingeniería e instalación | 6 meses desde confirmación |

---

## Conclusión
El PMGD cumple sus obligaciones SITR actuales via distribuidora. El punto de atención es el **umbral de 28 MW > 20 MW** que puede gatillar la obligación de PMUS. La primera acción es confirmar con el Coordinador si la S/E está en el estudio MMF 2025.
