---
name: evaluating-transmission-compliance
description: Evalúa cumplimiento normativo CEN para coordinados de transmisión eléctrica. Usar cuando el usuario mencione "transmisión", "STN", "empresa transmisora", "líneas de transmisión", "PDC", "MMF en transmisión" o "coordinado transmisor".
---

# Skill: Cumplimiento CEN — Transmisión

## Cuándo usar este skill
- Coordinado es una empresa de transmisión eléctrica (STN/STE/STR)
- Se revisan obligaciones SITR + PMUS/MMF en instalaciones de transmisión
- Se evalúa estado de EDAC/EDAG/ERAG cuando aplique
- Se audita integración con PDC local o corporativo

## Workflow

```markdown
- [ ] Identificar instalaciones STN/STE/STR del coordinado
- [ ] Verificar cumplimiento SITR base (ver skill_base_sitr)
- [ ] Verificar variables de red en tiempo real enviadas al SITR
- [ ] Revisar puntos PMU/MMF implementados según último estudio MMF
- [ ] Verificar integración con PDC local y/o corporativo
- [ ] Verificar disponibilidad y pruebas de enlaces PMU-PDC-CEN
- [ ] Si aplica EDAC/EDAG/ERAG: revisar formalidades, auditorías y desempeño
- [ ] Generar tabla de brechas y plan de acción
```

## Instrucciones

### 1. SITR para Transmisión
Aplica todo lo definido en `skill_base_sitr.md` + variables de red (tensiones de barra, flujos en líneas, estado de interruptores) en tiempo real.

### 2. PMUS/MMF en Transmisión (STN)

| Parámetro | Requisito | Fuente |
|---|---|---|
| Puntos de monitoreo | Definidos por estudio MMF vigente | Estudio MMF 2025 |
| Actualización estudio | Máximo 31 de julio cada año | Estudio MMF 2025 |
| Integración PDC | PDC Local conectado al PDC del CEN | Estudio MMF 2025 |
| Especificaciones PMU | Igual que generación (M-Class, 50 mps, C37.118, GPS) | Estudio MMF 2025 |
| Segundo enlace | Habilitado desde cada PMU/PDC Local | Estudio MMF 2025 |

### 3. Arquitectura PDC Requerida
- PMU(s) en subestaciones STN → PDC Local → PDC Corporativo → CEN SuperPDC
- Redundancia de enlace entre PDC Local y CEN
- Sincronización horaria GPS en cada PMU

### 4. Variables Mínimas en SITR — Transmisión

| Tipo de variable | Descripción |
|---|---|
| Tensión | Módulo y ángulo en barras principales |
| Potencia | Activa y reactiva por línea/transformador |
| Corriente | Por fase en barras principales |
| Estado | Posición de interruptores y seccionadores |
| Frecuencia | Si aplica (barras isladas o con generación local) |

### 5. Criterios EDAC/EDAG/ERAG (si aplica)
Ver tabla completa en `skill_generacion.md` — mismos criterios aplican para transmisión.

## Fuentes Autorizadas
- SITR dic-2019 y AT-SITR-1 mar-2025
- Estudio PMUS 2025: `documentos/fuentes/PMUS-Estudio-2025.pdf`
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`
- EDAC/EDAG/ERAG jun-2015 (si aplica)

## Checklists
- `documentos/checklists/checklist_transmision.md`
- `documentos/checklists_xlsx/checklist_transmision.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento transmisión (SITR + PMU/MMF + PDC)
- Tabla de brechas por instalación con criticidad y plazo de remediación
