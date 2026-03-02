# Ejemplo: Cumplimiento SSCC/AGC — Empresa Regulación Secundaria

**Skill utilizada:** `skill_sscc`
**Tipo de coordinado:** Central hidro 120 MW, prestadora de regulación secundaria (AGC)

---

## Inputs del caso

- Empresa: Energía Andina S.A.
- Central: Hidroeléctrica Andina, 120 MW (2 unidades Pelton de 60 MW)
- SSCC prestado: Regulación secundaria de frecuencia (AGC)
- Contrato vigente: Sí, renovado ene-2025
- Plataforma AGC: Sistema SCADA propio, protocolo IEC 60870-5-104 acordado con CEN

---

## Verificación de Parámetros de Control Declarados al Coordinador

| Parámetro | Valor declarado | Verificación terreno | Estado |
|---|---|---|---|
| Estatismo | 5% | 5% medido en prueba | ✅ OK |
| Banda muerta frecuencia | ± 0.02 Hz | ± 0.02 Hz configurado | ✅ OK |
| Rampa máxima | 6 MW/min | 6.1 MW/min (prueba) | ✅ OK |
| Pmin | 15 MW | 15 MW (mínimo técnico) | ✅ OK |
| Pmax | 120 MW | 118 MW (limitación actual unidad 2) | ⚠️ Actualizar al CEN |
| Tiempo respuesta escalón | <= 30 s | 22 s promedio | ✅ OK |

---

## Verificación del Canal AGC

| Parámetro | Requisito | Estado actual | Estado |
|---|---|---|---|
| Canal primario AGC | Operativo | IEC 60870-5-104 activo | ✅ OK |
| Canal respaldo AGC | Requerido | Enlace MPLS respaldo configurado | ✅ OK |
| Redundancia plataforma | SCADA redundante | Servidor primario + espejo | ✅ OK |
| Edad de datos control | <= 2 s | 0.8 s promedio | ✅ OK |
| Disponibilidad canal | >= 99.5% | 99.8% (último mes) | ✅ OK |

---

## Revisión Variables en Tiempo Real (SITR para AGC)

| Variable | Unidad | Enviada al CEN | Estado |
|---|---|---|---|
| Potencia activa neta | MW | ✅ | ✅ OK |
| Potencia reactiva neta | MVAR | ✅ | ✅ OK |
| Setpoint AGC recibido | MW | ✅ | ✅ OK |
| Estado disponibilidad AGC | Bool | ✅ | ✅ OK |
| Frecuencia en barra | Hz | ✅ | ✅ OK |
| Posición válvula (%) | % | ❌ No enviada | ⚠️ Revisar con CEN |

---

## Evento Detectado: Pérdida Canal AGC (15-Ene-2025)

| Detalle | Valor |
|---|---|
| Duración pérdida señal AGC | 4 minutos 32 segundos |
| Acción tomada por unidades | Modo "hold" (potencia fija) — correcto |
| Reportado al Coordinador | ❌ No se reportó formalmente |
| Tiempo de reconexión canal | Automático (failover a canal respaldo) |

---

## Tabla de Brechas

| ID | Brecha | Criticidad | Acción | Plazo |
|---|---|---|---|---|
| S01 | Pmax declarada al CEN (120 MW) ≠ real disponible (118 MW) | 🟠 Media | Comunicar al Coordinador ajuste de Pmax | 15 días |
| S02 | Variable "posición válvula" no enviada al SITR | 🟡 Menor | Verificar si el Coordinador la requiere; si sí, configurar | 30 días |
| S03 | Evento de pérdida de señal AGC (15-ene) no reportado formalmente | 🟠 Media | Enviar informe de evento al Coordinador | Inmediato |

---

## Conclusión
La central cumple en general con los requisitos de prestación de SSCC/AGC. Las brechas son menores y gestionables. **La más urgente es S03**: la no notificación del evento de pérdida de señal AGC, que es una obligación de reporte al Coordinador.
