# Ejemplo: Estudio ECAP — Conexión PMGD Parque Eólico 5 MW

**Skill utilizada:** `skill_estudio_ecap` + `skill_calculo_cortocircuito`
**Tipo de proyecto:** PMGD eólico 5 MW, conexión en barra MT 23 kV de S/E Distribución

---

## Inputs del caso

- Proyecto: Parque Eólico Punta Negra — 5 MW (5 aerogeneradores de 1 MW)
- Punto de conexión propuesto: Barra 23 kV, S/E Distribución Litoral Norte
- Empresa distribuidora: Cooperativa Eléctrica Litoral
- Tecnología: Aerogeneradores con convertidor full back-to-back (control de potencia independiente)
- FP: 0.95 ind/cap (control activo)
- Datos de red: Icc3φ en barra 23 kV = 6.2 kA simétrico (dato del Coordinador)
- Transformador de conexión: 5.5 MVA, 23/0.69 kV, Z = 6%

---

## Análisis de Flujo de Potencia

### Caso Base (inyección máxima 5 MW, FP = 0.95)

| Parámetro | Valor calculado | Límite | Estado |
|---|---|---|---|
| Tensión barra 23 kV con proyecto | +1.2% respecto a caso base | <= +5% (NTCSyCS) | ✅ OK |
| Flujo en línea de distribución aguas arriba | 82% de capacidad | <= 100% | ✅ OK |
| Flujo en transformador S/E | 67% de capacidad | <= 100% | ✅ OK |
| Tensión barra en mínima generación (noche) | -0.3% | >= -5% | ✅ OK |

### Contingencia N-1 (pérdida línea principal)
| Parámetro | Valor | Límite | Estado |
|---|---|---|---|
| Tensión barra 23 kV | +4.1% | <= +5% | ✅ OK (ajustado) |
| Flujo línea respaldo | 94% de capacidad | <= 100% | ✅ OK (límite) |

---

## Análisis de Cortocircuito

### Aporte del proyecto al Icc en barra 23 kV

```
Icc_red_previa:  6.20 kA
Icc_proyecto:    I_cc_PMGD ≈ 1.1 × In = 1.1 × (5500 / (√3 × 23)) = 152 A = 0.15 kA
Icc_resultante:  ≈ 6.35 kA (aumento de 2.4%)

Interruptores existentes en barra 23 kV:
  Poder de ruptura: 12.5 kA > 6.35 kA ✅ No requieren cambio
```

---

## Coordinación de Protecciones

| Protección | Función | Ajuste requerido | Estado |
|---|---|---|---|
| R01 (entrada S/E) | 51 (sobrecorriente) | Ip = 450 A, TMS = 0.25 | ✅ Vigente, no requiere ajuste |
| R02 (salida al PMGD) | 51 + 27/59 (anti-isla) | Ip = 175 A, TMS = 0.10; Vmin = 0.85 pu, Vmax = 1.10 pu | ⚠️ **Nuevo relé a instalar** |
| R03 (en transformador PMGD) | 87T + 51N | Diferencial + neutro restringido | ⚠️ **Nuevo a instalar** |

---

## Calidad de Suministro

| Parámetro | Resultado | Límite | Estado |
|---|---|---|---|
| THD tensión en barra 23 kV | 2.8% | <= 8% (IEC 61000-3-6) | ✅ OK |
| Flicker Pst | 0.42 | <= 1.0 | ✅ OK |
| Desequilibrio de tensión | 0.3% | <= 2% | ✅ OK |

---

## Requisitos SITR para PMGD 5 MW

Como PMGD conectado en red distribución:
- Enlace SITR vía sistema de comunicaciones de Cooperativa Litoral → **pendiente acuerdo formal**
- Variables a enviar: potencia activa, potencia reactiva, tensión, estado interruptor
- Disponibilidad >= 99.5% mensual

---

## Conclusión del Estudio ECAP

| Aspecto | Resultado |
|---|---|
| Flujo de potencia | ✅ Sin restricciones |
| Cortocircuito | ✅ Equipos existentes suficientes |
| Protecciones | ⚠️ Requiere instalar 2 nuevos relés (R02, R03) |
| Calidad de suministro | ✅ Cumple |
| SITR | ⚠️ Pendiente acuerdo de enlace con distribuidora |

**Decisión:** PMGD **puede conectarse** cumpliendo las condiciones: instalación de relés R02 y R03, y firma de acuerdo SITR con la distribuidora antes de la conexión.
