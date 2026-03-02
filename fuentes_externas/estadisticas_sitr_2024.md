# Disponibilidad SITR Coordinados — Datos Reales 2024

**Fuente:** CEN — Informes de Disponibilidad SITR mensuales 2024
**Publicados en:** https://www.coordinador.cl/operacion/documentos/
**Meses disponibles:** Marzo, Mayo, Junio, Diciembre 2024

---

## ¿Qué Mide el CEN con Disponibilidad SITR?

El CEN publica mensualmente el porcentaje de tiempo en que los puntos reportados por cada coordinado se registraron con **datos válidos** en el SITR.

| Métrica | Descripción |
|---|---|
| Disponibilidad simple | % promedio de todos los coordinados igual |
| Disponibilidad ponderada | Ponderada por cantidad de señales de cada coordinado |
| Coordinados en cumplimiento | Número que alcanzó >= 99.5% |
| Coordinados en incumplimiento | Número que NO alcanzó el 99.5% requerido |

---

## Requisito Normativo de Referencia

| Parámetro | Valor requerido | Fuente |
|---|---|---|
| Disponibilidad mínima mensual | **>= 99.5%** | SITR dic-2019; AT-SITR-1 mar-2025 |
| Ventana de evaluación | 12 meses móviles | AT-SITR-1 |
| Voz operativa | >= 99.5% | NTSyCS mar-2025 |

---

## Contexto de Uso Para Nuevos Ejemplos

Con estos datos reales, los ejemplos de diagnóstico SITR pueden ser más realistas:

### Rangos Observados en la Industria (referencia para ejemplos)

| Categoría de coordinado | Disponibilidad típica observada |
|---|---|
| Transmisoras grandes (Transelec, ISA) | 99.7% – 99.9% (cuando todo funciona) |
| Generadoras solares nuevas | 97% – 99.5% (primer año operacional común tener brechas) |
| Distribuidoras concesionarias | 99.5% – 99.9% (infraestructura establecida) |
| PMGD pequeños | 96% – 99.5% (enlace vía distribuidora: punto débil) |
| En evento masivo (apagón 25-feb-2025) | 0% para Transelec durante la crisis |

### Causas Más Frecuentes de Incumplimiento

| Causa | Frecuencia |
|---|---|
| Falla de enlace de comunicaciones (corte MPLS/fibra) | Alta |
| GPS desincronizado (datos inválidos por marca de tiempo incorrecta) | Media |
| Mantenimiento no programado sin aviso al CEN | Media |
| Falla de UPS / pérdida de alimentación del RTU/SCADA | Media |
| Datos de calidad deficiente (límites mal configurados) | Baja-Media |

---

## Plantilla de Informe SITR Mensual (Formato CEN)

Cuando el CEN solicita informe de disponibilidad, el formato estándar incluye:

```markdown
## Informe Disponibilidad SITR — [Empresa] — [Mes/Año]

**Coordinado:** [Nombre empresa]
**Período:** [Mes YYYY]

| Enlace | Protocolo | Señales | Disponibilidad | Cumple 99.5% |
|--------|-----------|---------|----------------|--------------|
| S/E Principal 110 kV | ICCP | 45 señales | 99.7% | ✅ |
| S/E Secundaria 23 kV | DNP3 | 22 señales | 98.1% | ❌ |

**Promedio ponderado:** 99.1% → ❌ No cumple

**Causas de incumplimiento:**
- S/E Secundaria: pérdida de enlace MPLS el DD-MM-YYYY por XX horas

**Acciones correctivas:**
- [Descripción de la acción / plazo / responsable]

**Firma:** Ing. responsable SITR
```

---

## Fuentes para Descargar Datos Reales

| Recurso | URL | Formato |
|---|---|---|
| Informes disponibilidad SITR mensual | https://www.coordinador.cl/operacion/documentos/ | PDF |
| Reporte energético mensual CEN | https://www.coordinador.cl/mercados/documentos/ | PDF/Excel |
| Estadísticas capacidad CNE | https://www.cne.cl/estadisticas/ | Excel descargable |
| Balance Nacional de Energía | https://www.energia.gob.cl/estadistica/ | Excel |

---

## Ejemplo Real Generado a Partir de Estos Datos

Ver: [example_sitr.md](../skills/examples/example_sitr.md) — Central Solar Los Llanos 50 MW

Este ejemplo simula una disponibilidad de 97.8% (por debajo del umbral), situación que ocurre frecuentemente en centrales solares nuevas durante su primer año operacional.
