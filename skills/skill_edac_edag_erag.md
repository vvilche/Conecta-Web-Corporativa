---
name: evaluating-edac-edag-erag-compliance
description: Evalúa cumplimiento normativo CEN para coordinados con esquemas EDAC, EDAG o ERAG. Usar cuando el usuario mencione "EDAC", "EDAG", "ERAG", "esquema de desconexión", "alivio de carga", "activación óptima de esquemas" o "auditoría EDAC".
---

# Skill: Cumplimiento CEN — EDAC / EDAG / ERAG

## Cuándo usar este skill
- Coordinado tiene esquemas EDAC, EDAG o ERAG configurados
- Se revisa cumplimiento de formalidades y activación óptima
- Se evalúa desempeño de esquemas ante eventos del SEN
- Se prepara para auditoría técnica del Coordinador

## Workflow

```markdown
- [ ] Identificar tipo de esquema: EDAC / EDAG / ERAG
- [ ] Verificar inventario de esquemas y parámetros vigentes declarados al CEN
- [ ] Verificar cumplimiento de formalidades y plazos con el Coordinador
- [ ] Revisar registros de eventos de activación con marcas de tiempo
- [ ] Evaluar desempeño: verificar % de actuación vs. valor esperado
- [ ] Verificar tiempo de operación (<= 200 ms)
- [ ] Verificar disponibilidad para auditoría técnica del Coordinador
- [ ] Identificar brechas y plan de acción
```

## Instrucciones

### 1. Diferencia entre Tipos de Esquema

| Tipo | Nombre completo | Función |
|---|---|---|
| EDAC | Esquema de Desconexión Automática de Cargas | Alivio de carga ante contingencias (frecuencia baja) |
| EDAG | Esquema de Desconexión Automática de Generación | Alivio de generación ante contingencias (sobrefrecuencia, islamiento) |
| ERAG | Esquema de Reconexión Automática de Generación | Reconexión controlada de generación post-evento |

### 2. Requisitos de Desempeño

| Criterio | Requisito | Calificación |
|---|---|---|
| Tiempo de operación | <= 200 ms desde inicio del evento | Obligatorio |
| Desempeño correcto | Desconexión/reconexión 80% – 120% del valor esperado | ✅ Correcto |
| Sobreactuación | > 120% del valor esperado | ⚠️ Observación |
| Desempeño deficiente | 20% – 80% del valor esperado | 🔴 Acción correctiva |
| Desempeño incorrecto | 0% – 20% del valor esperado | 🔴 Urgente |

### 3. Formalidades con el Coordinador

| Obligación | Plazo / Frecuencia | Fuente |
|---|---|---|
| Declarar parámetros del esquema | Antes de la operación / ante cambios | EDAC/EDAG/ERAG jun-2015 |
| Entregar datos y antecedentes | Según instrucción del Coordinador | EDAC/EDAG/ERAG jun-2015 |
| Facilitar auditoría técnica | Cuando el Coordinador lo requiera | EDAC/EDAG/ERAG jun-2015 |
| Reportar eventos de activación | Post-evento, con registro de tiempo | EDAC/EDAG/ERAG jun-2015 |
| Mantener configuraciones vigentes | Continuo; actualizar ante cambios | Estudio EDAC 2025 |

### 4. Información Mínima del Registro de Evento EDAC/EDAG/ERAG

Cada evento debe quedar registrado con:
- [ ] Fecha y hora de inicio (marca de tiempo GPS)
- [ ] Tipo de evento gatillante (baja frecuencia, sobretensión, etc.)
- [ ] Magnitud del evento (frecuencia mínima, tensión, potencia)
- [ ] Potencia/carga desconectada o reconectada (MW)
- [ ] Tiempo de operación del esquema (ms)
- [ ] Comparación con valor esperado (% desempeño)
- [ ] Estado final del sistema

### 5. Preparación para Auditoría Técnica CEN

Tener disponible:
- [ ] Configuraciones actuales de los esquemas (parámetros, umbrales, tiempos)
- [ ] Registros de eventos de los últimos 12 meses
- [ ] Registros de pruebas periódicas de los esquemas
- [ ] Actas de última calibración o verificación de equipos
- [ ] Documentación de cambios realizados al esquema

## Errores Comunes
- ❌ **Calcular el % de desempeño sobre la potencia instalada total** — debe calcularse sobre la potencia que el esquema *tenía programado* desconectar, no sobre la potencia instalada del coordinado
- ❌ **No reportar el evento al Coordinador** — aunque el esquema operó correctamente, el reporte post-evento es obligatorio; omitirlo es incumplimiento de formalidades
- ❌ **Medir el tiempo desde la alarma del SCADA** — el tiempo de operación se mide desde el inicio del evento gatillante (frecuencia cruzando umbral), no desde que el operador ve la alarma
- ❌ **Cambiar parámetros sin comunicar al CEN** — cualquier cambio en umbrales, tiempos o cargas del esquema debe declararse formalmente al Coordinador antes de implementarlo
- ❌ **No tener el registro de eventos con GPS** — sin marca de tiempo GPS, el Coordinador no puede validar el tiempo de operación; el dato queda impugnable

## Ejemplo Real
- [Central Hidro Río Claro — EDAC tiempo 430 ms](examples/example_edac.md)

## Fuentes Autorizadas
- EDAC/EDAG/ERAG jun-2015: `documentos/fuentes/EDAC-EDAG-ERAG-verificacion-2015.pdf`
- Estudio EDAC 2025: `documentos/fuentes/Estudio-EDAC-2025.pdf`

## Checklists
- `documentos/checklists/checklist_edac_edag_erag.md`
- `documentos/checklists_xlsx/checklist_edac_edag_erag.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento EDAC/EDAG/ERAG con tabla de desempeño histórico
- Estado de formalidades con el Coordinador
- Plan de preparación para auditoría técnica
