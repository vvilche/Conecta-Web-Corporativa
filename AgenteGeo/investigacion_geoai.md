# Estado del Arte: Agentes Geoespaciales (GeoAI) y LLMs en GIS

La integración de Agentes Autónomos (basados en LLMs) con Sistemas de Información Geográfica (GIS) es una de las áreas de investigación más activas ("GeoAI"). A continuación, presento un resumen de lo que existe actualmente en el mercado y en la academia, lo cual valida fuertemente la dirección de nuestro proyecto **AgenteGeo**.

## 1. ¿Qué son los Agentes Geoespaciales (LLM for GIS)?
A diferencia de los asistentes de texto tradicionales, un "GeoAI Agent" es un sistema capaz de:
*   **Razonamiento Espacial**: Comprender conceptos de cercanía, intersección, buffers y topología a partir de lenguaje natural.
*   **Tool Calling sobre GIS**: Traducir preguntas como *"¿Cuánta gente vive a 15 min de esta coordenada?"* en scripts ejecutables de Python (GeoPandas, Shapely) o consultas SQL espaciales (PostGIS/GeoAlchemy2).
*   **Descubrimiento Autónomo**: Buscar y descargar capas vectoriales de internet de forma autónoma (ej. conectarse a la API del INE o IDE Chile) cuando el LLM determina que le falta contexto.

## 2. Herramientas y Casos de Éxito Actuales

A nivel global, la comunidad open-source y empresas de software ya están lanzando agentes enfocados netamente en el espacio:

*   **GIS Copilot (Integraciones con QGIS/ArcGIS)**: Existen plugins experimentales donde el usuario interactúa mediante chat dentro de QGIS. El agente LLM internamente genera el código PyQGIS o ArcPy para aplicar geoprocesos automatizados sobre el lienzo del usuario.
*   **LLM-Find & Data Discovery Agents**: Agentes entrenados específicamente para explorar catálogos de metadatos espaciales. Si les pides "mapa de pobreza de Santiago", el agente navega servicios WFS/WMS públicos, descarga el Shapefile y lo estandariza.
*   **Plataformas Nativas de Cartografía AI (ej. CARTO, Felt)**: Grandes players de *Location Intelligence* están agregando capas de IA donde puedes seleccionar un polígono y pedirle en texto plano "Cruza esto con la red de transporte y dime el riesgo de inundación", y la plataforma orquesta los modelos matemáticos por detrás.
*   **Agentes de Ruteo y Logística**: Sistemas MAS (Multi-Agent Systems) donde decenas de agentes representan vehículos de reparto, negociando rutas óptimas en tiempo real en base a matrices de isócronas e información de tráfico de APIs (como OSRM o Google Maps).

## 3. ¿Cómo se posiciona nuestro AgenteGeo?

Lo que estamos construyendo con **AgenteGeo** está **en la frontera tecnológica actual**. 

Mientras que muchas herramientas (como ChatGPT Advanced Data Analysis) pueden escupir un mapa estático si le pasas un CSV, nuestro enfoque con **LangGraph** (donde separamos un Minero, un Geógrafo y un Científico de Datos conectados a nuestra propia Base de Datos PostGIS de Chile) es la arquitectura correcta, conocida como **Multi-Agent Orchestration for GIS**.

**Ventajas de nuestro enfoque sobre soluciones enlatadas:**
1.  **Contexto Local**: Tendremos las capas chilenas (SII, INE) directamente en la base de datos (PostGIS), no dependemos de que el LLM alucine datos demográficos.
2.  **Seguridad**: Al usar LangGraph, podemos poner validadores (Human-in-the-loop) antes de que el agente ejecute una query destructiva en SQL o asuma un dato erróneo para una consultoría de expansión comercial millonaria.
