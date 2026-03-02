# Análisis Técnico: NTCO PMGD — Norma Técnica CNE Feb-2026

**Documento de referencia:** Resolución Exenta CNE N° 69, 19 de febrero de 2026  
**Publicación:** Diario Oficial 19-feb-2026  
**Marco legal:** Decreto Supremo N° 88/2019 — Ministerio de Energía (Reglamento PMGD)  
**Ley habilitante BESS:** Ley 21.505 sobre Almacenamiento y Electromovilidad  

---

## ¿Qué es la NTCO PMGD?

La **Norma Técnica de Conexión y Operación de Pequeños Medios de Generación Distribuida en instalaciones de Media Tensión** (NTCO PMGD) es el instrumento regulatorio que define las condiciones técnicas y operacionales que deben cumplir los PMGD conectados a redes de distribución en MT.

Esta versión de febrero 2026 es la **actualización más significativa desde el DS 88/2019** y responde a la masificación del almacenamiento en baterías (BESS) en proyectos PMGD.

---

## Los 5 Cambios Clave de la Norma

### 1️⃣ BESS — Bloques Horarios de Inyección (Cambio más relevante)

La norma incorpora por primera vez una **regulación específica para PMGD con sistemas de almacenamiento**.

**¿Qué son los bloques horarios de inyección?**

Son ventanas de tiempo definidas por el Coordinador Eléctrico Nacional durante las cuales un PMGD+BESS puede inyectar energía desde sus baterías a la red. El objetivo es **usar las holguras de capacidad de la red** y evitar sobrecargas.

| Problema que resuelve | Sin bloques horarios | Con bloques horarios |
|---|---|---|
| Mediodía solar + BESS descargando | Red puede sobrecargarse | BESS no puede descargar en horario prohibido |
| Punta vespertina 18-22h | Sin control | BESS puede descargar maximizando valor |
| Noche baja demanda | BESS puede sobrecargar red | Descarga regulada |

**Implicancias técnicas para nuevos proyectos PMGD+BESS:**
- El inversor BESS debe aceptar señales de control externas (del Coordinador o distribuidora)
- El contrato de conexión debe incluir cláusulas de recorte de inyección BESS
- El SITR debe enviar el estado del BESS en tiempo real (SOC, potencia, modo)
- **El CEN puede instruir recortes directos de inyección** sin previo aviso cuando lo requiera la seguridad del sistema

---

### 2️⃣ Criterios de Congestión — Transmisión Zonal

La norma introduce **nuevos criterios para evaluar congestiones en el sistema de transmisión zonal** que afectan la capacidad de conexión de PMGD.

**Cambio respecto a la norma anterior:**

| Criterio anterior | Criterio nuevo (feb-2026) |
|---|---|
| Evaluación rígida de congestión | Mayor **flexibilidad** en la evaluación |
| Análisis estático | Análisis adaptativo (considera holguras dinámicas) |
| Rechazo directo si hay congestión | Puede aprobarse con restricciones operacionales |

**Impacto práctico:**
- Proyectos en zonas con transmisión zonal saturada que antes eran rechazados ahora pueden ser evaluados con condiciones
- El ECAP debe incluir análisis de congestión en transmisión zonal según los nuevos criterios
- Posible aprobación condicionada a recortes automáticos cuando hay congestión

---

### 3️⃣ Capítulo 9 — Operación, Monitoreo, Control y Coordinación (NUEVO)

El Capítulo 9 es la sección más renovada de la norma. Establece **nuevas exigencias estrictas** para que los PMGD sean visibles y controlables por los agentes del mercado.

**Contenido del nuevo Capítulo 9:**

| Materia | Exigencia nueva |
|---|---|
| **Monitoreo en tiempo real** | El PMGD debe enviar variables al sistema del Coordinador y la distribuidora en tiempo real |
| **Control remoto** | El Coordinador y distribuidora deben tener capacidad de comando sobre el PMGD cuando sea necesario para la seguridad del sistema |
| **Coordinación con agentes** | El PMGD debe coordinar operación con el CEN y la distribuidora según protocolos definidos |
| **Visibilidad BESS** | Para PMGD+BESS: deben enviarse variables de estado del sistema de almacenamiento |
| **Habilitación de recortes** | El PMGD debe aceptar instrucciones de recorte de inyección del Coordinador |

**Implicancias en SITR:**

```
Variables mínimas nuevas para PMGD bajo el Cap. 9:

Generación solar:
  - Potencia activa inyectada (MW)
  - Potencia reactiva (MVAR)
  - Tensión en punto de conexión (kV)
  - Estado interruptor

BESS (adicionales, si tiene):
  - Potencia activa BESS (carga -/descarga +) (MW)
  - Estado de carga SOC (%)
  - Estado: cargando / descargando / en espera
  - Modo de operación (automático / restricción horaria / recorte CEN)
```

