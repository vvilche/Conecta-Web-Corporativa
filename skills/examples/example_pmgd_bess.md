# Ejemplo: Diagnóstico PMGD Solar + BESS — 8 MW + 4 MWh

**Skill utilizada:** `skill_pmgd_pmg` + `skill_base_sitr` + `skill_estudio_ecap`
**Contexto:** Tendencia dominante 2025 — PMGD solar con almacenamiento en baterías (BESS)
**Tipo de caso:** Nuevo coordinado con tecnología BESS — evalúa obligaciones normativas completas

> 📌 A febrero 2026, la CNE actualizó la Norma Técnica de Conexión PMGD en MT específicamente para PMGD con BESS. Este ejemplo aplica esa normativa.

---

## Datos del Proyecto

| Dato | Valor |
|---|---|
| Proyecto | Parque Solar Maipo + BESS |
| Empresa | Energía Renovable Maipo SpA |
| Tecnología | Solar FV 8 MW + BESS LFP 4 MWh (1C, 2h de descarga) |
| Punto de conexión | Barra MT 23 kV, S/E Distribución Maipo Norte |
| Distribuidora | Enel Distribución Chile |
| Estado | Construcción — entrada en operación estimada mar-2026 |
| Región | Metropolitana |

---

## Clasificación del Coordinado

```
Potencia instalada solar: 8 MW (< 9 MW → PMGD ✅)
BESS: 4 MWh acoplado en AC → no suma a potencia de conexión
Clasificación: PMGD con almacenamiento (nueva categoría CNE feb-2026)
```

---

## Verificación del Umbral PMUS

```
¿Total PMGD en S/E Maipo Norte supera 20 MW?
  PMGD existentes en esa S/E: 12 MW (3 parques existentes)
  + Este proyecto: 8 MW
  = Total: 20 MW exacto → LÍMITE → EVALUAR con CEN

Acción requerida: Solicitar al Coordinador si la S/E Maipo Norte
aparece en el Estudio MMF vigente.
```

| Evaluación | Resultado |
|---|---|
| Umbral >= 20 MW | ✅ Alcanzado (exacto) |
| S/E en MMF 2025 | ⚠️ Pendiente confirmar con CEN |
| PMU actualmente | ❌ Sin PMU ninguno de los PMGD existentes |

---

## Obligaciones SITR para PMGD+BESS — Análisis Completo

### Variables SITR Requeridas (Solar FV — variables estándar)

| Variable | Unidad | Estado | Observación |
|---|---|---|---|
| Potencia activa solar | MW | ✅ Planificada | RTU configurado |
| Potencia reactiva solar | MVAR | ✅ Planificada | RTU configurado |
| Tensión barra conexión | kV | ✅ Planificada | RTU configurado |
| Estado interruptor principal | Bool | ✅ Planificada | RTU configurado |

### Variables SITR Adicionales BESS (nuevas — feb-2026)

| Variable BESS | Unidad | Estado | Normativa |
|---|---|---|---|
| Potencia activa BESS | MW (+carga / -descarga) | ⚠️ A confirmar con CEN | CNE NT PMGD feb-2026 |
| Estado de carga (SOC) | % | ⚠️ A confirmar con CEN | CNE NT PMGD feb-2026 |
| Estado BESS (cargando/descargando/en espera) | Enum | ⚠️ A confirmar con CEN | CNE NT PMGD feb-2026 |
| Energía acumulada disponible | MWh | ⚠️ A confirmar con CEN | CNE NT PMGD feb-2026 |

> ⚠️ **Atención:** La nueva normativa CNE de feb-2026 introduce variables específicas para BESS. Coordinar con el CEN qué puntos deben enviarse al SITR antes de la entrada en operación.

---

## Análisis ECAP — Impacto en Red MT

### Flujo de Potencia — Modos de Operación BESS

| Modo | Condición | Inyección neta | Impacto en red |
|---|---|---|---|
| Solar máx + BESS descargando | Mediodía sin nubes | +8 MW + 2 MW = **+10 MW** | Mayor tensión en barra |
| Solar máx + BESS cargando | Mediodía exceso solar | +8 MW - 2 MW = **+6 MW** | Menor tensión (absorbe) |
| Solar = 0 + BESS descargando | Noche / demanda pico | **+2 MW** | Inyección nocturna |
| Solar = 0 + BESS cargando | No aplica (solar = 0) | 0 MW | Sin impacto |

