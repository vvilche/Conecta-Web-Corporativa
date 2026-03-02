# Ejemplo: Revisión de Plano Unifilar — Ampliación Planta Industrial

**Skill utilizada:** `skill_revision_planos`
**Tipo de plano:** Diagrama unifilar eléctrico, ampliación tablero BT
**N° Plano:** E-IND-2025-003, Rev. 0

---

## Datos del Plano Revisado

- Proyecto: Ampliación planta procesadora acuícola, Puerto Montt
- Plano: Diagrama unifilar tablero general BT (TGBT) ampliado
- Revisión recibida: Rev. 0 (primera emisión borrador)
- Fecha de revisión: 2025-02-20
- Revisado por CONECTA: Equipo ingeniería

---

## Información del Plano (Verificación Documental)

| Elemento | Estado |
|---|---|
| Título del plano | ✅ Presente |
| Número de plano | ✅ E-IND-2025-003 |
| Revisión y fecha | ✅ Rev. 0, 2025-02-12 |
| Escala | ✅ "Sin escala" indicado |
| Firma proyectista | ❌ Falta firma del proyectista |
| Cuadro de revisiones | ⚠️ Solo tiene Rev. 0, formato incompleto |
| Leyenda de simbología | ✅ Presente |
| Notas generales | ❌ Ausente |

---

## Lista de Comentarios (RFI)

| N° | Ref. Plano | Área | Observación | Norma | Categoría | Estado |
|---|---|---|---|---|---|---|
| 001 | E-IND-003 | Portada | Falta firma del proyectista eléctrico responsable | NCh Elec 4, Art. 5 | 🟠 Mayor | Abierto |
| 002 | E-IND-003 | General | Ausencia de notas generales (tensión nominal, normas aplicables, empresa) | — | 🟡 Menor | Abierto |
| 003 | E-IND-003 | Q-12 (nuevo) | Interruptor diferencial de 300 mA en circuito de alumbrado de área húmeda — debe ser 30 mA | NCh Elec 4, Sec. 701 | 🔴 Crítico | Abierto |
| 004 | E-IND-003 | Barra BT | Calibre del conductor de neutro no indicado en alimentador principal | IEC 60364-5-54 | 🟠 Mayor | Abierto |
| 005 | E-IND-003 | Q-08 | Potencia del motor indicada en HP en lugar de kW (deben usarse unidades SI) | — | 🟡 Menor | Abierto |
| 006 | E-IND-003 | Sistema tierra | No se indica resistencia de tierra de diseño, ni método de cálculo | NCh Elec 4, Sec. 9 | 🟠 Mayor | Abierto |
| 007 | E-IND-003 | Q-15 | Interruptor magnetotérmico 63A en circuito con cable 35 mm²; protección sobredimensionada (cable admite 125A) — correcto si es funcional, confirmar | IEC 60364-4-43 | 🟡 Menor | Por aclarar |

---

## Estado de Revisión

| Código | Significado | Resultado |
|---|---|---|
| **A** | Aprobado | — |
| **B** | Aprobado con comentarios | — |
| **C** | **Rechazado — Corregir y re-enviar** | ✅ Aplica |
| **D** | Para información | — |

**Estado asignado: C — Rechazado**

**Motivo principal:** OBS-003 (diferencial 300 mA en área húmeda) es un error de seguridad crítico que impide la aprobación. Adicionalmente OBS-001 (falta firma) es un requisito documental indispensable.

---

## Próximos Pasos

1. Proyectista corrige OBS-001 a OBS-007
2. Re-emite plano como Rev. 1
3. CONECTA realiza segunda revisión (objetivo: código A o B)
4. Estimado para re-revisión: 5 días hábiles desde re-emisión
