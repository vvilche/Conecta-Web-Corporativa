---
name: evaluating-sscc-compliance
description: Evalúa cumplimiento normativo CEN para prestadores de Servicios Complementarios (SSCC). Usar cuando el usuario mencione "servicios complementarios", "SSCC", "AGC", "regulación de frecuencia", "control automático de generación" o "prestador SSCC".
---

# Skill: Cumplimiento CEN — Servicios Complementarios (SSCC)

## Cuándo usar este skill
- Coordinado es prestador de servicios complementarios al SEN
- Se revisan obligaciones de telemetría y control para AGC
- Se evalúa estado de plataforma y enlaces para regulación de frecuencia
- Se audita capacidad de comunicación en tiempo real para SSCC específicos

## Workflow

```markdown
- [ ] Identificar SSCC prestados (regulación primaria, secundaria, terciaria, SSCC técnicos)
- [ ] Verificar cumplimiento SITR base (ver skill_base_sitr)
- [ ] Definir variables en tiempo real requeridas por el Coordinador para cada SSCC
- [ ] Verificar protocolos AGC implementados (canal y plataforma)
- [ ] Verificar redundancia de plataforma y enlaces para AGC
- [ ] Verificar parámetros de control (estatismo, rampa, límites) disponibles en tiempo real
- [ ] Evaluar latencia de señales de control AGC
- [ ] Identificar brechas y plan de acción
```

## Instrucciones

### 1. Tipos de SSCC y Requerimientos de Telemetría

| Tipo de SSCC | Variables requeridas típicas | Control requerido |
|---|---|---|
| Regulación primaria de frecuencia | Potencia activa, frecuencia local, estatismo | Automático (governor/DVR) |
| Regulación secundaria (AGC) | Potencia activa, Set Point, ACE, estado unidades | Señal AGC del Coordinador |
| Regulación de tensión (Q) | Potencia reactiva, tensión, límites Q | Automático (AVR/condensador) |
| Banda negra | Estado, disponibilidad, potencia | Confirmación operativa |
| Servicio de arranque | Estado de disponibilidad | Confirmación operativa |

### 2. Requisitos AGC (Regulación Secundaria)

| Parámetro | Requisito | Fuente |
|---|---|---|
| Protocolo AGC | Definido por el Coordinador caso a caso | NTSyCS mar-2025 |
| Canal de comunicación | Redundante (primario + respaldo) | NTSyCS mar-2025 |
| Plataforma AGC | Redundante; sin punto único de falla | SITR dic-2019 |
| Latencia señal AGC | Según especificación del Coordinador | AT-SITR-1 |
| Edad de datos | <= 2 s para variables de control AGC | AT-SITR-1 |
| Parámetros en SITR | Estatismo, límites, tasa de toma de carga | NTSyCS mar-2025 |

### 3. Parámetros de Control a Declarar ante el Coordinador

- Estatismo (%) del regulador de velocidad
- Banda muerta de frecuencia (Hz)
- Rampa máxima de carga/descarga (MW/min)
- Límites de potencia activa (Pmin, Pmax)
- Límites de potencia reactiva (Qmin, Qmax) si aplica regulación de tensión
- Tiempo de respuesta al escalón de regulación

### 4. Criterios de Calidad de la Señal de Control
- Señal AGC no puede interrumpirse por más tiempo del definido por el Coordinador
- Si se pierde señal AGC: unidades deben pasar a modo "hold" o "droop" según instrucción
- Registrar eventos de pérdida de señal AGC para reporte al Coordinador

## Fuentes Autorizadas
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`
- SITR dic-2019: `documentos/fuentes/SITR-dic2019.pdf`
- AT-SITR-1 mar-2025: `documentos/fuentes/AT-SITR-1-mar2025.pdf`

## Checklists
- `documentos/checklists/checklist_sscc.md`
- `documentos/checklists_xlsx/checklist_sscc.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento SSCC/AGC con tabla de brechas
- Verificación de parámetros de control declarados al Coordinador
- Plan de acción con plazos y responsables