**Caso más severo para red:** +10 MW simultáneo (solar máx + BESS descargando)

| Parámetro | Caso severo (+10 MW) | Límite | Estado |
|---|---|---|---|
| Tensión barra 23 kV | +3.8% | <= +5% | ✅ OK (margen estrecho) |
| Flujo línea distribuidora | 78% capacidad | <= 100% | ✅ OK |

---

## Coordinación de Protecciones — BESS agrega complejidad

El BESS puede inyectar corriente de falla **en horas sin sol**, lo que cambia el comportamiento de las protecciones:

| Situación | Sin BESS | Con BESS (descargando) |
|---|---|---|
| Falla en red a las 22:00 | Icc solo desde red | Icc red + aporte BESS (~0.3 kA) |
| Antipasivación (anti-isla) | Detecta fácilmente | Más difícil detectar isla con BESS |

**Acción requerida:**
- Relé antipasivación debe configurarse para detectar isla con BESS activo (tensión y frecuencia estables con BESS inyectando)
- Esquema: protección de isla por desplazamiento de impedancia o ROCOF + df/dt reforzado

---

## Bloques Horarios de Inyección BESS (Nueva Normativa CNE feb-2026)

La nueva normativa introduce bloques horarios para coordinar la inyección de BESS con la red:

| Bloque horario | Modo recomendado BESS |
|---|---|
| 00:00 – 06:00 | Descarga permitida (demanda baja: gestión de red) |
| 06:00 – 12:00 | Carga (aprovechando generación solar temprana) |
| 12:00 – 16:00 | Carga o stand-by (exceso solar → limitar inyección) |
| 16:00 – 22:00 | **Descarga** (punta de demanda — máximo valor) |
| 22:00 – 00:00 | Stand-by o descarga moderada |

> 📌 El despacho específico debe coordinarse con la distribuidora y puede variar según congestiones locales.

---

## Tabla de Brechas Pre-Entrada en Operación

| ID | Brecha | Criticidad | Acción | Plazo |
|---|---|---|---|---|
| B01 | Variables SITR para BESS sin confirmar con CEN | 🔴 Alta | Solicitar lista de puntos al CEN antes del comisionamiento | 30 días antes de entrada |
| B02 | S/E Maipo Norte en límite 20 MW — verificar PMUS | 🟠 Media | Confirmar con Coordinador si aplica PMU | 45 días antes de entrada |
| B03 | Relé antipasivación sin configuración BESS | 🔴 Alta | Ajustar relé para detección de isla con BESS activo | 60 días antes de entrada |
| B04 | Acuerdo SITR con Enel Distribución no firmado | 🔴 Alta | Iniciar gestión con distribuidora (plazo ~30-60 días) | Inmediato |
| B05 | Bloques horarios BESS no coordinados con distribuidora | 🟠 Media | Definir programa de despacho BESS con Enel | 30 días antes de entrada |

---

## Checklist Pre-Comisionamiento PMGD+BESS

```markdown
- [ ] Acuerdo SITR firmado con distribuidora
- [ ] Variables SITR (solar + BESS) confirmadas con CEN
- [ ] RTU configurado con todos los puntos acordados
- [ ] Disponibilidad SITR 48 h en pruebas >= 99.5%
- [ ] Relé antipasivación ajustado para BESS activo
- [ ] Relé diferencial transformador instalado y probado
- [ ] Bloques horarios BESS coordinados con distribuidora
- [ ] Consulta CEN sobre PMUS respondida y gestionada
- [ ] Diagrama unifilar as-built aprobado y en sala
- [ ] Manual de operación BESS disponible en sala de control
```

---

## Propuesta de Valor CONECTA para este Caso

**Servicio:** Diagnóstico pre-comisionamiento PMGD+BESS  
**Entregable:** Checklist técnica-normativa + plan de cierre de brechas  
**Tiempo:** 3 semanas  
**Por qué es crítico:** La nueva norm. CNE feb-2026 es desconocida para muchos proyectistas; un error en el relé antipasivación puede bloquear la entrada en operación del proyecto.
