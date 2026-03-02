---
name: evaluating-distribution-compliance
description: Evalúa cumplimiento normativo CEN para coordinados de distribución y clientes coordinados. Usar cuando el usuario mencione "distribución", "empresa distribuidora", "cliente coordinado", "acceso a mediciones distribución" o "SITR distribución".
---

# Skill: Cumplimiento CEN — Distribución y Clientes Coordinados

## Cuándo usar este skill
- Coordinado es una empresa distribuidora o cliente coordinado
- Se revisan obligaciones SITR mediante enlace a red de distribución
- Se evalúa acceso a mediciones por seguridad y calidad de suministro
- Se verifica correcta gestión de enlaces vía distribuidora

## Workflow

```markdown
- [ ] Confirmar si coordinado es distribuidora o cliente coordinado
- [ ] Verificar cumplimiento SITR base (ver skill_base_sitr)
- [ ] Inventariar variables requeridas por el Coordinador
- [ ] Verificar enlace al sistema de comunicaciones de la distribuidora (si aplica)
- [ ] Verificar acceso a mediciones de seguridad y calidad de suministro
- [ ] Documentar acuerdos de enlace vigentes
- [ ] Identificar brechas y generar plan de acción
```

## Instrucciones

### 1. SITR para Distribución
Aplica todo lo definido en `skill_base_sitr.md` + variables específicas de red de distribución requeridas por el Coordinador.

### 2. Obligaciones Específicas

| Obligación | Descripción | Fuente |
|---|---|---|
| Variables en tiempo real | Tensiones, potencias y estados según requerimiento CEN | SITR dic-2019 |
| Enlace vía distribuidora | Para clientes coordinados conectados en red de distribución | AT-SITR-1 |
| Acceso a mediciones | Disponibilidad de medidas para seguridad y calidad (SEC/CEN) | NTSyCS mar-2025 |
| Disponibilidad | >= 99.5% mensual, igual que todos los coordinados | AT-SITR-1 |

### 3. Distinción entre Tipos de Coordinado

| Tipo | Enlace SITR | Variables típicas |
|---|---|---|
| Distribuidora | Directo al CEN | Tensiones barras MT, flujos, estados |
| Cliente coordinado (en red distribución) | Vía sistema de comunicaciones distribuidora | Variables según acuerdo con CEN |
| PMGD conectado en distribución | Vía distribuidora (ver skill_pmgd_pmg) | Mediciones de inyección y estado |

### 4. Requisitos de Acuerdos de Enlace
- Acuerdo formal entre coordinado (o cliente) y distribuidora para el enlace
- Diagrama de comunicaciones aprobado por el Coordinador
- Protocolo acordado (ICCP, DNP3, IEC 104)
- Aviso al Coordinador >= 30 días antes de cualquier cambio en acuerdo entre coordinados

## Fuentes Autorizadas
- SITR dic-2019: `documentos/fuentes/SITR-dic2019.pdf`
- AT-SITR-1 mar-2025: `documentos/fuentes/AT-SITR-1-mar2025.pdf`
- NTSyCS mar-2025: `documentos/fuentes/NTSyCS-Mar-2025.pdf`

## Checklists
- `documentos/checklists/checklist_distribucion_clientes.md`
- `documentos/checklists_xlsx/checklist_distribucion_clientes.xlsx`

## Salida Esperada
- Diagnóstico de cumplimiento distribución/clientes con tabla de brechas
- Verificación de acuerdos y diagramas de enlace vigentes
