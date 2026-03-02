# Norma Técnica de Seguridad y Calidad de Servicio (NTSyCS) — 2026

## Metadatos
- **Institución**: Comisión Nacional de Energía (CNE)
- **Resolución**: RE CNE N°45 — enero 2026
- **PDF oficial**: [Descargar NTSyCS 2026](https://www.cne.cl/wp-content/uploads/2026/02/2026.01.28_NTSyCS_RES45.pdf)
- **PDF local**: `../pdfs/CNE_NTSyCS_2026.pdf`

## Alcance
Establece los **estándares de seguridad y calidad de servicio** que deben cumplir todos los agentes del SEN: generadores, transmisores, distribuidores y grandes clientes. Es la norma "paraguas" que contiene los anexos técnicos (SITR, ECAP, protecciones, etc.).

## Estructura de la norma
```
NTSyCS
├── Cap. 1  Definiciones y alcance
├── Cap. 2  Obligaciones de coordinados (SITR, disponibilidad)
├── Cap. 3  Calidad de frecuencia
├── Cap. 4  Calidad de tensión
├── Cap. 5  Protecciones y coordinación
├── Cap. 6  Control y automatización (AGC, SSCC)
├── Cap. 7  Auditorías técnicas (EDAC, EDAG, ERAG)
└── Anexos técnicos (AT-SITR, AT-ECAP, AT-Protecciones)
```

## Obligaciones clave para PMGD

### Calidad de frecuencia
- Operación continua en rango: **49,8 – 50,2 Hz**
- Desconexión automática si frecuencia < 47,5 Hz o > 52 Hz por más de 200 ms
- PMGD con BESS: capacidad de respuesta primaria de frecuencia obligatoria (nueva Feb 2026)

### Calidad de tensión en punto de conexión
- Tensión de conexión: debe mantenerse en **±5% de la tensión nominal** en operación normal
- Factor de potencia: PMGD > 5 MW deben operar en rango **0,95 inductivo – 0,95 capacitivo**

### Auditorías técnicas (EDAC)
- **EDAC**: Evaluación de Desempeño de Agentes Coordinados — audit anual obligatoria
- **Aplica a**: todos los PMGD conectados al SITR
- **Contenido**: revisión de señales SITR, protecciones, esquemas de control

## Cambios 2026 vs versión anterior
- ✅ Respuesta primaria de frecuencia obligatoria para PMGD con BESS
- ✅ Nuevas especificaciones de antipasivación
- ✅ Requisitos adicionales de ciberseguridad para SCADA/RTU

## Referencias cruzadas
- [AT-SITR 2025](./AT_SITR_2025.md) — especificaciones técnicas SITR
- [NTSSCC 2026](./NTSSCC_2026.md) — norma de servicios complementarios
- [NTCO PMGD 2026](./NTCO_PMGD_2026.md) — aplicación específica en PMGD
