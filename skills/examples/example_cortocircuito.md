# Ejemplo: Cálculo de Cortocircuito — S/E Industrial Puerto Montt

**Skill utilizada:** `skill_calculo_cortocircuito`
**Tipo de instalación:** Subestación industrial MT/BT, 23/0.4 kV, 1000 kVA

---

## Datos de Entrada

- Tensión de red MT: 23 kV
- Potencia de cortocircuito en barra 23 kV: Scc = 350 MVA (dato SEC/distribuidora)
- Transformador T1: 1000 kVA, 23/0.4 kV, Z% = 5.75%, grupo vector Dyn11
- Cable MT: no aplica (conexión directa en barra de S/E distribución)
- Cables BT: 3 × (1×240 mm² Cu XLPE), longitud 80 m desde tablero BT del T1

---

## Cálculo Icc en Barra MT (23 kV)

```
Icc3φ_MT = Scc / (√3 × Vnom) = 350 × 10⁶ / (1.732 × 23 × 10³)
Icc3φ_MT = 8.786 kA simétrico

Ipico_MT = Icc3φ × √2 × k = 8.786 × 1.414 × 1.7 = 21.1 kA
  (k = 1.7 para red MT, factor de asimetría IEC 60909)
```

---

## Cálculo Icc en Tablero BT (0.4 kV) — Barra Principal

### Base: Sbase = 1 MVA, Vbase = 0.4 kV

```
Zbase_BT = Vbase² / Sbase = 0.16 / 1 = 0.16 Ω

Z_red_MT_pu = Sbase / Scc = 1 / 350 = 0.00286 pu

Z_trafo_pu = (Z% / 100) × (Sbase / Strafo) = (5.75 / 100) × (1 / 1) = 0.0575 pu

Zcc_total_pu = Z_red + Z_trafo = 0.00286 + 0.0575 = 0.06036 pu

Ibase_BT = Sbase / (√3 × Vbase) = 1 × 10⁶ / (1.732 × 400) = 1443 A

Icc3φ_BT = 1 / Zcc_total_pu × Ibase_BT = (1 / 0.06036) × 1443 = 23.9 kA

Ipico_BT = Icc3φ × √2 × k = 23.9 × 1.414 × 1.4 = 47.3 kA
  (k = 1.4 para redes BT industriales)
```

---

## Cálculo Icc al Final del Cable BT (80 m)

```
Cable: 240 mm² Cu XLPE    →   R = 0.0754 Ω/km, X = 0.090 Ω/km
                               R_cable = 0.0754 × 0.08 = 0.00603 Ω/fase
                               X_cable = 0.090 × 0.08  = 0.00720 Ω/fase

Z_cable = √(R² + X²) = √(0.00603² + 0.00720²) = 0.00939 Ω
Z_cable_pu = 0.00939 / 0.16 = 0.0587 pu

Zcc_total_final = 0.06036 + 0.0587 = 0.11906 pu
Icc3φ_final = (1 / 0.11906) × 1443 = 12.12 kA
```

---

## Tabla Resumen de Resultados

| Punto | Unom | Icc3φ sim (kA) | Ipico (kA) | Poder ruptura existente | Estado |
|---|---|---|---|---|---|
| Barra MT 23 kV | 23 kV | 8.79 | 21.1 | 25 kA | ✅ OK |
| Barra BT tablero | 0.4 kV | 23.9 | 47.3 | 50 kA | ✅ OK |
| Final cable 80 m | 0.4 kV | 12.1 | 24.0 | — | ✅ Info |

---

## Verificación de Protecciones

| Interruptor | Ubicación | In (A) | Poder ruptura (kA) | Icc local (kA) | Estado |
|---|---|---|---|---|---|
| Q1 (entrada MT) | 23 kV | 40 A | 25 kA | 8.79 kA | ✅ OK |
| Q2 (salida BT) | 0.4 kV | 1600 A | 50 kA | 23.9 kA | ✅ OK |
| Q3 (tablero secundario) | 0.4 kV | 400 A | 15 kA | 12.1 kA | ✅ OK |

---

## Conclusión
Todos los equipos existentes tienen capacidad de ruptura suficiente. La barra BT tiene una Icc de **23.9 kA**, lo que debe considerarse para cualquier ampliación futura del transformador o de la potencia de red.
