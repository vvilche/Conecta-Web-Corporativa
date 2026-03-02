---
name: generating-technical-report
description: Genera informes técnicos formales para proyectos de ingeniería eléctrica. Usar cuando el usuario mencione "informe técnico", "reporte de ingeniería", "documento formal", "entregable técnico", "informe al CEN", "informe a la SEC" o "informe de proyecto".
---

# Skill: Generación de Informe Técnico

## Cuándo usar este skill
- Usuario pide generar un informe técnico o entregable formal
- Se necesita estructurar resultados de análisis o estudios
- Se requiere documento para presentar al CEN, SEC, cliente o EPP
- Se necesita consolidar hallazgos de visitas, cálculos o estudios

## Workflow

```markdown
- [ ] Identificar tipo de informe y destinatario (CEN, SEC, cliente, interno)
- [ ] Definir alcance y estructura del informe
- [ ] Recopilar información de entrada (datos, cálculos, hallazgos)
- [ ] Redactar secciones siguiendo estructura formal
- [ ] Incluir tablas, figuras y referencias normativas
- [ ] Revisar consistencia interna y ortografía técnica
- [ ] Emitir informe con número, revisión y firmas
```

## Instrucciones

### 1. Tipos de Informe y Requisitos Específicos

| Tipo | Destinatario | Requisito clave |
|---|---|---|
| Informe ECAP | CEN | Basado en simulaciones; firma de ingeniero competente |
| Memoria de cálculo | SEC / cliente | Trazable a normativa NCh/IEC; firmada |
| Informe de inspección | Cliente / interno | Evidencia fotográfica; tabla de observaciones |
| Informe de avance | Cliente | Hitos, estado de actividades, curva S |
| Informe de comisionamiento | CEN / cliente | Protocolos de prueba y actas de aceptación |
| Informe normativo CEN | CEN | Trazabilidad a procedimientos y guías técnicas CEN |

### 2. Estructura Base (Aplicable a Todo Informe)

```
[PORTADA]
- Logo CONECTA
- Título del informe
- Proyecto
- Cliente / Destinatario
- N° de informe: [CON-ING-YYYY-NNN]
- Revisión: [Rev. 0 / Rev. A / Rev. 1]
- Fecha de emisión
- Preparado por / Revisado por / Aprobado por

[CONTROL DE REVISIONES]
| Rev. | Fecha | Descripción | Elaborado | Revisado | Aprobado |
|------|-------|-------------|-----------|----------|----------|
| 0    | YYYY-MM-DD | Emisión inicial | XX | YY | ZZ |

[TABLA DE CONTENIDOS]

1. Resumen ejecutivo
2. Introducción
   2.1 Antecedentes
   2.2 Objetivo del informe
   2.3 Alcance
3. Normativa y referencias
4. Descripción del sistema / instalación
5. Desarrollo técnico (cálculos, análisis, hallazgos)
6. Resultados y discusión
7. Conclusiones
8. Recomendaciones
9. Referencias bibliográficas
10. Anexos
```

### 3. Resumen Ejecutivo (Guía de Redacción)
- Máximo 1 página
- Incluir: contexto (1-2 oraciones), objetivo (1 oración), resultado principal (2-3 oraciones), conclusión/recomendación clave (1-2 oraciones)
- Sin tecnicismos excesivos; legible para nivel gerencial

**Plantilla:**
```
El presente informe analiza [tema] en el contexto de [proyecto/instalación].
El objetivo es [objetivo específico].
Los resultados indican que [hallazgo principal].
Se concluye que [conclusión] y se recomienda [acción].
```

### 4. Sección de Normativa y Referencias

Formato estándar de citación:
```markdown
## Normativa Aplicable
- [COD-01] IEC 60909:2016 — Short-circuit currents in three-phase AC systems
- [COD-02] NCh Elec 4/2003 — Instalaciones de consumo en baja tensión
- [COD-03] NTSyCS Mar-2025 — Norma Técnica de Seguridad y Calidad de Servicio
- [COD-04] AT-SITR-1 Mar-2025 — Especificaciones técnicas SITR

Referencia en texto: "...según [COD-01], la corriente de cortocircuito..."
```

### 5. Numeración y Control de Documentos

**Nomenclatura de informe CONECTA:**
```
CON-[ÁREA]-[AÑO]-[NNN]-[TIPO]

Ejemplos:
CON-ING-2025-001-MEM  → Memoria de cálculo N°001, 2025
CON-ING-2025-002-INF  → Informe técnico N°002, 2025
CON-ING-2025-003-ECK  → Checklist N°003, 2025
CON-CEN-2025-001-INF  → Informe al CEN N°001, 2025
```

**Revisiones:**
- Rev. 0 o Rev. A: Borrador para revisión
- Rev. 1: Primera emisión oficial
- Rev. 2, Rev. 3...: Revisiones posteriores con cambios

### 6. Buenas Prácticas de Redacción Técnica
- Usar voz activa: "El análisis muestra..." no "Se muestra por el análisis..."
- Ser preciso con unidades: siempre indicar la unidad (kV, kA, MW, %)
- Cada afirmación técnica → citar fuente o referencia
- Tablas y figuras → numeradas y con título descriptivo
- Abreviaciones → definir en primera mención: "Sistema de Información en Tiempo Real (SITR)"
- Evitar ambigüedad: en lugar de "valores altos" → usar "valores superiores a X kA"

### 7. Lista de Verificación Final

```markdown
- [ ] Portada completa (título, número, fecha, revisión, firmas)
- [ ] Cuadro de revisiones actualizado
- [ ] Resumen ejecutivo ≤ 1 página
- [ ] Todas las tablas numeradas y con título
- [ ] Todas las figuras numeradas y con pie de figura
- [ ] Referencias normativas citadas en el texto
- [ ] Unidades indicadas en todas las magnitudes
- [ ] Consistencia de datos entre secciones
- [ ] Conclusiones responden al objetivo del informe
- [ ] Sin errores de ortografía ni redacción
```

## Salidas Esperadas
- Informe técnico con numeración y control de revisiones
- Resumen ejecutivo conciso
- Secciones técnicas completas y trazables a normativa
