# Fuentes de Datos Abiertos: Flujo Peatonal y Movilidad en Chile

Para alimentar la toma de decisiones del **AgenteGeo**, la medición del flujo de personas (población flotante y movilidad) es crítica. Tras investigar el estado de los datos abiertos y APIs en Chile, estas son las fuentes y metodologías disponibles actualmente:

## 1. APIs de Transporte Público (Ministerio de Transportes / DTPM)
Aunque no cuentan personas caminando unívocamente, las APIs de movilidad son el mejor proxy en tiempo real del flujo masivo:
*   **Directorio de Transporte Público Metropolitano (DTPM):** Poseen un portal de datos abiertos que expone *Web Services* (API) con el posicionamiento GPS de toda la flota de buses de Santiago (Red) en tiempo real y alertas operacionales.
*   **Datos GTFS (Transapp / MTT):** Gran parte de las ciudades de Chile (Antofagasta, Gran Concepción, Santiago) tienen su matriz de viajes públicos estandarizada en formato GTFS. AgenteGeo puede consumir esta API para saber exactamente qué esquinas concentran los mayores transbordos y a qué horas.

## 2. Población Flotante y Turismo (Sernatur / Censo)
Para estimar cuánta gente "visita" o "trabaja" en una zona durante el día vs. la gente que "duerme" ahí de noche:
*   **Sernatur y Subdere:** Publican estimaciones de "Población Flotante" por comuna, que se usan para la distribución del Fondo Común Municipal.
*   **Datos Censo 2017 (INE):** El Censo chileno tiene una matriz de conmutación origen-destino (Preguntas: "¿En qué comuna vive?" vs "¿En qué comuna trabaja/estudia?"). Cruzando este cruce matricial se pueden modelar los flujos pendulares diarios por comuna.

## 3. Mapas de Calor Institucionales (Gobierno Regional Santiago)
El Gobierno Regional Metropolitano y municipalidades específicas (ej. Plan Integral de Movilidad de Stgo Centro) realizan forzadamente conteos manuales o por cámaras de los flujos peatonales. Por ejemplo, han publicado datos que indican que corredores como Huérfanos o Ahumada mueven sobre 30.000 peatones diarios. Si bien estos datos no suelen estar en una API en tiempo real, suelen publicarse en repositorios CSV estáticos en plataformas como `datos.gob.cl`.

## 4. Opciones Privadas (Altamente recomendadas en la industria)
Dado que el gobierno chileno modela el flujo peatonal granular para infraestructura (lento y con desfase), el mercado comercial suele apoyarse en APIs privadas que "venden" data agregada y anonimizada de celulares:
*   **Data de Telcos (Entel Ocean, Movistar LUCA):** Poseen modelos geográficos casi en tiempo real de densidad poblacional cruzando las cuadrículas de las antenas celulares.
*   **APIs Globales (Foursquare / Google Places):** La API de *Google Places* o *Foursquare Places* expone el atributo `popular_times` o `foot_traffic`. AgenteGeo podría enviar un requerimiento a esta API solicitando el tráfico del "Mall Costanera Center" y obtener la curva de tráfico del día.

### Conclusión para AgenteGeo
Para el MVP, la estrategia más realista y gratuita es:
1. Usar el **Censo INE 2017/2024** para la población residente.
2. Usar **APIs de Transporte del DTPM (GTFS)** para identificar nodos de alto tránsito (paraderos, metro).
3. Complementar extrapolando zonas con algoritmos de Machine Learning hasta poder integrar APIs privadas de flujo como Foursquare.
