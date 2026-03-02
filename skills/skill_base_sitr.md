---
name: evaluating-sitr-compliance
description: Evalúa y diagnostica el cumplimiento SITR para cualquier coordinado del SEN. Usar cuando el usuario mencione "SITR", "telemetría en tiempo real", "enlaces al Coordinador", "disponibilidad SITR", "AT-SITR-1" o "cumplimiento comunicaciones CEN".
---

# Skill: Cumplimiento SITR — Todos los Coordinados

## Cuándo usar este skill
- Usuario consulta sobre obligaciones SITR de cualquier coordinado
- Se necesita diagnosticar estado de cumplimiento de telemetría
- Se requiere identificar brechas en enlaces, calidad o disponibilidad
- Usuario menciona requisitos de comunicaciones con el CEN

## Workflow

```markdown
- [ ] Identificar tipo de coordinado (generación, transmisión, distribución, PMGD, SSCC)
- [ ] Levantar inventario de enlaces y protocolos actuales
- [ ] Verificar disponibilidad mensual (>= 99.5%) con reportes
- [ ] Verificar sincronización GPS (+/- 100 µs)
- [ ] Verificar edad de datos (<= 5 s, 2 s para AGC)
- [ ] Verificar muestreo y precisión de variables
- [ ] Verificar respaldo de alimentación (>= 6 h)
- [ ] Verificar grabación de voz operativa (>= 6 meses retención)
- [ ] Identificar brechas y clasificar criticidad
- [ ] Generar plan de remediación con plazos
```

## Instrucciones

### 1. Requisitos Mínimos SITR (Aplicables a Todos los Coordinados)

| Parámetro | Requisito | Fuente |
|---|---|---|
| Disponibilidad mensual | >= 99.5% (ventana 12 meses) | SITR dic-2019; AT-SITR-1 |
| Disponibilidad voz | >= 99.5% | NTSyCS mar-2025 |
| Sincronización GPS | +/- 100 µs; marcas >= 1 ms | SITR dic-2019 |
| Edad de datos | <= 5 s (2 s para AGC) | AT-SITR-1 |
| Muestreo analógico | <= 2 s | SITR dic-2019 |
| Precisión | Clase 2 ANSI o mejor | AT-SITR-1 |
| Precisión frecuencia | < 0.003% | SITR dic-2019 |
| Respaldo alimentación | >= 6 horas | AT-SITR-1 |
| Retención grabación voz | >= 6 meses + sync +/- 1 s | NTSyCS mar-2025 |

### 2. Protocolos de Comunicación Permitidos
- ICCP (TASE.2)
- DNP3 TCP/IP
- IEC 60870-5-104
- Protocolo debe estar acordado formalmente con el Coordinador

### 3. Calidad de Datos — Reglas
- Dato inválido si supera límites configurados O queda desactualizado > 30 s
- Dato con origen, validez y estampa de tiempo obligatoria
- Corrección de mala calidad: <= 8 h acción, <= 2 días informe, <= 5 días plan si afecta estimador EMS

### 4. Plazos Operativos Clave

| Evento | Plazo |
|---|---|
| Cierre de pruebas de integración | Coordinador notifica en <= 5 días |
| Aviso por modificación de enlace | >= 20 días antes |
| Aviso acuerdo entre coordinados | >= 30 días + notificación SEC |
| Implementación de nuevas exigencias | <= 12 meses desde publicación D.O. |

### 5. Diagnóstico de Brechas — Tabla de Salida

```markdown
| ID | Requisito | Estado actual | Brecha | Criticidad | Plazo sugerido |
|----|-----------|--------------|--------|------------|----------------|
| S01 | Disponibilidad >= 99.5% | 98.2% | -1.3% | 🔴 Alta | Inmediato |
| S02 | GPS +/- 100 µs | No configurado | Total | 🔴 Alta | 30 días |
| S03 | Respaldo 6 h | 4 h disponibles | -2 h | 🟠 Media | 60 días |
```

## Errores Comunes

- ❌ **Medir disponibilidad solo el mes puntual** — el requisito es 99.5% en ventana de 12 meses, no mensual
- ❌ **Confundir GPS del SITR con GPS del PMU** — son dos sincronizaciones independientes; ambas deben cumplir sus propios requisitos
- ❌ **No documentar el protocolo acordado** — el protocolo (ICCP, DNP3, IEC 104) debe estar acordado formalmente con el Coordinador, no solo configurado
- ❌ **Reportar corrección de mala calidad solo al cerrar** — el plazo de 8 h es para la corrección; el informe es dentro de 2 días; son plazos distintos
- ❌ **Olvidar avisar al Coordinador antes de modificar enlaces** — el plazo es >= 20 días de anticipación; hacerlo sin aviso es incumplimiento

## Ejemplo Real
- [Central Solar Los Llanos 50 MW](examples/example_sitr.md) — brecha de disponibilidad 97.8% y respaldo insuficiente

## Fuentes Autorizadas
- SITR dic-2019: `documentos/fuentes/SITR-dic2019.pdf`
- AT-SITR-1 mar-2025: `documentos/fuentes/AT-SITR-1-mar2025.pdf`
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`

## Checklists
- `documentos/checklists/checklist_todos_coordinados.md`
- `documentos/checklists_xlsx/checklist_todos_coordinados.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento SITR con tabla de brechas priorizadas
- Plan de remediación con plazos y responsables sugeridos
