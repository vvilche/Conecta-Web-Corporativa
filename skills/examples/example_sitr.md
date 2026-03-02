# Ejemplo: Diagnóstico SITR — Central Solar Los Llanos 50 MW

**Skill utilizada:** `skill_base_sitr` + `skill_generacion`
**Tipo de coordinado:** Generación solar fotovoltaica, 50 MW, conectada en barra 110 kV

---

## Inputs del caso

- Empresa: Energías Los Llanos SpA
- Proyecto: Central Solar Los Llanos, Atacama
- Potencia: 50 MW en 6 inversores de 8.3 MW c/u
- Punto de conexión: S/E Los Llanos 110 kV (barra del CEN)
- SITR: Enlace DNP3 TCP/IP instalado, protocolo acordado con el Coordinador
- GPS: Equipo Trimble instalado, sin calibración reciente documentada
- Respaldo: UPS 4 horas disponibles
- Disponibilidad último mes: 97.8%
- PMUS: PMU Schweitzer SEL-421 instalada solo en 1 de 6 inversores (>= 9 MW c/u: NO → el conjunto sí es >= 9 MW)

---

## Diagnóstico Ejecutado

### Verificación SITR Base

| Parámetro | Requisito | Valor actual | Estado |
|---|---|---|---|
| Disponibilidad mensual | >= 99.5% | 97.8% | ❌ Crítico |
| GPS sincronización | +/- 100 µs | No calibrado en 14 meses | ⚠️ Revisar |
| Marcas de tiempo | >= 1 ms resolución | 1 ms ✅ | ✅ OK |
| Edad de datos | <= 5 s | 3 s promedio | ✅ OK |
| Muestreo analógico | <= 2 s | 1 s | ✅ OK |
| Precisión | Clase 2 ANSI | Clase 2 certificado | ✅ OK |
| Respaldo alimentación | >= 6 h | 4 h | ❌ Insuficiente |
| Protocolo acordado | Sí | DNP3 TCP/IP acordado | ✅ OK |

### Verificación PMUS (Generación >= 9 MW)

La central tiene 50 MW total. El estudio MMF 2025 la incluye como punto requerido.

| Parámetro | Requisito | Estado actual | Estado |
|---|---|---|---|
| PMU instalada | Sí (50 MW) | Solo en 1 inversor | ❌ Incompleto |
| Clase PMU | M-Class | SEL-421 es M-Class | ✅ OK |
| Tasa de muestreo | 50 mps | 50 mps configurado | ✅ OK |
| Protocolo | IEEE C37.118 | Configurado | ✅ OK |
| Segundo enlace | Requerido | No habilitado | ❌ Falta |
| Alimentación respaldo | >= 8 h | 4 h | ❌ Insuficiente |
| Ancho de banda | >= 120 kbps | 256 kbps | ✅ OK |
| Dossier PES | Requerido | Parcial | ⚠️ Completar |
| Checklist PMUS anual | Requerido | No realizada 2024 | ❌ Vencida |

---

## Tabla de Brechas y Plan de Acción

| ID | Brecha | Criticidad | Plazo | Responsable |
|---|---|---|---|---|
| B01 | Disponibilidad SITR 97.8% (debe ser >= 99.5%) | 🔴 Alta | 30 días | TI/Telecom |
| B02 | Respaldo alimentación 4 h (debe ser >= 6 h SITR / >= 8 h PMUS) | 🔴 Alta | 60 días | Mantenimiento |
| B03 | GPS sin calibración documentada desde hace 14 meses | 🟠 Media | 30 días | Ingeniería |
| B04 | PMU solo en 1 inversor; todos los >= 9 MW deben tener o el conjunto | 🔴 Alta | 90 días | Ingeniería |
| B05 | Segundo enlace PMU/PDC no habilitado | 🟠 Media | 90 días | TI/Telecom |
| B06 | Checklist PMUS anual 2024 no realizada | 🟠 Media | 15 días | Cumplimiento |
| B07 | Dossier PES incompleto (faltan manuales y pruebas) | 🟡 Baja | 45 días | Ingeniería |

---

## Conclusión
La central presenta **3 brechas críticas** que requieren acción inmediata, especialmente la disponibilidad SITR (97.8% vs 99.5% requerido) que puede generar multas o requerimientos formales del Coordinador. Se recomienda iniciar plan de remediación en los próximos 5 días hábiles.
