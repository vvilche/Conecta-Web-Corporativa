# Norma Técnica de Calidad de Servicio de Distribución (NTCSD) — 2024

## Metadatos
- **Institución**: Comisión Nacional de Energía (CNE)
- **Resolución**: Res. Exen. N°210 — mayo 2024
- **PDF oficial**: [Descargar NTCSD 2024](https://www.cne.cl/wp-content/uploads/2024/05/NTCSDx2024-1.pdf)
- **PDF local**: `../pdfs/CNE_NTCSD_2024.pdf`

## Alcance
Establece los **indicadores de calidad de servicio** que deben cumplir las empresas distribuidoras en sus redes MT y BT. Relevante para PMGD porque define los límites de tensión en el punto de conexión y los indicadores de continuidad del suministro.

## Indicadores de calidad relevantes para PMGD

### Calidad de tensión en MT
| Indicador | Límite | Consecuencia |
|---|---|---|
| **Variación de tensión** | ±5% Vn en régimen permanente | PMGD que cause exceder este límite debe reducir potencia |
| **Flicker Pst** | ≤ 1,0 (95% del tiempo) | Aplica a arranques de motores en sitios industriales |
| **Flicker Plt** | ≤ 0,8 (95% del tiempo) | Perturbaciones lentas acumuladas |
| **THD tensión** | ≤ 5% | Distorsión armónica total |

### Continuidad del suministro
| Indicador | Descripción | Umbral |
|---|---|---|
| **SAIDI** | Sistema de Indisponibilidad Promedio | Define penalización de distribuidoras |
| **SAIFI** | Frecuencia de interrupción | Define penalización de distribuidoras |
| **CAIDI** | Duración promedio por interrupción | Calculado de SAIDI/SAIFI |

### Relación con PMGD
- **PMGD que cause deterioro de calidad** puede ser desconectado por la distribuidora
- **ECAP (Estudio ECAP)** evalúa el impacto del PMGD en los indicadores de la distribuidora antes de la conexión
- Con **BESS cargando en horas punta de baja tensión**, puede mejorar SAIDI local

## Medición y reporte
- Distribuidoras miden y reportan indicadores trimestralmente al CEN
- PMGD deben facilitar acceso a medidores de calidad en punto de conexión

## Referencias cruzadas
- [NTCO PMGD 2026](./NTCO_PMGD_2026.md) — conexión MT y estudio ECAP
- [DISTRIBUIDORAS — Enel requisitos](../DISTRIBUIDORAS/Enel_requisitos_conexion.md)
