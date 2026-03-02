---
name: evaluating-pmgd-pmg-compliance
description: Evalúa cumplimiento normativo CEN para PMGD y PMG coordinados. Usar cuando el usuario mencione "PMGD", "PMG", "pequeños medios de generación distribuida", "generación distribuida", "inyección en red de distribución" o "medición PMGD".
---

# Skill: Cumplimiento CEN — PMGD / PMG

## Cuándo usar este skill
- Coordinado opera uno o más PMGD o PMG
- Se revisan obligaciones SITR vía distribuidora
- Se evalúa necesidad de PMUS en subestación con concentración > 20 MW PMGD
- Se verifica disponibilidad de mediciones para el Coordinador y distribuidora

## Workflow

```markdown
- [ ] Identificar tipo: PMGD (< 9 MW) o PMG (9–20 MW) y capacidad total instalada
- [ ] Verificar punto de conexión (red distribución o transmisión)
- [ ] Verificar enlace al sistema de comunicaciones de la distribuidora
- [ ] Verificar disponibilidad de medidas para Coordinador y distribuidora
- [ ] Evaluar si SE/EE de conexión tiene > 20 MW PMGD acumulados (acción PMUS)
- [ ] Si aplica PMUS: verificar instalación y especificaciones PMU
- [ ] Identificar brechas y plan de acción
```

## Instrucciones

### 1. Contexto Normativo PMGD/PMG

| Tipo | Potencia | Conexión típica | Coordinación SITR |
|---|---|---|---|
| PMGD | <= 9 MW | Red distribución MT | Vía sistema comunicaciones distribuidora |
| PMG | 9–20 MW | Red distribución o transmisión | Puede ser directo al CEN |

### 2. Obligaciones SITR PMGD/PMG

| Obligación | Descripción | Fuente |
|---|---|---|
| Enlace vía distribuidora | Cuando conexión es en red distribución | AT-SITR-1 |
| Medidas disponibles para CEN | Potencia activa/reactiva, tensión, estado | SITR dic-2019 |
| Medidas disponibles para distribuidora | Mismas u otras según acuerdo de conexión | AT-SITR-1 |
| Disponibilidad | >= 99.5% mensual | AT-SITR-1 |

### 3. Umbral PMUS — SS/EE con Concentración > 20 MW PMGD

Si en una subestación se concentran PMGD con potencia total > 20 MW:
- Puede requerirse instalación de PMU en esa SS/EE según estudio MMF vigente
- Verificar en el último Estudio MMF si el punto está incluido
- Si está incluido → aplicar requisitos de `skill_generacion.md` (especificaciones PMU)

### 4. Documentación Requerida de Enlace
- Diagrama de conexión al sistema de comunicaciones de la distribuidora
- Acuerdo entre PMGD/PMG y distribuidora para el enlace
- Aprobación del Coordinador del esquema de enlace
- Aviso al Coordinador >= 30 días ante cambios en acuerdos

## Fuentes Autorizadas
- SITR dic-2019: `documentos/fuentes/SITR-dic2019.pdf`
- AT-SITR-1 mar-2025: `documentos/fuentes/AT-SITR-1-mar2025.pdf`
- Estudio PMUS 2025: `documentos/fuentes/PMUS-Estudio-2025.pdf`
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`
- **NTCO PMGD feb-2026**: Resolución Exenta CNE N° 69, 19-feb-2026 (nueva)

## ⚡ Actualización: NTCO PMGD — Feb 2026 (Resolución Exenta N° 69)

> ⚠️ **Vigente desde el 19 de febrero de 2026.** Aplica a todos los proyectos nuevos y PMGDs con BESS ya conectados.

### 5 Cambios Clave

#### 1. BESS — Bloques Horarios de Inyección
Para PMGD que incorporan almacenamiento en baterías:
- La inyección desde baterías queda sujeta a **bloques horarios** definidos por el Coordinador
- El BESS debe aceptar señales de control externas (recorte disponible al CEN)
- **El CEN puede instruir recortes directos** de inyección BESS sin previo aviso cuando lo requiera la seguridad del sistema
- El contrato de conexión debe incluir cláusulas de recorte — **verificar contratos existentes**

#### 2. Nuevas Variables SITR para PMGD+BESS (Capítulo 9)
Además de las variables SITR estándar, los PMGD con BESS deben enviar:

| Variable nueva | Unidad | Descripción |
|---|---|---|
| Potencia activa BESS | MW (+ descarga / - carga) | Separada de la generación solar |
| Estado de carga (SOC) | % | En tiempo real |
| Estado BESS | Enum | Cargando / descargando / en espera |
| Modo de operación | Enum | Automático / restricción horaria / recorte CEN |

#### 3. Congestión — Transmisión Zonal
- Nuevos criterios más **flexibles** para evaluar congestiones en transmisión zonal
- Proyectos antes rechazados por congestión pueden ahora aprobarse con restricciones operacionales
- El ECAP debe analizar congestión zonal bajo los nuevos criterios (solicitar metodología actualizada al CEN)

#### 4. Horarios Críticos — Procedimiento Estandarizado
- Nuevo procedimiento uniforme para evaluar "coincidencias de inyección" en horarios de baja demanda + alta generación solar
- Permite restricciones preventivas antes de sobrecargas

#### 5. Precio Básico de Energía (referencia)
| Zona | Bloque nocturno | Bloque diurno |
|---|---|---|
| Norte (Parinacota) | **$91.722/kWh** (máx.) | Menor (alta solar) |
| Centro (Cerro Navia) | ~$89.000/kWh | Baja al mediodía |
| Sur (Puerto Montt) | **$54.966/kWh** (mín.) | — |

La CNE actualiza este valor los primeros 5 días de cada mes.

### Checklist de Adecuación — PMGD+BESS Post 19-Feb-2026

```markdown
- [ ] Variables SITR BESS confirmadas con CEN (SOC, potencia, estado, modo)
- [ ] Contrato de conexión incluye cláusula de recorte CEN
- [ ] Inversor BESS con interfaz de control remoto habilitada
- [ ] Bloques horarios coordinados con distribuidora
- [ ] ECAP actualizado con análisis de congestión transmisión zonal
- [ ] Relé antipasivación ajustado para BESS activo
```

## Análisis completo
- [fuentes_externas/analisis_ntco_pmgd_feb2026.md](../fuentes_externas/analisis_ntco_pmgd_feb2026.md)
- [Ejemplo PMGD+BESS](examples/example_pmgd_bess.md)

## Errores Comunes
- ❌ **No revisar el contrato de conexión** — el contrato anterior puede no incluir la cláusula de recorte CEN requerida ahora
- ❌ **Asumir que el SITR estándar cubre BESS** — las variables de SOC, estado y potencia BESS son nuevas y deben coordinarse con el CEN
- ❌ **No verificar el inversor BESS** — muchos inversores BESS no tienen interfaz de control remoto habilitada por defecto
- ❌ **Olvidar la potencia en límite 20 MW** — si la SS/EE llega exactamente a 20 MW, es obligatorio consultar al CEN sobre estudio MMF

## Checklists
- `documentos/checklists/checklist_pmgd_pmg.md`
- `documentos/checklists_xlsx/checklist_pmgd_pmg.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento PMGD/PMG con tabla de brechas
- Evaluación del umbral PMUS (>20 MW en SS/EE)
- Verificación de adecuación NTCO PMGD feb-2026 (si tiene BESS)
- Plan de acción con responsables y plazos

