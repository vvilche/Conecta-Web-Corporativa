# Anexo Técnico SITR — Sistema de Información en Tiempo Real

## Metadatos
- **Institución**: Comisión Nacional de Energía (CNE)
- **Documento**: Anexo Técnico SITR — versión marzo 2025
- **Norma madre**: NTSyCS (Norma Técnica de Seguridad y Calidad de Servicio)
- **PDF oficial**: [Descargar AT-SITR-2025](https://www.cne.cl/wp-content/uploads/2025/04/2025.03_AT-SITR-1.pdf)
- **PDF local**: `../pdfs/CNE_AT_SITR_2025.pdf`

## Alcance
Define los **parámetros técnicos y operativos** para el envío de datos desde instalaciones coordinadas al Sistema de Información en Tiempo Real (SITR) del Coordinador Eléctrico Nacional (CEN).

## Protocolos de comunicación aceptados
| Protocolo | Descripción | Uso recomendado |
|---|---|---|
| **ICCP (IEC-60870-6/TASE.2)** | Inter-Control Center Communications | Prioridad para LATs y grandes generadores |
| **DNP 3.0 TCP/IP** | Distributed Network Protocol | Estándar para PMGD |
| **IEC 60870-5-104** | Telecontrol equipments | Alternativa para PMGD |

## Parámetros de calidad de datos
| Parámetro | Requisito |
|---|---|
| **Tasa de refresco** | ≤ 4 segundos para señales analógicas |
| **Sincronización horaria** | GPS obligatorio (± 1 ms) |
| **Disponibilidad mínima** | ≥ 99,5% en ventana de 48 h |
| **Latencia máxima datos** | ≤ 10 segundos extremo a extremo |
| **Protocolo de backup** | Requerido si canal principal falla > 10 min |

## Variables mínimas por tipo de instalación

### PMGD Solar FV
```
P_neta        [MW]    Potencia activa neta en punto de conexión
Q_neta        [MVAR]  Potencia reactiva en punto de conexión
V_barra       [kV]    Tensión en barra MT de conexión
I_principal   [A]     Corriente en interruptor principal
Est_interr    [Bool]  Estado interruptor principal (0=abierto / 1=cerrado)
```

### PMGD BESS (nuevas variables — NTCO PMGD Feb 2026)
```
P_bess        [MW]    Potencia activa BESS (+carga / −descarga)
SOC           [%]     Estado de carga (0–100%)
Est_bess      [Enum]  Estado: 0=espera / 1=cargando / 2=descargando
E_disponible  [MWh]   Energía acumulada disponible para despacho
```
> ⚠️ Lista definitiva de señales BESS debe confirmarse con el CEN previo al comisionamiento.

## Proceso de integración SITR
1. **Solicitud al CEN**: formulario de lista de señales + tipo de RTU/ICCP
2. **Configuración**: RTU o servidor ICCP con señales definidas
3. **Prueba de conectividad**: verificar enlace de datos con sala de control CEN
4. **Prueba de disponibilidad**: 48 h continuas ≥ 99,5% de uptime
5. **Informe de prueba**: presentar a CNE/SEC como requisito previo COD

## Tipos de enlace aceptados
| Tipo | Carrier | Velocidad mínima |
|---|---|---|
| Fibra óptica | Xtera / propia | ≥ 1 Mbps |
| Radio enlace | UHF / microondas | ≥ 128 kbps |
| Internet privado (VPN) | MPLS / IPsec | ≥ 256 kbps |

## Errores comunes en integración SITR
1. **Señales con timestamps incorrectos**: falta de GPS o sincronización NTP incorrecta
2. **Unidades equivocadas**: MW vs kW — verificar escala en RTU
3. **Estado de interruptor invertido**: lógica 0/1 debe coincidir con definición del CEN
4. **Señales duplicadas**: un único punto de medición por variable

## Referencias cruzadas
- [NTCO PMGD 2026](./NTCO_PMGD_2026.md) — obligaciones SITR para PMGD+BESS
- [CEN — Instrucciones coordinador](../CEN/instructivo_sitr.md) — proceso de inscripción y pruebas
