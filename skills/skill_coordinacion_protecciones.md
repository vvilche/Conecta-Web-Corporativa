---
name: coordinating-electrical-protections
description: Analiza, ajusta y documenta la coordinación de protecciones eléctricas. Usar cuando el usuario mencione "coordinación de protecciones", "ajuste de relés", "curvas de tiempo-corriente", "selectividad", "protección diferencial", "protección de distancia" o "relay settings".
---

# Skill: Coordinación de Protecciones Eléctricas

## Cuándo usar este skill
- Se necesita ajustar relés de sobrecorriente, diferencial o distancia
- Se evalúa selectividad entre protecciones en cascada
- Se verifica coordinación para estudios ECAP o post-falla
- Se prepara documentación de ajustes para el Coordinador o SEC

## Workflow

```markdown
- [ ] Recopilar datos del sistema (Icc en cada barra, calibres, equipos)
- [ ] Identificar zona de protección y relés involucrados
- [ ] Calcular corrientes de pick-up para cada relé
- [ ] Calcular tiempos de operación verificando selectividad
- [ ] Verificar tiempo de despeje de falla total (<= 200 ms para EDAC)
- [ ] Graficar curvas TCC (Tiempo-Corriente-Corriente) si aplica
- [ ] Verificar zonas de protección de distancia (si aplica AT)
- [ ] Documentar ajustes en tabla de settings
- [ ] Verificar coordinación con protecciones aguas arriba y abajo
```

## Instrucciones

### 1. Tipos de Protección y Aplicación

| Tipo | Función | Aplicación típica |
|---|---|---|
| **Sobrecorriente (50/51)** | Detecta exceso de corriente | BT, MT, generadores |
| **Sobrecorriente direccional (67)** | Detecta dirección del flujo de falla | Redes con múltiples fuentes |
| **Diferencial (87)** | Comparación de corrientes entrada/salida | Transformadores >= 10 MVA, barras |
| **Distancia (21)** | Detecta falla por impedancia medida | Líneas de AT |
| **Tensión (27/59)** | Baja/sobretensión | Generadores, barras |
| **Frecuencia (81)** | Baja/sobrefrecuencia | Generadores, EDAC |
| **Diferencial de tierra (87N)** | Fallas a tierra resistivas | Transformadores AT |

### 2. Cálculo de Settings — Sobrecorriente (50/51)

**Pick-up de corriente (Ip):**
```
Ip = 1.25 × In_máximo_circuito    (para 51, arranque de tiempo inverso)
Ip = 0.8 × Icc_mínima_zona       (verificar que detecta toda falla)

Condición: Ip_aguas_arriba > Ip_aguas_abajo × 1.1  (selectividad)
```

**Tiempo de operación (curva normal inversa, IEC 60255-151):**
```
t = TMS × [0.14 / ((I/Ip)^0.02 - 1)]

Donde:
TMS = Time Multiplier Setting (ajuste de tiempo)
I = corriente de falla
Ip = corriente de pickup

Para garantizar selectividad:
t_aguas_arriba(Icc) >= t_aguas_abajo(Icc) + intervalo de coordinación

Intervalo de coordinación típico: 0.3–0.4 s
```

**Pick-up instantáneo (50):**
```
Ip_inst = 1.25 × Icc_máx_fin_zona_propia    (no debe ver Icc aguas abajo)
```

### 3. Verificación Tiempo de Despeje Total

> ⚠️ **Crítico para EDAC**: tiempo total de despeje <= 200 ms

```
t_despeje_total = t_relé + t_interruptor

t_relé típico:    20–60 ms (relé numérico moderno)
t_interruptor:    40–80 ms (interruptor SF6/vacío MT)
                  60–100 ms (disyuntor AT)

Ejemplo: t_relé = 30 ms + t_int = 60 ms → t_total = 90 ms ✅ < 200 ms
```

### 4. Tabla de Settings — Formato Estándar CONECTA

```markdown
| Relé | Barra | Función | Ip (A primario) | TMS | t_inst (ms) | Ip_inst (A) | Estado |
|------|-------|---------|-----------------|-----|-------------|-------------|--------|
| R01 | B1-110kV | 51 | 450 | 0.30 | — | — | ✅ |
| R02 | B1-110kV | 50 | — | — | 30 | 8500 | ✅ |
| R03 | T1-23kV | 87 | 85 (diferencial) | — | 30 | — | ✅ |
| R04 | B2-23kV | 51 | 320 | 0.15 | — | — | ✅ |
```

### 5. Verificación de Selectividad — Reglas

- ✅ **Selectividad por tiempo**: diferencia entre curvas >= 0.3 s en punto Icc
- ✅ **Selectividad por corriente**: 50-inst aguas arriba no opera ante Icc al final de zona aguas abajo
- ✅ **Zona de back-up**: relé aguas arriba cubre falla si relé aguas abajo falla (t + margen)
- ⚠️ Revisar punto de cruce de curvas: si cruzan, hay pérdida de selectividad

### 6. Coordinación con CEN — Requisitos
Para coordinados con EDAC/EDAG/ERAG:
- Tiempo de despeje de falla no puede superar el umbral que active el esquema incorrectamente
- Los ajustes deben ser declarados al Coordinador si afectan al esquema EDAC
- Cambios en ajustes que impacten tiempos de operación → aviso >= 20 días

## Normativa Aplicable
- IEC 60255-151: Características de tiempo-corriente
- IEC 60909: Corrientes de cortocircuito (base para ajuste)
- EDAC/EDAG/ERAG jun-2015: Tiempo de actuación <= 200 ms
- Instrucciones del Coordinador para esquemas EDAC específicos

## Cross-references
- `skill_calculo_cortocircuito.md` → Datos de Icc necesarios como input
- `skill_edac_edag_erag.md` → Requisitos de tiempo de despeje
- `skill_estudio_ecap.md` → Coordinación como parte del estudio ECAP

## Errores Comunes
- ❌ Usar Icc máximo para ajustar relé de back-up (debe usarse Icc mínimo de la zona)
- ❌ Olvidar el tiempo del interruptor al calcular t_despeje total
- ❌ No verificar que el 50-inst aguas arriba no ve la Icc al final de la zona aguas abajo
- ❌ Ajustar solo con Icc trifásico sin revisar falla monofásica (puede ser < pick-up)

## Salida Esperada
- Tabla de settings completa con todos los relés del sistema
- Verificación de selectividad en puntos críticos
- Confirmación de tiempos de despeje <= 200 ms donde aplica EDAC
