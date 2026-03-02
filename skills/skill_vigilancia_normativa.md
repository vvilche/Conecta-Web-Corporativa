---
name: monitoring-regulatory-changes
description: Monitorea y gestiona cambios normativos del CEN, SEC y CNE que afectan a coordinados. Usar cuando el usuario mencione "nueva normativa", "actualización CEN", "cambio normativo", "vigilancia regulatoria", "alerta CEN" o "qué cambió en la normativa".
---

# Skill: Vigilancia Normativa CEN/SEC/CNE

## Cuándo usar este skill
- Usuario pregunta sobre actualizaciones normativas recientes
- Se necesita revisar si alguna normativa del catálogo ha cambiado
- Se configura el proceso periódico de vigilancia normativa
- Se recibe una resolución o circular nueva del CEN/SEC/CNE

## Workflow

```markdown
- [ ] Identificar fuentes a revisar (CEN, SEC, CNE, Diario Oficial)
- [ ] Revisar URLs oficiales por nuevas publicaciones
- [ ] Comparar versiones: nueva vs. versión en catálogo local
- [ ] Evaluar impacto en coordinados (SITR, PMUS, EDAC, SSCC)
- [ ] Actualizar catálogo normativo local (indice_maestro.md)
- [ ] Identificar obligaciones afectadas y plazos de implementación
- [ ] Notificar internamente y generar plan de adecuación
```

## Instrucciones

### 1. Fuentes Oficiales a Revisar (en orden de prioridad)

| Fuente | URL | Frecuencia sugerida |
|---|---|---|
| CEN — Operación | https://www.coordinador.cl/operacion/documentos/ | Semanal |
| CEN — Planificación | https://www.coordinador.cl/desarrollo/documentos/ | Semanal |
| CEN — Procedimientos internos | https://www.coordinador.cl/procedimientos-internos/ | Mensual |
| CEN — Guías técnicas | https://www.coordinador.cl/guias-tecnicas/ | Mensual |
| CEN — Marco normativo | https://www.coordinador.cl/transparencia/marco-normativo/ | Mensual |
| CNE — Normativa | https://www.cne.cl/normativa/ | Mensual |
| SEC — Normativa | https://www.sec.cl/sitenormativa/ | Mensual |
| Diario Oficial | https://www.diariooficial.interior.gob.cl/ | Semanal |

### 2. Catálogo de Documentos Bajo Vigilancia

| Documento | Versión actual | Fecha | Archivo local |
|---|---|---|---|
| NTSyCS | Mar-2025 | 2025-03 | `documentos/fuentes/NTSyCS-Mar-2025.pdf` |
| AT-SITR-1 | Mar-2025 | 2025-03 | `documentos/fuentes/AT-SITR-1-mar2025.pdf` |
| SITR | Dic-2019 | 2019-12 | `documentos/fuentes/SITR-dic2019.pdf` |
| Estudio MMF/PMUS | 2025 | 2025-07 | `documentos/fuentes/PMUS-Estudio-2025.pdf` |
| Estudio EDAC | 2025 | 2025-07 | `documentos/fuentes/Estudio-EDAC-2025.pdf` |
| EDAC/EDAG/ERAG verificación | Jun-2015 | 2015-06 | `documentos/fuentes/EDAC-EDAG-ERAG-verificacion-2015.pdf` |

### 3. Proceso de Evaluación de Cambio

Al detectar un documento nuevo o actualizado:

**Paso 1 — Verificar si es relevante para coordinados:**
- ¿Menciona coordinados, empresas coordinadas o agentes del SEN?
- ¿Modifica algún documento del catálogo bajo vigilancia?
- ¿Establece nuevas obligaciones, plazos o evidencias?

**Paso 2 — Clasificar el impacto:**
| Nivel | Criterio | Acción |
|---|---|---|
| 🔴 **Crítico** | Nueva obligación con plazo < 3 meses | Alerta inmediata + plan urgente |
| 🟠 **Alto** | Nueva obligación con plazo 3–12 meses | Alerta + planificación |
| 🟡 **Medio** | Cambio de parámetros o procedimientos | Revisar en siguiente ciclo |
| 🟢 **Informativo** | Guía o consulta sin impacto inmediato | Registrar y archivar |

**Paso 3 — Identificar coordinados afectados:**
Marcar qué tipos de coordinado se ven impactados:
- [ ] Generación
- [ ] Transmisión
- [ ] Distribución
- [ ] PMGD/PMG
- [ ] SSCC
- [ ] Coordinados con EDAC/EDAG/ERAG

**Paso 4 — Actualizar catálogo local:**
- Actualizar `documentos/indice_maestro.md` con nueva versión
- Descargar nuevo PDF a `documentos/fuentes/`
- Actualizar skill correspondiente si cambian parámetros o requisitos
- Registrar cambio en `documentos/catalogo_normativo_cen.md`

### 4. Calendario de Vigilancia Recomendado

| Frecuencia | Acción |
|---|---|
| **Semanal** | Revisar portales CEN y Diario Oficial |
| **Mensual** | Revisar SEC y CNE; comparar versiones del catálogo |
| **Trimestral** | Revisión profunda de todas las fuentes + actualización de skills |
| **Anual (julio)** | Especial: revisar Estudio MMF/PMUS (plazo 31 julio) |

### 5. Plantilla de Alerta Normativa

```markdown
## ALERTA NORMATIVA — [Fecha]

**Documento:** [Nombre del documento]
**Versión nueva:** [X.X / fecha] → reemplaza a [versión anterior]
**Publicado en:** [Fuente URL]
**Fecha de publicación:** [YYYY-MM-DD]
**Plazo de implementación:** [<= 12 meses desde publicación en D.O. / fecha específica]

**Impacto en coordinados:**
- Tipo(s) afectado(s): [Generación / Transmisión / ...]
- Obligaciones nuevas o modificadas: [descripción]
- Parámetros que cambian: [detallar]

**Skill(s) a actualizar:** [skill_base_sitr / ...]
**Acción requerida:** [descarga, análisis, plan de adecuación]
**Responsable:** [nombre]
```

## Errores Comunes
- ❌ Asumir que la versión local es la vigente sin revisarla contra la fuente oficial
- ❌ No registrar la fecha de consulta de las fuentes
- ❌ Olvidar el plazo de implementación: AT-SITR-1 establece que nuevas exigencias del D.O. deben implementarse en <= 12 meses

## Fuentes
- `documentos/indice_maestro.md` — Catálogo local
- `documentos/catalogo_normativo_cen.md` — Registro de versiones

## Salida Esperada
- Informe de vigilancia normativa con cambios detectados
- Alertas clasificadas por impacto
- Plan de adecuación para cambios con plazo