---

### 4️⃣ Evaluación de Coincidencias de Inyección en Horarios Críticos

La norma define un **procedimiento estandarizado** para evaluar si múltiples PMGD inyectan simultáneamente en horarios donde la red tiene menor capacidad de absorción.

**¿Qué es un horario crítico?**

Períodos en que la demanda es baja y la generación solar es alta (típicamente mediodía en verano), o períodos de alta demanda con límites en transmisión zonal.

**El nuevo procedimiento permite:**
1. Identificar zonas geográficas con alta concentración de PMGD
2. Calcular la coincidencia de inyección máxima en horarios críticos
3. Definir restricciones operativas antes de que ocurran sobrecargas (preventivo, no reactivo)

---

### 5️⃣ Precio Básico de Energía

La norma introduce el concepto de **"precio básico de energía"** como referencia para la remuneración de PMGD, reemplazando el esquema de precio estabilizado anterior.

**Valores referenciales vigentes (enero 2026):**

| Zona | Subestación | Bloque nocturno | Bloque diurno |
|---|---|---|---|
| Norte | Parinacota | **$91.722/kWh** (máximo) | Menor (alta solar) |
| Centro | Cerro Navia / Polpaico | ~$89.000/kWh (noche) | Baja al mediodía |
| Sur | Puerto Montt | **$54.966/kWh** (mínimo) | — |

> Diferencia máxima entre zonas: **~$37/kWh** — factor clave para decisión de inversión y ubicación del proyecto.

La CNE actualiza este indicador dentro de los primeros 5 días de cada mes.

---

## Impacto en Proyectos PMGD Vigentes y Nuevos

### Para proyectos en operación (antes de feb-2026):

| Situación | Acción requerida |
|---|---|
| PMGD sin BESS | Verificar si el nuevo Cap. 9 requiere variables de monitoreo adicionales |
| PMGD con BESS ya conectado | **Revisar contrato de conexión** — debe incluir cláusulas de recorte |
| Acuerdo SITR firmado | Revisar si cubre nuevas variables del Cap. 9 |

### Para proyectos nuevos (post 19-feb-2026):

| Requisito nuevo | Obligatorio desde |
|---|---|
| Variables BESS en SITR | Entrada en operación post 19-feb-2026 |
| Bloques horarios BESS en contrato | Todos los proyectos con BESS |
| Capacidad de control remoto BESS | Obligatorio en especificaciones técnicas |
| ECAP con análisis de congestión zonal | Todos los proyectos nuevos |

---

## Resumen de Brechas Comunes que Generará Esta Norma

Basado en el análisis, los errores más frecuentes que encontraremos en proyectos PMGD post-2026:

| Brecha | Probabilidad | Skill para diagnosticarla |
|---|---|---|
| SITR sin variables BESS (SOC, estado, potencia separada) | 🔴 Alta | skill_base_sitr + skill_pmgd_pmg |
| Contrato de conexión sin cláusula de recorte CEN | 🔴 Alta | skill_pmgd_pmg |
| Inversor BESS sin interfaz de control remoto | 🟠 Media | skill_estudio_ecap |
| ECAP sin análisis de congestión transmisión zonal | 🟠 Media | skill_estudio_ecap |
| Relé antipasivación sin ajuste para BESS activo | 🔴 Alta | skill_coordinacion_protecciones |
| Desconocimiento de bloques horarios por el operador | 🟡 Baja (técnica) | skill_vigilancia_normativa |

---

## Oportunidad Comercial CONECTA

> Esta norma crea una **ventana de oportunidad de 6–12 meses** donde la mayoría del mercado aún no sabe cómo implementarla correctamente.

**Tres servicios concretos:**

1. **Diagnóstico de adecuación NTCO PMGD** — para proyectos ya en operación con BESS  
   → *¿Tu proyecto cumple con el Cap. 9 post 19-feb-2026?*

2. **Estudio ECAP con nueva metodología** — para proyectos nuevos con BESS  
   → *Incluye análisis de congestión zonal bajo criterios nuevos*

3. **Revisión de contratos de conexión** — para verificar cláusulas de recorte BESS  
   → *Lo que la norma exige y lo que el contrato dice son cosas distintas*

---

## Referencias

| Documento | Referencia |
|---|---|
| Resolución Exenta CNE N° 69 | 19-feb-2026, Diario Oficial |
| DS 88/2019 — Reglamento PMGD | Ministerio de Energía |
| Ley 21.505 — Almacenamiento y Electromovilidad | Ley habilitante para BESS en PMGD |
| Fijación precios básicos energía | CNE, actualizada primeros 5 días de cada mes |

**Fuentes de seguimiento:**
- https://www.cne.cl/normativa/electricidad/normas-tecnicas/
- https://www.energia.gob.cl/tema/pequenos-medios-de-generacion-distribuida
