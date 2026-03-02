# Ejemplo: Memoria de Cálculo — Tablero Industrial 400 A

**Skill utilizada:** `skill_memoria_calculo`
**N° Documento:** CON-ING-2025-004-MEM, Rev. 1  
**Proyecto:** Ampliación eléctrica planta acuícola, Puerto Montt

---

## 1. Resumen Ejecutivo

El presente cálculo dimensiona el tablero general de baja tensión (TGBT) ampliado para la planta procesadora Los Canales, considerando la incorporación de 3 nuevas líneas de proceso con una potencia instalada adicional de 185 kW. Se concluye que el alimentador existente de 400 A es insuficiente y debe reemplazarse por uno de 630 A.

---

## 2. Normativa Aplicable

- [N01] NCh Elec 4/2003 — Instalaciones de consumo en baja tensión
- [N02] IEC 60364-4-43 — Protección contra sobreintensidades
- [N03] IEC 60228 — Conductores de cables aislados
- [N04] IEC 60947-2 — Interruptores automáticos

---

## 3. Inventario de Cargas

| N° | Descripción | P instalada (kW) | FP | FD | P demandada (kW) |
|---|---|---|---|---|---|
| 1 | Motor bomba A (existente) | 75 | 0.87 | 0.80 | 60.0 |
| 2 | Motor bomba B (existente) | 75 | 0.87 | 0.70 | 52.5 |
| 3 | Alumbrado (existente) | 20 | 1.00 | 1.00 | 20.0 |
| 4 | **Nueva línea proceso 1** | 90 | 0.85 | 0.80 | 72.0 |
| 5 | **Nueva línea proceso 2** | 55 | 0.85 | 0.75 | 41.3 |
| 6 | **Nueva línea proceso 3** | 40 | 0.85 | 0.80 | 32.0 |
| | **TOTAL** | **355 kW** | | | **277.8 kW** |

---

## 4. Dimensionamiento del Alimentador Principal

**Corriente de diseño:**
```
In = P_demandada / (√3 × Vnom × FP_medio × η)
In = 277,800 / (1.732 × 400 × 0.86 × 0.94)
In = 277,800 / 560.5 = 496 A

Factores de corrección (cable en bandeja, 35°C ambiente):
Fc_temp = 0.94   (para cable XLPE 90°C a 35°C)
Fc_agrup. = 0.80  (4 cables en bandeja)

Id = In / (Fc_temp × Fc_agrup.) = 496 / (0.94 × 0.80) = 660 A
```

**Cable seleccionado:** 3×(1×300 mm² Cu XLPE 90°C) + N(1×150 mm²) + T(1×95 mm²)
- Corriente admisible Iz = 690 A > 660 A ✅

**Verificación caída de tensión (longitud: 45 m):**
```
ΔV% = (√3 × In × L × (R·cosφ + X·senφ)) / Vnom × 100
     = (1.732 × 496 × 0.045 × (0.060×0.86 + 0.075×0.51)) / 400 × 100
     = (38.73 × (0.0516 + 0.0383)) / 400 × 100
     = (38.73 × 0.0899) / 400 × 100 = 0.87% < 5% [N01] ✅
```

---

## 5. Dimensionamiento de Protección Principal

```
Condición 1: In_prot >= In_circuito       → >= 496 A
Condición 2: In_prot <= Iz_cable          → <= 690 A
Resultado: Interruptor 630 A seleccionado ✅

Poder de ruptura requerido: Icc_BT = 23.9 kA (ver example_cortocircuito)
Poder de ruptura seleccionado: 36 kA ✅
```

**Protección diferencial principal:** IDn = 300 mA (instalación industrial)

---

## 6. Sistema de Puesta a Tierra

```
Suelo: Franco-arcilloso, ρ = 80 Ω·m (medición terreno)

Electrodo vertical L = 3 m, d = 0.016 m:
R = ρ/(2πL) × ln(4L/d) = 80/(2π×3) × ln(750) = 4.244 × 6.62 = 28.1 Ω

Para cumplir R <= 25 Ω → 2 electrodos en paralelo con separación >= 6 m:
R_paralelo = 28.1 / 2 × 1.08 (factor de interferencia) = 15.2 Ω ✅
```

---

## 7. Conclusiones

| Ítem | Resultado | Estado |
|---|---|---|
| Alimentador | 3×300 mm² Cu XLPE | ✅ Seleccionado |
| Caída de tensión | 0.87% | ✅ < 5% |
| Protección principal | 630 A / 36 kA | ✅ Seleccionado |
| Sistema de tierra | 2 electrodos → 15.2 Ω | ✅ < 25 Ω |

**El alimentador existente de 400 A es insuficiente.** Se requiere reemplazo por 630 A conforme a los cálculos y normativa [N01].
