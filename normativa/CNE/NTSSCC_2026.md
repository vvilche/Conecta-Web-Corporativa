# Norma Técnica de Servicios Complementarios (NTSSCC) — 2026

## Metadatos
- **Institución**: Comisión Nacional de Energía (CNE)
- **Resolución**: RE CNE N°45 — enero 2026
- **PDF oficial**: [Descargar NTSSCC 2026](https://www.cne.cl/wp-content/uploads/2026/02/2026.01.28_NTSSCC_RES45.pdf)
- **PDF local**: `../pdfs/CNE_NTSSCC_2026.pdf`

## Alcance
Regula los **servicios complementarios** del SEN: regulación de frecuencia (AGC), servicios de tensión, y capacidades de partida autónoma. Con la entrada de BESS a gran escala, esta norma adquiere especial relevancia.

## Servicios Complementarios relevantes para PMGD+BESS

### AGC — Control Automático de Generación
- PMGD normalmente **exentos de AGC**
- BESS de gran escala (> 5 MWh) pueden ser requeridos para participar en regulación secundaria de frecuencia
- Señal AGC recibida via SCADA/SITR en tiempo real

### SSCC — Servicios de Tensión
- Control de tensión mediante Q (potencia reactiva)
- PMGD con inversor capaz de control Q deben participar si la distribuidora lo requiere
- Curva Q(V) definida por la norma

### EDAC/EDAG/ERAG — Evaluaciones de Desempeño
| Evaluación | Tipo | Periodicidad |
|---|---|---|
| **EDAC** | Agentes Coordinados (generadores) | Anual |
| **EDAG** | Desempeño en AGC | Semestral |
| **ERAG** | Regulación automática de generación | Anual |

## Implicancias para BESS en mercado Chileno
- BESS puede ofrecer **reserva de regulación primaria** → ingreso adicional en mercado de SSCCs
- **Arbitraje horario** + **servicios de frecuencia** = doble flujo de ingresos
- CEN puede requerir disponibilidad de reserva mínima (SOC mínimo) para BESS que participen en SSCCs

## Cambios 2026
- ✅ BESS incorporado como proveedor potencial de SSCCs
- ✅ Nueva metodología de verificación de desempeño en regulación de frecuencia
- ✅ Requisitos de ciberseguridad para sistemas de control de SSCCs

## Referencias cruzadas
- [NTSyCS 2026](./NTSyCS_2026.md) — norma madre de seguridad
- [NTCO PMGD 2026](./NTCO_PMGD_2026.md) — conexión PMGD
- [CEN — PMUS](../CEN/PMUS_MMF.md) — sincrofasores y medición
