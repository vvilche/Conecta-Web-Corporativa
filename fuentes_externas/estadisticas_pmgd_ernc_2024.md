# Estadísticas PMGD y ERNC Chile 2024-2025

**Fuentes:** CNE, Energía.gob.cl, CEN, PV Magazine Latam
**Fecha de referencia:** Febrero 2026

---

## Capacidad Instalada PMGD (Pequeños Medios de Generación Distribuida)

| Período | Capacidad Total PMGD | Solar | Eólico | Térmica | Hidro |
|---|---|---|---|---|---|
| Junio 2024 | **3.042 MW** | 82% (~2.494 MW) | 2% (~61 MW) | 10% (~304 MW) | 6% (~183 MW) |
| Diciembre 2025 | **~3.106 MW solar + 53 MW eólico** | 82%+ | 2%+ | — | — |
| Total PMG + PMGD 2025 | **4.127 MW** | — | — | — | — |

**Adiciones 1S2024:** 247 MW nuevos (99% solar)

---

## Contexto Regulatorio PMGD 2025-2026

| Evento | Fecha | Impacto |
|---|---|---|
| SEC: inmutabilidad costos de conexión PMGD | Jul-2024 | Certeza jurídica para nuevos proyectos |
| CNE: Nueva Norma Técnica de Conexión PMGD en MT | Feb-2026 | Nuevos criterios con BESS; procedimiento estandarizado |
| BESS instalado | A feb-2026 | ~1.700 MW operativos; 4.500 MW en construcción |
| Proyectos PMGD vigentes | Feb-2026 | >70 proyectos; varios con entrada operación mar-2026 |

---

## Proyectos ERNC en Construcción (Dic 2024)

| Dato | Valor |
|---|---|
| Proyectos en construcción | 271 proyectos |
| Fecha estimada entrada en operación | Hasta abril 2027 |
| Tecnología dominante | Solar FV + BESS (almacenamiento) |
| MW en construcción estimados | ~8.000 MW |

**A septiembre 2025:** 46 centrales (3.053 MW) en construcción activa

---

## Tendencias que Afectan Obligaciones Normativas de Coordinados

### 1. BESS — Nuevos Requisitos SITR (2025+)
Los sistemas de almacenamiento en baterías conectados como PMGD requieren:
- Variables SITR adicionales: Estado de carga (SOC), potencia activa/reactiva BESS
- Posible EDAG si el BESS puede actuar en eventos de sobrefrecuencia
- Nuevas variables de control para AGC si presta regulación de frecuencia

### 2. Solar Dominante → Impacto en EDAC
Con 30% de capacidad solar:
- En horas pico solar (mediodía), el sistema puede tener exceso → EDAG más relevante
- En horas nocturnas, la solar cae a 0 → EDAC más relevante
- Los esquemas EDAC/EDAG deben calibrarse para ambos escenarios

### 3. PMGD Pequeños → Punto Débil en SITR
- El 82% de los PMGD son solares con potencias de 1-9 MW
- Muchos usan enlace SITR vía distribuidora → dependencia del sistema de la distribuidora
- Mayor riesgo de incumplimiento de disponibilidad 99.5%

---

## Datos para Nuevos Ejemplos de Diagnóstico

### Caso Típico: PMGD Solar 5 MW nuevo en 2025

Características estadísticamente representativas:
```
- Tecnología: Solar FV + posiblemente BESS 1-2 MWh
- Punto conexión: Red MT 23 kV vía distribuidora local
- Enlace SITR: DNP3 TCP/IP vía sistema comunicaciones distribuidora
- Primer año operacional: Disponibilidad SITR esperada 97-99% (curva de aprendizaje)
- Obligaciones:
  * SITR: Sí (vía distribuidora)
  * PMUS: Solo si SS/EE concentra >20 MW PMGD
  * EDAC/EDAG: Ver si aplica por potencia y configuración
```

### Caso Típico: Central Solar 50 MW nueva

```
- Tecnología: Solar FV + BESS 20 MWh (tendencia 2025)
- Punto conexión: Barra 110 kV propia o S/E CEN
- PMUS: Definitivamente aplica (>= 9 MW)
- SITR directo al CEN
- Variables nuevas SITR: SOC del BESS, potencia BESS separada de solar
```

---

## Fuentes Verificables

| Fuente | URL | Disponibilidad |
|---|---|---|
| Estadísticas PMGD CNE | https://www.cne.cl/estadisticas/ | Pública, descargable |
| Reporte ERNC mensual | https://www.energia.gob.cl/tema/pequenos-medios-de-generacion-distribuida | Pública |
| PV Magazine Latam | https://pv-magazine-latam.com | Pública |
| Electrominería | https://electromineria.cl | Pública (análisis) |
