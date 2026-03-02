---
name: calculating-short-circuit
description: Realiza y revisa análisis de cortocircuito en sistemas eléctricos. Usar cuando el usuario mencione "cortocircuito", "Icc", "corriente de falla", "cálculo de falla", "poder de ruptura" o "coordinación de protecciones".
---

# Skill: Cálculo de Cortocircuito

## Cuándo usar este skill
- Usuario pide "calcular cortocircuito" o "Icc en barra X"
- Se necesita verificar capacidad de ruptura de interruptores
- Se requiere base para ajuste de protecciones
- Se evalúa impacto de nuevo equipo en corrientes de falla

## Workflow

```markdown
- [ ] Recopilar datos del sistema (impedancias, tensiones nominales, topología)
- [ ] Definir punto(s) de falla a analizar
- [ ] Calcular Icc trifásico (falla más severa)
- [ ] Calcular Icc monofásico a tierra
- [ ] Calcular Icc bifásico y bifásico a tierra si aplica
- [ ] Comparar con capacidades de equipos existentes
- [ ] Documentar resultados y observaciones
```

## Instrucciones

### 1. Datos Requeridos
Recopilar del usuario:
- Diagrama unifilar del sistema (o descripción topológica)
- Potencia de cortocircuito en barra de alimentación (MVA o kA)
- Impedancias de transformadores (Z%, potencia nominal, relación de transformación)
- Impedancias de líneas y cables (R, X, B por unidad de longitud)
- Datos de generadores locales si aplica (Xd'', Xd', Xd)
- Tensión nominal de cada barra analizada

### 2. Método de Cálculo

**Método Simplificado (verificación rápida):**
```
Icc3φ = Unom / (√3 × Zcc_total)
Icc1φ = (3 × Unom) / (√3 × (Z1 + Z2 + Z0))
```

**Nivel de tensión y factor c (IEC 60909):**
| Tensión nominal | c_max | c_min |
|---|---|---|
| BT (≤ 1 kV) | 1.05 | 0.95 |
| MT (1–35 kV) | 1.10 | 1.00 |
| AT (> 35 kV) | 1.10 | 1.00 |

**Impedancias típicas de referencia:**
- Transformador distribución 630 kVA 23/0.4 kV: Z% ≈ 4-6%
- Transformador potencia 10 MVA 110/23 kV: Z% ≈ 8-12%
- Cable XLPE 240 mm² (23 kV): R ≈ 0.078 Ω/km, X ≈ 0.12 Ω/km

### 3. Cálculo en Sistema por Unidad (p.u.)

```
Base: Sbase (MVA), Vbase (kV)
Zbase = Vbase² / Sbase  [Ω]

Z_trafo_pu = (Z% / 100) × (Sbase / Strafo)
Z_linea_pu = Z_linea_Ω / Zbase
Ibase = Sbase / (√3 × Vbase)  [kA]

Icc3φ = 1.0 / Zcc_total  [p.u.] → Icc_kA = Icc_pu × Ibase
```

### 4. Verificación de Equipos
Comparar resultados contra:
- **Poder de ruptura** del interruptor (kA simétrico)
- **Corriente de cierre** (valor pico = Icc × √2 × factor k)
- **Corriente de corta duración** (1 s o 3 s)
- **Capacidad dinámica** de barras y conexiones

Valores de factor de asimetría k (IEC 60909):
- Redes AT: k ≈ 1.7–1.8
- Redes MT: k ≈ 1.5–1.7
- Redes BT: k ≈ 1.2–1.4

### 5. Tabla de Resultados Estándar

| Barra | Unom (kV) | Icc3φ sim (kA) | Icc1φ (kA) | Ipico (kA) | Estado |
|---|---|---|---|---|---|
| B1 | 110 | — | — | — | ✅/⚠️/❌ |
| B2 | 23 | — | — | — | ✅/⚠️/❌ |
| B3 | 0.4 | — | — | — | ✅/⚠️/❌ |

### 6. Criterios de Aceptación
- ✅ Icc < 80% del poder de ruptura del interruptor
- ⚠️ Icc entre 80–100% → requiere revisión del equipo
- ❌ Icc > poder de ruptura → equipo subdimensionado, acción correctiva urgente

## Errores Comunes
- ❌ **Usar solo Icc trifásico para verificar la protección** — la falla monofásica puede ser menor y no ser detectada por el relé si el pick-up está muy alto
- ❌ **Olvidar el factor de pico (Ipico)** — los interruptores tienen requisitos de corriente de cierre; comparar solo Icc simétrico puede llevar a subdimensionar
- ❌ **No convertir las impedancias a la misma base** — si se mezclan valores en Ω y p.u. sin convertir, el resultado es incorrecto
- ❌ **Asumir que el Icc del sistema no cambia con el proyecto** — un generador nuevo aporta corriente de cortocircuito; recalcular siempre post-conexión
- ❌ **No calcular el Icc mínimo** — para ajustar protecciones se necesita el Icc mínimo (condición de red reducida) además del máximo

## Ejemplo Real
- [S/E Industrial Puerto Montt — Tablero MT/BT 1000 kVA](examples/example_cortocircuito.md)

## Salidas Esperadas
- Tabla resumen de corrientes de cortocircuito por barra
- Identificación de equipos con capacidad insuficiente
- Recomendaciones de refuerzo o ajuste de protecciones
