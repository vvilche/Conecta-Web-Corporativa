# Ejemplo: Informe Técnico Formal — ECAP PMGD Punta Negra

**Skill utilizada:** `skill_informe_tecnico`
**N° Documento:** CON-ING-2025-005-INF, Rev. 1
**Tipo:** Informe ECAP para presentación al Coordinador

---

## PORTADA (Estructura)

```
CONECTA SpA — Ingeniería y Cumplimiento Eléctrico

ESTUDIO DE CONEXIÓN AL SEN (ECAP)
PARQUE EÓLICO PUNTA NEGRA — 5 MW

Cliente: Punta Negra Energías SpA
N° Documento: CON-ING-2025-005-INF
Revisión: Rev. 1
Fecha: 2025-02-20

Preparado por:  Ing. María González (Ingeniería CONECTA)
Revisado por:   Ing. Pedro Soto (Jefe Ingeniería CONECTA)
Aprobado por:   Ing. Carlos Ruiz (Gerente Técnico)
```

---

## CONTROL DE REVISIONES

| Rev. | Fecha | Descripción | Elaborado | Revisado | Aprobado |
|---|---|---|---|---|---|
| 0 | 2025-02-10 | Borrador para revisión interna | M.G. | P.S. | — |
| 1 | 2025-02-20 | Primera emisión oficial | M.G. | P.S. | C.R. |

---

## 1. RESUMEN EJECUTIVO

El presente informe analiza la viabilidad técnica de conexión del Parque Eólico Punta Negra (5 MW) a la barra MT 23 kV de la S/E Distribución Litoral Norte, Cooperativa Eléctrica Litoral.

Los resultados indican que la conexión es técnicamente viable, sin restricciones de flujo de potencia ni de cortocircuito. Se requiere la instalación de dos nuevos relés de protección (antipasivación y diferencial de transformador) y la firma de un acuerdo SITR con la empresa distribuidora.

Se recomienda aprobar la conexión condicionada al cumplimiento de estas dos medidas previas a la puesta en servicio.

---

## 3. NORMATIVA APLICABLE

- [N01] NTSyCS Mar-2025 — Norma Técnica de Seguridad y Calidad de Servicio
- [N02] AT-SITR-1 Mar-2025 — Especificaciones técnicas SITR
- [N03] IEC 60909:2016 — Corrientes de cortocircuito
- [N04] IEC 61000-3-6 — Compatibilidad electromagnética, armónicos
- [N05] NCh Elec 4/2003 — Instalaciones de consumo BT
- [N06] Procedimiento CEN: Conexión de Pequeños Medios de Generación Distribuida

---

## 5. RESULTADOS PRINCIPALES

### 5.1 Flujo de Potencia
Ver análisis completo en [example_ecap.md](example_ecap.md).

| Escenario | Tensión barra 23 kV | Flujo línea AT | Estado |
|---|---|---|---|
| Máxima generación | +1.2% | 82% capacidad | ✅ OK |
| Contingencia N-1 | +4.1% | 94% capacidad | ✅ OK (límite) |
| Mínima generación | -0.3% | — | ✅ OK |

### 5.2 Cortocircuito

| Punto | Icc3φ (kA) | Equipo existente | Estado |
|---|---|---|---|
| Barra 23 kV | 6.35 kA | Interruptor 12.5 kA | ✅ OK |

### 5.3 Protecciones — Condiciones para Conexión

| Protección | Acción requerida | Responsable |
|---|---|---|
| Relé antipasivación R02 | **Instalar antes de conexión** | Propietario PMGD |
| Diferencial transformador R03 | **Instalar antes de conexión** | Propietario PMGD |

---

## 7. CONCLUSIONES

1. El Parque Eólico Punta Negra (5 MW) puede conectarse a la barra 23 kV de S/E Litoral Norte sin restricciones de flujo de potencia ni de cortocircuito.
2. Los equipos existentes no requieren refuerzo.
3. **Condición suspensiva 1:** Instalar relé antipasivación (R02) antes de la puesta en servicio.
4. **Condición suspensiva 2:** Instalar relé diferencial de transformador (R03) antes de la puesta en servicio.
5. **Condición suspensiva 3:** Firma de acuerdo SITR con Cooperativa Eléctrica Litoral y aprobación del Coordinador.

---

## 8. RECOMENDACIONES

- Iniciar gestión del acuerdo SITR con la distribuidora de inmediato (puede tardar 30-60 días).
- Adquirir equipos de protección con al menos 60 días de anticipación a la puesta en servicio.
- Coordinar pruebas de integración SITR con el Coordinador con aviso >= 20 días.

**Documento emitido por CONECTA SpA bajo la responsabilidad del Ingeniero a cargo.**
