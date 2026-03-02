# Ejemplo: EDAC Post-Evento — Generadora Río Claro

**Skill utilizada:** `skill_edac_edag_erag`
**Tipo de coordinado:** Central hidroeléctrica 85 MW, con EDAC configurado

---

## Inputs del caso

- Empresa: Hidro Río Claro S.A.
- Instalación: Central HR-01, 85 MW (3 unidades de 28.3 MW)
- Esquema: EDAC con desconexión de 60 MW ante baja frecuencia < 49.2 Hz
- Evento reportado: 14-Feb-2025, 14:32:15 UTC — apagón parcial zona sur
- Frecuencia disparadora: 48.9 Hz (< 49.2 Hz umbral configurado)
- Carga desconectada real: 48 MW
- Carga esperada a desconectar: 60 MW
- Tiempo de operación registrado: 430 ms

---

## Evaluación de Desempeño

### Verificación de Tiempo

| Medición | Valor | Requisito | Estado |
|---|---|---|---|
| Tiempo de operación esquema | 430 ms | <= 200 ms | ❌ Incorrecto |
| Frecuencia de disparo | 48.9 Hz | < 49.2 Hz (correcto umbral) | ✅ OK |

### Verificación de Magnitud

```
Carga real desconectada:     48 MW
Carga esperada desconectar:  60 MW

% Desempeño = (48 / 60) × 100 = 80%
```

| Rango | Calificación |
|---|---|
| 80% – 120% | ✅ Correcto |
| > 120% | ⚠️ Sobreactuación |
| 20% – 80% | 🔴 Deficiente |
| 0% – 20% | 🔴 Incorrecto |

**Resultado magnitud: 80% → Límite inferior de "Correcto"** ⚠️ (requiere análisis)

### Diagnóstico del Tiempo de Operación (430 ms >> 200 ms)

Causas probables a investigar:
1. Relé de frecuencia con tiempo intencional mal configurado (debería ser 0 ms)
2. Interruptor de potencia con tiempo de apertura > 100 ms (revisión mecánica)
3. Lógica EDAC en PLC con ciclo de scan excesivo (> 50 ms)

---

## Información del Registro de Evento

| Campo | Valor |
|---|---|
| Fecha y hora | 14-Feb-2025 14:32:15.432 UTC |
| Evento gatillante | Frecuencia < 49.2 Hz |
| Frecuencia mínima registrada | 48.9 Hz |
| MW desconectados | 48 MW |
| MW esperados | 60 MW |
| Tiempo de operación | 430 ms |
| Marca de tiempo GPS | ✅ Sincronizado |
| Informe enviado al CEN | Pendiente |

---

## Brechas Identificadas

| ID | Brecha | Criticidad | Acción |
|---|---|---|---|
| E01 | Tiempo operación 430 ms (> 200 ms requerido) | 🔴 Alta | Diagnóstico urgente del sistema EDAC |
| E02 | % desempeño en límite inferior (80%) | 🟠 Media | Revisar configuración de cargas a desconectar |
| E03 | Informe post-evento no enviado al CEN | 🟠 Media | Enviar dentro de 48 horas del evento |

---

## Conclusión
El EDAC operó correctamente en magnitud (80%), pero **el tiempo de operación de 430 ms supera ampliamente los 200 ms requeridos**, lo que califica el esquema como de "desempeño incorrecto por tiempo". Se requiere diagnóstico técnico urgente y comunicación formal al Coordinador.
