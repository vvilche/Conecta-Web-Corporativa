---
name: evaluating-generation-compliance
description: Evalúa cumplimiento normativo CEN para coordinados de generación eléctrica. Usar cuando el usuario mencione "generación", "PMUS", "PMU", "EDAG", "ERAG", "coordinado generador" o "central generadora".
---

# Skill: Cumplimiento CEN — Generación

## Cuándo usar este skill
- Coordinado es una empresa de generación eléctrica
- Se revisan obligaciones SITR + PMUS/PMU para unidades >= 9 MW
- Se evalúa estado de EDAG/ERAG cuando aplique
- Se audita dossier PES o checklist anual PMUS

## Workflow

```markdown
- [ ] Confirmar tipo y potencia de unidades (>= 9 MW para PMUS)
- [ ] Verificar cumplimiento SITR base (ver skill_base_sitr)
- [ ] Verificar instalación de PMU por unidad >= 9 MW
- [ ] Verificar segundo enlace de comunicaciones desde PMU/PDC
- [ ] Revisar especificaciones PMU (M-Class, 50 muestras/s, IEEE C37.118, GPS/IRIG-B)
- [ ] Verificar alimentación respaldada >= 8 h y redundancia de tensión
- [ ] Verificar ancho de banda >= 120 kbps y cálculo presentado al CEN
- [ ] Revisar dossier PES completo
- [ ] Verificar checklist anual PMUS actualizada (plazo: 31 julio)
- [ ] Si aplica EDAG/ERAG: revisar formalidades, auditorías y desempeño
- [ ] Generar tabla de brechas y plan de acción
```

## Instrucciones

### 1. SITR para Generación
Aplica todo lo definido en `skill_base_sitr.md` + variables operativas en tiempo real específicas de generación.

### 2. Requisitos PMUS/PMU (Generación >= 9 MW)

| Parámetro | Requisito | Fuente |
|---|---|---|
| Clase PMU | M-Class | Estudio MMF 2025 |
| Tasa de muestreo | 50 muestras/s | Estudio MMF 2025 |
| Protocolo | IEEE C37.118 | Estudio MMF 2025 |
| Sincronización | GPS/IRIG-B, precisión 1 µs | Estudio MMF 2025 |
| Segundo enlace | Habilitado desde PMU/PDC Local | Estudio MMF 2025 |
| Alimentación | >= 8 horas respaldo + redundancia TP | Estudio MMF 2025 |
| Ancho de banda | >= 120 kbps (cálculo presentado) | Estudio MMF 2025 |
| Actualización estudio MMF | Máximo 31 de julio cada año | Estudio MMF 2025 |

### 3. Contenido del Dossier PES

El dossier PES debe incluir:
- [ ] Layout del sistema PMUS
- [ ] Diagrama de conexiones de medida
- [ ] Esquema de sincronización horaria
- [ ] Diagrama de comunicaciones (arquitectura)
- [ ] Esquema de alimentación y respaldo
- [ ] Manuales de equipos PMU/PDC
- [ ] Protocolo de pruebas y actas de comisionamiento

### 4. Criterios EDAG/ERAG (cuando aplique)

| Criterio | Requisito | Fuente |
|---|---|---|
| Tiempo de operación | <= 200 ms | EDAC/EDAG/ERAG jun-2015 |
| Desempeño correcto | 80% – 120% del valor esperado | EDAC/EDAG/ERAG jun-2015 |
| Sobreactuación | > 120% (observación) | EDAC/EDAG/ERAG jun-2015 |
| Desempeño deficiente | 20% – 80% (acción correctiva) | EDAC/EDAG/ERAG jun-2015 |
| Desempeño incorrecto | 0% – 20% (urgente) | EDAC/EDAG/ERAG jun-2015 |

### 5. Calendario de Obligaciones — Generación

| Frecuencia | Obligación |
|---|---|
| Mensual | Reporte disponibilidad SITR |
| Anual (31 jul) | Actualización estudio MMF y checklist PMUS |
| Anual | Revisión configuraciones PMU |
| Evento | Corrección calidad SITR (<= 8 h) |

## Errores Comunes

- ❌ **Instalar solo una PMU para toda la central** — si hay varias unidades >= 9 MW, el estudio MMF define los puntos exactos; revisar si aplica por unidad o por subestación
- ❌ **No actualizar el dossier PES ante cambios de equipos** — cualquier cambio de PMU, PDC, GPS o comunicaciones requiere actualización del PES
- ❌ **Olvidar la checklist PMUS anual** — plazo estricto: 31 de julio de cada año; su incumplimiento es brecha formal ante el CEN
- ❌ **No presentar el cálculo de ancho de banda al CEN** — no basta con tener >= 120 kbps disponibles; el cálculo debe presentarse formalmente
- ❌ **Confundir respaldo SITR (6 h) con respaldo PMUS (8 h)** — son requisitos distintos; la alimentación de la PMU debe tener >= 8 h

## Ejemplo Real
- [Central Solar 60 MW — Cumplimiento PMUS](examples/example_generacion.md)
- [Central Solar Los Llanos 50 MW — Con brechas](examples/example_sitr.md)

## Fuentes Autorizadas
- SITR dic-2019 y AT-SITR-1 mar-2025
- Estudio PMUS 2025: `documentos/fuentes/PMUS-Estudio-2025.pdf`
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`
- EDAC/EDAG/ERAG jun-2015 (si aplica)

## Checklists
- `documentos/checklists/checklist_generacion.md`
- `documentos/checklists_xlsx/checklist_generacion.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento generación (SITR + PMUS + EDAG/ERAG)
- Tabla de brechas por sistema con criticidad y plazo de remediación
