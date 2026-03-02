---
name: reviewing-electrical-plans
description: Revisa planos eléctricos y diagramas unifilares contra normativa técnica y estándares de calidad. Usar cuando el usuario mencione "revisar plano", "diagrama unifilar", "plano eléctrico", "layout eléctrico" o "revisión de ingeniería".
---

# Skill: Revisión de Planos Eléctricos

## Cuándo usar este skill
- Usuario sube o describe un plano eléctrico para revisión
- Se necesita validar diagrama unifilar contra normativa
- Se requiere checklist de revisión de ingeniería
- Se pide detectar errores u omisiones en documentación técnica

## Workflow

```markdown
- [ ] Identificar tipo de plano (unifilar, layout, esquema de control, canalización)
- [ ] Verificar información mínima requerida en el plano
- [ ] Revisar simbología y nomenclatura (IEC/IEEE/NCh)
- [ ] Verificar consistencia técnica (tensiones, calibres, protecciones)
- [ ] Revisar cumplimiento normativo aplicable
- [ ] Generar lista de comentarios (RFI / punch list)
- [ ] Emitir estado de revisión (Aprobado / Aprobado con comentarios / Rechazado)
```

## Instrucciones

### 1. Información Mínima Requerida en Todo Plano
Verificar que el plano contenga:
- [ ] Título, número de plano, revisión y fecha
- [ ] Escala (si aplica) o "Sin escala"
- [ ] Firma(s) del proyectista y revisor
- [ ] Cuadro de revisiones
- [ ] Leyenda de simbología
- [ ] Notas generales
- [ ] Nombre del proyecto y propietario

### 2. Revisión de Diagrama Unifilar
Verificar:
- [ ] Tensiones nominales en cada barra claramente indicadas
- [ ] Potencia nominal de transformadores y secuencia de vector
- [ ] Calibres y tipo de conductores en cada rama
- [ ] Protecciones indicadas (interruptores, fusibles, relés) con ajustes o referencia
- [ ] Medidores y equipos de transformación de medida (TC, TP)
- [ ] Puesta a tierra del neutro y del sistema
- [ ] Identificación de barras principale y de emergencia/respaldo
- [ ] Fuentes de alimentación (normal + respaldo si aplica)
- [ ] Cargas identificadas (descripción, potencia, factor de potencia)

### 3. Revisión de Simbología
Verificar conformidad con:
- IEC 60617: Símbolos gráficos para diagramas
- NCh aplicables al tipo de instalación
- Estándar interno del cliente si está definido

Símbolos críticos a verificar:
| Equipo | Símbolo correcto |
|---|---|
| Interruptor automático | Cuadrado con línea de interrupción |
| Transformador | Dos círculos entrelazados |
| Fusible | Rectángulo con línea |
| Seccionador | Línea con abertura |
| Puesta a tierra | Tres líneas horizontales decrecientes |

### 4. Verificación de Coordinación de Protecciones
- [ ] Interruptor aguas abajo protege contra fallo de fusible aguas arriba
- [ ] Discriminación de protecciones (tiempo o corriente)
- [ ] Protección de mínima tensión cuando aplique
- [ ] Interlock entre fuentes de alimentación alternativas
- [ ] Relé de protección diferencial en transformadores ≥ 10 MVA

### 5. Revisión de Layout y Canalización
- [ ] Distancias de seguridad entre equipos (IEC, NCh, reglamento SEC)
- [ ] Acceso para operación y mantenimiento (MTBF considerations)
- [ ] Separación entre circuitos de potencia y control
- [ ] Rutas de cable indicadas y dimensionadas
- [ ] Protección mecánica de cables (bandejas, ductos, conduits)

### 6. Códigos de Estado de Revisión

| Código | Significado | Acción |
|---|---|---|
| **A** | Aprobado | Procede a construcción sin modificaciones |
| **B** | Aprobado con comentarios | Incorporar comentarios, no requiere re-revisión |
| **C** | Rechazado | Corregir y re-enviar para segunda revisión |
| **D** | Para información | No requiere aprobación formal |

### 7. Plantilla de Lista de Comentarios (RFI/Punch List)

```markdown
| N° | Plano | Sección | Observación | Categoría | Estado |
|----|-------|---------|-------------|-----------|--------|
| 001 | E-001 | Barra BT | Calibre de conductor no indicado | Técnico | Abierto |
| 002 | E-001 | General | Falta cuadro de revisiones | Documental | Abierto |
```

## Normativa Aplicable
- IEC 60617: Símbolos gráficos
- IEC 61439: Tableros de baja tensión
- NCh Elec 4/2003: Instalaciones de consumo en BT
- SEC: Resoluciones aplicables (instalaciones eléctricas Chile)
- NSEG aplicables según tipo de instalación

## Salidas Esperadas
- Lista de comentarios numerada y categorizada
- Estado de revisión del plano (A/B/C/D)
- Checklist de revisión completada con marcas
