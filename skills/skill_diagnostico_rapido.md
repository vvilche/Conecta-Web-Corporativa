---
name: diagnosing-coordinado-type
description: Realiza el diagnóstico inicial y triage de cualquier coordinado para derivar al skill correcto. Usar cuando el usuario mencione un nuevo coordinado, inicio de proyecto, "qué obligaciones tengo", "soy empresa X" o "por dónde empiezo".
---

# Skill: Diagnóstico Rápido — Identificación de Coordinado

> ⚡ **Usar este skill SIEMPRE al iniciar** cualquier análisis. Identifica el tipo de coordinado y activa las skills correctas.

## Cuándo usar este skill
- Usuario presenta un nuevo cliente o proyecto
- Usuario pregunta "¿qué obligaciones tenemos?"
- Se inicia un diagnóstico de cumplimiento desde cero
- No está claro qué tipo de coordinado es el cliente

## Workflow

```markdown
- [ ] Solicitar nombre y descripción de la empresa/proyecto
- [ ] Identificar tipo de coordinado según criterios de clasificación
- [ ] Verificar si tiene obligaciones SITR (todos los coordinados)
- [ ] Identificar skills adicionales por tipo específico
- [ ] Confirmar con el usuario la clasificación
- [ ] Emitir hoja de ruta personalizada
```

## Instrucciones

### 1. Preguntas de Clasificación Inicial

Formular al usuario:
1. **¿Qué tipo de instalación opera?** (central generadora / línea de transmisión / red de distribución / PMGD / cliente industrial conectado en AT)
2. **¿Cuál es la potencia instalada?** (para determinar umbrales PMUS, PMGD, PMG)
3. **¿A qué tensión está conectado al SEN?** (AT, MT, BT)
4. **¿Tiene contratos o comunicaciones previas con el CEN?**
5. **¿Presta algún Servicio Complementario?** (regulación, reserva, etc.)
6. **¿Tiene esquemas EDAC, EDAG o ERAG configurados?**

### 2. Árbol de Clasificación

```
¿Opera instalaciones en el SEN?
├─► SÍ → ¿Qué tipo?
│         ├─► GENERACIÓN
│         │   ├─► P >= 9 MW → Coordinado generación + PMUS aplica
│         │   └─► P < 9 MW  → Posible PMGD (ver abajo)
│         │
│         ├─► TRANSMISIÓN (líneas STN/STE/STR)
│         │   └─► Coordinado transmisión + MMF aplica
│         │
│         ├─► DISTRIBUCIÓN (concesionaria distribución)
│         │   └─► Coordinado distribución
│         │
│         ├─► PMGD (P <= 9 MW, conectado en red distribución)
│         │   └─► Coordinado PMGD/PMG
│         │
│         └─► SSCC (presta regulación, reserva, etc.)
│             └─► Coordinado SSCC (además de su tipo base)
│
└─► ¿Tiene EDAC/EDAG/ERAG? → SÍ → Agregar skill EDAC a cualquier tipo
```

### 3. Tabla de Skills por Tipo de Coordinado

| Tipo de Coordinado | Skill Base | Skills Adicionales | Skills Ingeniería |
|---|---|---|---|
| **Generación >= 9 MW** | skill_base_sitr | skill_generacion | skill_estudio_ecap |
| **Generación < 9 MW (PMGD)** | skill_base_sitr | skill_pmgd_pmg | skill_estudio_ecap |
| **Transmisión STN** | skill_base_sitr | skill_transmision | skill_calculo_cortocircuito |
| **Distribución** | skill_base_sitr | skill_distribucion_clientes | skill_revision_planos |
| **PMGD/PMG** | skill_base_sitr | skill_pmgd_pmg | skill_estudio_ecap |
| **SSCC** | skill_base_sitr | skill_sscc | — |
| **Con EDAC/EDAG/ERAG** | + skill_edac_edag_erag | (combinable con cualquiera) | skill_coordinacion_protecciones |

### 4. Hoja de Ruta de Diagnóstico — Plantilla de Salida

```markdown
## Diagnóstico Inicial — [Nombre empresa]

**Tipo de coordinado:** [Generación / Transmisión / Distribución / PMGD / SSCC]
**Potencia instalada:** [XX MW]
**Punto de conexión:** [Subestación X, tensión Y kV]
**Esquemas especiales:** [EDAC/EDAG/ERAG: Sí/No]
**SSCC prestados:** [Sí → cuáles / No]

### Skills a aplicar (en orden):
1. ✅ skill_base_sitr → Obligatorio siempre
2. ✅ skill_[tipo] → Por tipo de coordinado
3. [✅/—] skill_edac_edag_erag → Si aplica
4. [✅/—] skill_sscc → Si presta SSCC
5. ✅ skill_estudio_ecap → Si necesita estudio de conexión

### Prioridades iniciales:
- 🔴 Urgente: [X, Y]
- 🟠 Mediano plazo: [Z]
- 🟡 Planificación anual: [W]
```

## Errores Comunes
- ❌ Clasificar como "solo distribución" a una empresa que también presta SSCC
- ❌ Olvidar que un PMGD conectado en distribución igualmente tiene obligaciones SITR con el CEN
- ❌ No preguntar por potencia: un generador de 8 MW no necesita PMUS; uno de 9 MW sí

## Fuentes
- [README.md](README.md) — Índice completo de skills
- `skill_base_sitr.md` → Obligaciones comunes a todos

## Salida Esperada
- Clasificación confirmada del coordinado
- Lista de skills a aplicar en orden
- Hoja de ruta de diagnóstico personalizada
