# Inteligencia de Mercado — S/E Distribución 23 kV en Riesgo PMUS

## ¿Qué buscar?
Subestaciones de distribución 23 kV donde la **suma de potencia de todos los PMGD
conectados ≥ 20 MW**, lo que activa la obligación de PMUS (Unidades Sincrofasoras)
para todos los generadores de esa S/E según la **NTSyCS Cap. 6**.

## Fuente: Informe CEN Mayo 2024
El Coordinador Eléctrico Nacional publicó en mayo 2024 el estudio
**"Verificación de Posibles Congestiones en Instalaciones de Transmisión Zonal por Inyección de PMGD"**
(art. 3-45 NTCO PMGD):

| Hallazgo | Dato |
|---|---|
| Transformadores AT/MT congestionados | **63** |
| Subestaciones afectadas | **55** |
| Transformadores con inversión de flujo | **95** |
| S/E con obras de expansión en curso | 14 |
| Concentración geográfica | Coquimbo → Maule (71,5% del total PMGD) |
| Tecnología dominante | Solar FV (82%) |

> 📄 **Fuente**: Informe CEN mayo 2024 — disponible en coordinador.cl (requiere acceso portal coordinados)

## Zonas de Mayor Riesgo PMUS (por concentración PMGD)

### 🔴 CRÍTICO — Región del Maule (más congestionada del SEN)
| Subestación | Distribuidora | PMGD estimados |
|---|---|---|
| S/E Talca Norte | CGE | 4-6 parques solares |
| S/E Curicó | CGE / Chilquinta | Alta concentración agrícola solar |
| S/E Linares | CGE | Zona vitícola saturada |
| S/E Cauquenes | CGE | Pipeline activo 2024-2025 |

### 🔴 CRÍTICO — Región de O'Higgins
| Subestación | Distribuidora | Situación |
|---|---|---|
| S/E Santa Cruz | CGE | Valle Colchagua — alta penetración solar |
| S/E San Fernando | CGE | Múltiples PMGD en construcción |
| S/E Rancagua Sur | Enel | Area industrial + agrícola |

### 🟡 EN LÍMITE — Región Metropolitana (23 kV Enel Distribución)
| Subestación | Distribuidora | Situación |
|---|---|---|
| **S/E Maipo Norte** | Enel | ⚠️ 12 MW existentes + 8 MW proyecto = **20 MW exacto** |
| S/E Buin | Enel | Pipeline activo zona sur RM |
| S/E Talagante | Enel | Saturación en curso |
| S/E Melipilla | Enel | Múltiples PMGD rurales |
| S/E San Bernardo | Enel | Alta densidad urbano-rural |

### 🟡 EN LÍMITE — Región de Coquimbo
| Subestación | Distribuidora | Situación |
|---|---|---|
| S/E Ovalle | CGE Norte | Cuenca Limarí — solar intensivo |
| S/E La Serena Sur | CGE Norte | Expansión descontrolada 2022-24 |
| S/E Illapel | CGE Norte | Zona en límite conocido |

### 🟡 EN LÍMITE — Región de Valparaíso
| Subestación | Distribuidora | Situación |
|---|---|---|
| S/E San Antonio | Chilquinta | Costa — solar + eólico |
| S/E Casablanca | Chilquinta | Alta penetración solar |
| S/E Quillota | Chilquinta | Zona agroindustrial saturada |

## Cómo Confirmar el Estado Real de una S/E

### Paso 1 — Portal coordinados.cl (acceso coordinado registrado)
```
coordinador.cl → Mercados → Documentos → Normas y procedimientos
→ Informe MMF vigente (actualización Q1 cada año)
```

### Paso 2 — Verificar en Sistema MGEN del CEN
El MGEN (Módulo de Generación) permite consultar qué instalaciones están conectadas
a cada S/E y su potencia nominal. Acceso con credenciales de coordinado.

### Paso 3 — Solicitud directa al CEN
Via formulario de consulta técnica → CEN debe responder en 15 días hábiles.
Preguntar: "¿La S/E [nombre] aparece en el MMF vigente como zona PMUS obligada?"

## Oportunidad Comercial CONECTA INGENIERIA
Las S/E cerca del umbral representan la oportunidad más urgente:

| Situación | Nº S/E estimadas | Ticket promedio | Urgencia |
|---|---|---|---|
| S/E YA sobre 20 MW (sin saberlo) | ~20-25 S/E | USD 8.000-15.000 / PMGD | **INMEDIATA** |
| S/E en 15-20 MW (próximas) | ~30-40 S/E | USD 5.000-10.000 prevención | Alta |
| S/E en 10-15 MW (pipeline) | ~50+ S/E | Asesoría temprana | Media |

> 💡 **Acción recomendada**: CONECTA INGENIERIA puede ofrecer un servicio de
> "diagnóstico PMUS" a precio fijo (USD 3.500-5.000) para verificar si una S/E
> está en el MMF vigente y qué deben hacer los PMGDs antes de su COD.

## Metodología de Priorización
Para identificar las S/E más urgentes:
1. Cruzar lista de PMGDs en construcción (permisos SEC) con S/E de conexión
2. Consultar informe MMF Q1-2025 en portal coordinados
3. Priorizar S/E donde hay PMGD en fase pre-COD (máxima urgencia)
4. Contactar directamente a los propietarios de PMGDs afectados

## Referencias cruzadas
- [NTCO PMGD 2026](../CNE/NTCO_PMGD_2026.md) — obligaciones PMUS
- [NTSyCS 2026](../CNE/NTSyCS_2026.md) — Cap. 6 base normativa PMUS
- [CEN — PMUS/MMF](./PMUS_MMF.md) — instrucciones del coordinador
