# Norma Técnica de Conexión y Operación de PMGD — Feb 2026

## Metadatos
- **Institución**: Comisión Nacional de Energía (CNE)
- **Resolución**: RE CNE N°69 — publicada Diario Oficial 19 feb 2026
- **Vigencia**: Desde publicación en D.O.
- **PDF oficial**: [Descargar NTCO-PMGD-2026](https://www.cne.cl/wp-content/uploads/2026/02/2026.02.19_NTCO-PMGD-2026.pdf)
- **Resolución exenta**: [RE N°69](https://www.cne.cl/wp-content/uploads/2026/02/2026.02.19_RE_CNE_69_DO.pdf)
- **PDF local**: `../pdfs/CNE_NTCO_PMGD_2026.pdf`

## Alcance
Regula la **conexión y operación** de Pequeños Medios de Generación Distribuida (PMGD) conectados a redes de **Media Tensión (MT)** en el Sistema Eléctrico Nacional (SEN) del mercado Chileno.

> ⭐ **Novedad Feb 2026**: Primera norma que incorpora BESS (sistemas de almacenamiento en baterías) como categoría regulada explícita dentro de los PMGD.

## Definiciones clave
| Término | Definición |
|---|---|
| **PMGD** | Medio de generación ≤ 9 MW conectado a red de distribución MT |
| **BESS** | Battery Energy Storage System — almacenamiento electroquímico |
| **SITR** | Sistema de Información en Tiempo Real del CEN |
| **ECAP** | Estudio de Capacidad de Acogida y Perturbaciones |
| **COD** | Commercial Operation Date — fecha entrada operación comercial |
| **PMUS** | Plan de Medición con Unidades Sincrofasores |

## Clasificación normativa PMGD
- Potencia instalada nominal ≤ 9 MW
- Conexión en barra MT de red de distribución
- Propietario distinto de la distribuidora
- Puede ser solar FV, eólico, hidro de pasada, cogeneración, o BESS standalone/híbrido

### Umbral PMUS (20 MW)
Si la suma de PMGD en una misma S/E supera **20 MW acumulados**, todos los PMGD de esa S/E quedan obligados a instalar Unidades Sincrofasoras (PMU).

## Obligaciones SITR — Variables requeridas

### Solar FV estándar
| Variable | Unidad | Protocolo |
|---|---|---|
| Potencia activa neta | MW | ICCP / DNP3 / IEC104 |
| Potencia reactiva | MVAR | ICCP / DNP3 / IEC104 |
| Tensión barra conexión | kV | ICCP / DNP3 / IEC104 |
| Estado interruptor principal | Bool | ICCP / DNP3 / IEC104 |

### BESS adicionales (NUEVO — Feb 2026)
| Variable | Unidad | Estado norma |
|---|---|---|
| Potencia activa BESS | MW (+carga / −descarga) | ⚠️ A confirmar lista exacta con CEN |
| Estado de carga (SOC) | % | ⚠️ A confirmar con CEN |
| Estado BESS (cargando/descargando/espera) | Enum | ⚠️ A confirmar con CEN |
| Energía acumulada disponible | MWh | ⚠️ A confirmar con CEN |

**Disponibilidad mínima SITR requerida**: ≥ 99,5% medido en ventana de 48 h previas al COD.

## Bloques horarios de coordinación BESS (nuevo Feb 2026)

| Bloque | Modo recomendado | Razón |
|---|---|---|
| 00:00 – 06:00 | Descarga permitida | Demanda baja, gestión de red |
| 06:00 – 12:00 | Carga | Aprovechar generación solar temprana |
| 12:00 – 16:00 | Carga / stand-by | Exceso solar → limitar inyección |
| 16:00 – 22:00 | **Descarga — máximo valor** | Punta de demanda, precio alto |
| 22:00 – 00:00 | Stand-by / descarga moderada | Fin de punta |

El despacho específico debe coordinarse con la distribuidora antes del COD.

## Requisitos de protecciones con BESS
1. **Antipasivación reforzada**: BESS puede mantener tensión/frecuencia durante isla → relé estándar puede fallar. Requiere ROCOF + df/dt reforzado o protección de desplazamiento de impedancia.
2. **Diferencial de transformador**: obligatorio con BESS activo nocturno.
3. **Coordinación con protecciones de la distribuidora**: revisión obligatoria de selectividad.

## Proceso de conexión — Pasos clave
1. Solicitud formal a distribuidora + estudio de impacto (ECAP)
2. Aprobación técnica de distribuidora
3. Firma de Acuerdo SITR con CEN
4. Configuración RTU con variables SITR definidas
5. Pruebas de disponibilidad SITR ≥ 99,5% por 48 h
6. Autorización COD por la SEC

## Cambios respecto a versión anterior
- ✅ BESS como categoría regulada (antes no existía)
- ✅ Variables SITR específicas para almacenamiento
- ✅ Bloques horarios de coordinación BESS
- ✅ Antipasivación reforzada obligatoria con BESS
- ✅ SOC y estado de carga como señales SITR

## Referencias cruzadas
- [DS 244](../LEYES/DS_244_PMGD.md) — define qué es un PMGD
- [AT-SITR](./AT_SITR_2025.md) — especificaciones técnicas del sistema SITR
- [NTSyCS 2026](./NTSyCS_2026.md) — norma de seguridad y calidad de servicio
