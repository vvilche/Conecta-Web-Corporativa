---
name: conducting-field-inspection
description: Estructura y documenta visitas de levantamiento e inspección técnica en terreno para proyectos eléctricos. Usar cuando el usuario mencione "visita a terreno", "levantamiento en sitio", "inspección eléctrica", "auditoría de instalación" o "relevamiento de activos".
---

# Skill: Visita e Inspección en Terreno

## Cuándo usar este skill
- Usuario solicita preparar una visita técnica a instalación eléctrica
- Se necesita estructurar informe de levantamiento en terreno
- Se requiere checklist de inspección para auditoría o diagnóstico
- Usuario describe hallazgos de terreno y necesita documentarlos

## Workflow

```markdown
- [ ] Definir objetivo de la visita (levantamiento, diagnóstico, auditoría, comisionamiento)
- [ ] Preparar checklist y documentación previa
- [ ] Ejecutar la visita (o documentar datos entregados por el usuario)
- [ ] Registrar hallazgos, fotos y mediciones
- [ ] Clasificar observaciones (crítico, mayor, menor, oportunidad)
- [ ] Redactar informe de terreno
- [ ] Proponer plan de acción
```

## Instrucciones

### 1. Preparación Previa a la Visita

Documentación a revisar antes de ir:
- [ ] Planos vigentes (as-built si existen)
- [ ] Historial de fallas o mantenimientos previos
- [ ] Normativa aplicable al tipo de instalación
- [ ] EPP requerido (casco, guantes dieléctricos, calzado, lentes)
- [ ] Plan de seguridad y permisos de trabajo (LOTO, PTT)
- [ ] Equipos de medición necesarios (multímetro, pinzas amperimétricas, telurómeto, cámara termográfica)

### 2. Checklist de Inspección Visual

**Tableros y celdas:**
- [ ] Estado físico de la caja (golpes, corrosión, sellos)
- [ ] Identificación de circuitos completa y legible
- [ ] Conductores ordenados, identificados y sin daño visible
- [ ] Bornes apretados (sin signos de arco o calentamiento)
- [ ] Protecciones correctamente calibradas (verificar etiquetas de ajuste)
- [ ] Espacio libre para operación y mantenimiento
- [ ] Extintor accesible y vigente

**Conductores y canalizaciones:**
- [ ] Cables sin daño mecánico visible
- [ ] Bandejas con tapa y sin sobrecarga (regla: max 40% lleno para BT)
- [ ] Ductos y conduits sin rotura ni ingreso de agua
- [ ] Separación entre circuitos de potencia y control

**Equipos de potencia:**
- [ ] Transformadores: nivel de aceite, temperatura, signos de fuga, ruido anormal
- [ ] Interruptores: operación local/remota, estado de señalización
- [ ] Motores: vibración, temperatura, rodamientos, acoplamiento
- [ ] Equipos de compensación reactiva: ventilación, temperatura

**Sistema de tierra:**
- [ ] Conductor de tierra visible y continuo
- [ ] Electrodos de tierra identificados y accesibles
- [ ] Medición de resistencia de tierra (registrar valor y condiciones)
- [ ] Uniones equipotenciales en equipos metálicos

**Comunicaciones y SITR (si aplica CEN):**
- [ ] Enlace de comunicación operativo
- [ ] GPS sincronizado
- [ ] Disponibilidad de telemetría

### 3. Registro de Mediciones

| Punto | Tipo de Medición | Valor Medido | Límite Normativo | Estado |
|---|---|---|---|---|
| Barra BT | Tensión L-L | — V | — V | ✅/⚠️/❌ |
| Tablero principal | Corriente L1/L2/L3 | — A | — A | ✅/⚠️/❌ |
| Electrodo tierra | Resistencia | — Ω | ≤ 25 Ω (NCh Elec 4) | ✅/⚠️/❌ |
| Motor bomba | Temperatura carcasa | — °C | ≤ clase_motor °C | ✅/⚠️/❌ |

### 4. Clasificación de Observaciones

| Categoría | Criterio | Plazo de acción sugerido |
|---|---|---|
| 🔴 **Crítico** | Riesgo inmediato para personas o equipos | Inmediato (horas/días) |
| 🟠 **Mayor** | Incumplimiento normativo o riesgo latente | Corto plazo (semanas) |
| 🟡 **Menor** | Desviación leve o buena práctica no aplicada | Mediano plazo (meses) |
| 🟢 **Oportunidad** | Mejora opcional para eficiencia o confiabilidad | Largo plazo / mejora continua |

### 5. Estructura del Informe de Terreno

```
1. Datos de la visita (fecha, lugar, asistentes, objetivo)
2. Descripción general de la instalación
3. Resumen ejecutivo de hallazgos
4. Detalle de observaciones por área
5. Tabla de observaciones con clasificación y recomendaciones
6. Mediciones tomadas en terreno
7. Evidencia fotográfica (con referencia en texto)
8. Plan de acción propuesto
9. Conclusiones
```

### 6. Plantilla de Observación Individual

```markdown
**OBS-001**
- Área: Tablero General BT
- Descripción: Interruptor Q15 sin etiqueta de identificación de circuito
- Evidencia: Foto 012
- Categoría: 🟡 Menor
- Normativa: NCh Elec 4, Sección 5.3
- Recomendación: Etiquetar según nomenclatura del diagrama unifilar
- Responsable sugerido: Mantenimiento eléctrico
- Plazo sugerido: 30 días
```

## Salidas Esperadas
- Informe de inspección con estructura formal
- Tabla de observaciones priorizadas por categoría
- Plan de acción con responsables y plazos
- Registro fotográfico referenciado en texto
