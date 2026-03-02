---
name: evaluating-ecap-study
description: Analiza y genera estudios ECAP para conexión al Sistema Eléctrico Nacional (SEN). Usar cuando el usuario mencione "estudio de conexión", "ECAP", "conexión al SEN", "interconexión eléctrica" o "evaluación de conexión".
---

# Skill: Estudio ECAP — Conexión al SEN

## Cuándo usar este skill
- Usuario menciona "estudio de conexión al SEN" o "ECAP"
- Se necesita evaluar viabilidad de conexión de un nuevo coordinado
- Se requiere análisis de impacto en la red por nueva instalación
- Se pide revisión de requisitos técnicos para interconexión

## Workflow

```markdown
- [ ] Identificar tipo de proyecto (generación, transmisión, distribución, PMGD/PMG)
- [ ] Levantar datos técnicos del proyecto (potencia, tensión, punto de conexión)
- [ ] Identificar normativa aplicable (NTCS, NSEG, procedimientos CEN)
- [ ] Ejecutar análisis de flujo de potencia
- [ ] Ejecutar análisis de cortocircuito
- [ ] Evaluar coordinación de protecciones
- [ ] Revisar calidad de suministro (armónicos, tensión, frecuencia)
- [ ] Redactar informe ECAP con observaciones y recomendaciones
```

## Instrucciones

### 1. Recopilación de Datos del Proyecto
Solicitar al usuario:
- Tipo y potencia instalada (MW/MVA)
- Punto de conexión propuesto (subestación, barra, tensión nominal)
- Tecnología de generación (solar, eólica, PMGD, hidro, etc.)
- Curva de potencia y disponibilidad estimada
- Equipamiento de interconexión (transformadores, interruptores, relés)

### 2. Análisis de Flujo de Potencia
Evaluar:
- Flujos en líneas y transformadores vecinos (verificar capacidad térmica)
- Perfiles de tensión en la barra de conexión (±5% en condición normal, NTCS)
- Flujos ante contingencias N-1 y N-2 cuando aplique
- Identificar cuellos de botella y restricciones de capacidad

### 3. Análisis de Cortocircuito
Evaluar:
- Corriente de cortocircuito trifásico y monofásico en punto de conexión
- Verificar que corrientes no superen capacidad de ruptura de equipos existentes
- Calcular aportes del nuevo proyecto al sistema
- Revisar coordinación con protecciones existentes

### 4. Coordinación de Protecciones
Revisar:
- Ajustes de relés de sobrecorriente, distancia y diferencial
- Protección de isla involuntaria (antipasivación)
- Requisitos de automatismo según NTSyCS y procedimientos CEN
- Tiempos de despeje de falla (≤ 200 ms para EDAC cuando aplique)

### 5. Calidad de Suministro
Revisar:
- Armónicos: THD tensión ≤ 8% (IEC 61000-3-6, NCh)
- Flicker: Pst ≤ 1.0 / Plt ≤ 0.65
- Desequilibrio de tensión ≤ 2%
- Variaciones de frecuencia dentro de rango CEN

### 6. Estructura del Informe ECAP

```
1. Resumen ejecutivo
2. Descripción del proyecto y punto de conexión propuesto
3. Normativa aplicable
4. Datos del sistema existente
5. Resultados de flujo de potencia (caso base + contingencias)
6. Resultados de cortocircuito
7. Evaluación de protecciones
8. Calidad de suministro
9. Conclusiones y requisitos para conexión
10. Anexos (modelos, datos, simulaciones)
```

## Normativa de Referencia
- NTCS (Norma Técnica de Calidad de Servicio) vigente
- Normas de Seguridad (NSEG) aplicables
- Procedimientos CEN aplicables a coordinados
- SITR: requisitos de telemetría para nuevo coordinado
- NCh Elec 4/2003 y actualizaciones

## Entradas Esperadas
- Ficha técnica del proyecto
- Modelo de red del área de influencia (datos del Coordinador)
- Datos de cortocircuito en barra de conexión (solicitables al CEN)

## Salidas Esperadas
- Informe ECAP con resultados de simulación
- Tabla de brechas y requisitos para conexión
- Checklist de condiciones previas a la conexión

## Errores Comunes
- ❌ **No solicitar los datos de Icc al CEN antes de empezar** — sin ese dato no se puede verificar si los equipos existentes son suficientes
- ❌ **Asumir N-1 siempre cumple sin calcularlo** — en redes débiles o PMGD rurales, la contingencia N-1 puede superar el +5% de tensión
- ❌ **Olvidar la protección de antipasivación (anti-isla)** — es obligatoria para toda generación conectada en red de distribución; sin ella no puede aprobarse la conexión
- ❌ **Emitir el informe sin firma de ingeniero competente** — el ECAP debe ir firmado por un profesional competente; de lo contrario el CEN no lo acepta
- ❌ **No incluir requisitos SITR en el informe** — el nuevo coordinado hereda inmediatamente las obligaciones SITR; deben detallarse en el informe

## Ejemplo Real
- [Parque Eólico Punta Negra 5 MW — Conexión PMGD](examples/example_ecap.md)

## Consideraciones
- No reemplaza al software de simulación (PSS/E, DIgSILENT, PSCAD)
- Los datos del sistema deben validarse con el CEN
- El informe debe ser firmado por ingeniero eléctrico competente
- Los plazos del proceso de conexión los define el Coordinador (AT-SITR-1 mar-2025)
