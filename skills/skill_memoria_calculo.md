---
name: generating-calculation-report
description: Genera y estructura memorias de cálculo eléctrico para proyectos de ingeniería. Usar cuando el usuario mencione "memoria de cálculo", "memoria técnica", "justificación de diseño", "cálculo eléctrico" o "dimensionamiento".
---

# Skill: Memoria de Cálculo Eléctrico

## Cuándo usar este skill
- Usuario pide generar o revisar una memoria de cálculo
- Se necesita justificar dimensionamiento de equipos o conductores
- Se requiere documento formal para presentar a SEC, CEN o cliente
- Se necesita verificar cálculos de un diseño existente

## Workflow

```markdown
- [ ] Definir alcance y tipo de instalación
- [ ] Recopilar datos de entrada (cargas, características red, normativa)
- [ ] Calcular demanda máxima y factor de demanda
- [ ] Dimensionar conductores (capacidad de corriente y caída de tensión)
- [ ] Dimensionar protecciones (sobrecorriente, diferencial, sobretensión)
- [ ] Calcular sistema de puesta a tierra
- [ ] Calcular alumbrado si aplica
- [ ] Validar resultados contra normativa
- [ ] Redactar memoria con estructura formal
```

## Instrucciones

### 1. Estructura de la Memoria de Cálculo

```
1. Portada y datos del proyecto
2. Tabla de contenidos
3. Alcance y descripción del sistema
4. Normativa y referencias aplicables
5. Datos de alimentación (tensión, potencia disponible, Icc)
6. Inventario de cargas
7. Cálculo de demanda máxima
8. Dimensionamiento de conductores
9. Dimensionamiento de protecciones
10. Cálculo de corriente de cortocircuito (referencia a skill_calculo_cortocircuito)
11. Sistema de puesta a tierra
12. Cálculo de alumbrado (si aplica)
13. Conclusiones
14. Anexos (tablas de referencia, fichas técnicas)
```

### 2. Inventario y Demanda de Cargas

Tabla de cargas estándar:
```markdown
| N° | Descripción | Potencia instalada (kW) | FP | FD | Potencia demandada (kW) |
|----|-------------|------------------------|----|----|------------------------|
| 1  | Motor X     | 75                     | 0.85 | 0.75 | 56.25 |
| 2  | Alumbrado   | 10                     | 1.00 | 1.00 | 10.00 |
| Total | | 85 | | | 66.25 |
```

**Factores de demanda (FD) típicos:**
- Motores industriales: 0.70–0.85
- Alumbrado: 1.00
- Climatización: 0.70–0.90
- TICS/Data center: 0.90–1.00
- Cargas varias: 0.50–0.80

### 3. Dimensionamiento de Conductores

**Paso 1: Corriente nominal**
```
In = P_demandada / (√3 × Vnom × FP × η)      [trifásico]
In = P_demandada / (Vnom × FP × η)             [monofásico]
```

**Paso 2: Corriente de diseño (factores de corrección)**
```
Id = In / (Fc_temp × Fc_agrupamiento × Fc_tipo_instalación)
```

Factores de corrección comunes (IEC 60364 / NCh Elec 4):
- Temperatura 40°C: Fc ≈ 0.87 (cable XLPE 90°C)
- Temperatura 50°C: Fc ≈ 0.71
- 3 cables agrupados: Fc ≈ 0.70
- 6 cables agrupados: Fc ≈ 0.57

**Paso 3: Selección de cable**
Seleccionar cable donde: Iz_cable ≥ Id

**Paso 4: Verificar caída de tensión**
```
ΔV% = (√3 × In × L × (R·cosφ + X·senφ)) / Vnom × 100

Límites NCh Elec 4:
- BT alumbrado: ΔV ≤ 3%
- BT fuerza: ΔV ≤ 5%
- AT-MT: según normativa específica
```

### 4. Dimensionamiento de Protecciones

**Interruptores automáticos:**
```
Condición 1: In_protección ≥ In_circuito
Condición 2: In_protección ≤ Iz_cable
Condición 3: Icc_min ≥ I_disparo_magnético × 1.5 (verificar discriminación)
```

**Protección diferencial (BT):**
- Locales secos: IDn = 30 mA
- Locales húmedos: IDn = 30 mA (alta sensibilidad)
- Industrial: IDn = 300 mA o 500 mA según caso

### 5. Sistema de Puesta a Tierra

```
R_tierra = ρ / (2π × L) × ln(4L/d)   [electrodo vertical, Dwight]

Donde:
ρ = resistividad del suelo (Ω·m)  → medir o estimar por tipo de suelo
L = longitud del electrodo (m)
d = diámetro del electrodo (m)

Valores típicos de resistividad:
- Arcilla: 10–100 Ω·m
- Arena húmeda: 50–300 Ω·m
- Roca: 1000–10000 Ω·m
```

Resistencia máxima admisible:
- Instalaciones en BT: R ≤ 25 Ω (NCh Elec 4)
- Subestaciones MT/AT: R ≤ 1 Ω (recomendado)
- Torres de transmisión: R ≤ 10 Ω (o según CEN)

### 6. Presentación de Resultados

Cada cálculo debe incluir:
1. Hipótesis y datos de entrada
2. Fórmulas utilizadas con referencia normativa
3. Cálculo numérico paso a paso
4. Resultado obtenido
5. Comparación con límite normativo
6. Conclusión (✅ cumple / ❌ no cumple)

## Normativa de Referencia
- NCh Elec 4/2003: Instalaciones de consumo en BT
- IEC 60364: Instalaciones eléctricas de baja tensión
- IEC 60228: Conductores de cables aislados
- IEC 60269: Fusibles de baja tensión
- Reglamento SEC aplicable

## Salidas Esperadas
- Memoria de cálculo estructurada y trazable
- Tablas de resumen de resultados
- Conclusión de cumplimiento normativo
