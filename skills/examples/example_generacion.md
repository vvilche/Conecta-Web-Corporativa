# Ejemplo: Cumplimiento PMUS — Central Solar 60 MW

**Skill utilizada:** `skill_generacion`
**Tipo de coordinado:** Generación solar fotovoltaica >= 9 MW

---

## Inputs del caso

- Empresa: Energía Desierto S.A.
- Central: Parque Solar Atacama, 60 MW (6 inversores de 10 MW c/u)
- Estado: PMU instalada, primer año de operación como coordinado
- PDC: Local instalado en S/E de la central

---

## Verificación PMUS

| Req. | Parámetro | Estado actual | Estado |
|---|---|---|---|
| P >= 9 MW → PMU | 60 MW — incluida en MMF 2025 | PMU SEL-425 instalada | ✅ OK |
| Clase M-Class | M-Class | Certificado fabricante | ✅ OK |
| 50 muestras/s | 50 mps | Configurado | ✅ OK |
| IEEE C37.118 | Protocolo | Configurado | ✅ OK |
| GPS/IRIG-B, precisión 1 µs | GPS Trimble | Calibrado oct-2024 | ✅ OK |
| Segundo enlace | Requerido | ✅ MPLS + fibra respaldo | ✅ OK |
| Alimentación >= 8 h | UPS + banco baterías | UPS 12 h certificado | ✅ OK |
| Ancho de banda >= 120 kbps | 512 kbps disponibles | Cálculo presentado al CEN | ✅ OK |
| Dossier PES | Completo | Rev. 2, dic-2024 | ✅ OK |
| Checklist PMUS anual | Plazo 31 julio | Realizada jul-2024 | ✅ OK |

---

## SITR Base

| Parámetro | Requisito | Valor | Estado |
|---|---|---|---|
| Disponibilidad SITR | >= 99.5% | 99.7% | ✅ |
| Edad de datos | <= 5 s | 2 s | ✅ |
| Respaldo SITR | >= 6 h | UPS 12 h | ✅ |
| GPS (sync SITR) | +/- 100 µs | Misma unidad GPS | ✅ |

---

## Tabla de Brechas

| ID | Brecha | Criticidad |
|---|---|---|
| G01 | Checklist PMUS 2025 aún no realizada (plazo 31-jul-2025) | 🟡 Planificar |

---

## Conclusión
✅ Central cumple **completamente** con sus obligaciones de generación coordinada. Solo pendiente la checklist PMUS 2025 (plazo julio). Caso modelo de cumplimiento full.
