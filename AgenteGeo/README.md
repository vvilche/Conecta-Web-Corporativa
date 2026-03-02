# AgenteGeo - Consultor Autónomo de Geomarketing (Chile)

Un ecosistema multi-agente diseñado para consultar bases de datos espaciales (IDE, SII, INE), cruzar variables demográficas, calcular isócronas y ejecutar modelos de Machine Learning para definir localizaciones óptimas comerciales y realizar *Lookalikes* geográficos en todo Chile.

## Estructura del Proyecto

*   `api/`: Interfaz para exponer el agente o conectar a aplicaciones externas.
*   `core/`: Definición de grafos y lógica principal del orquestador (LangGraph/CrewAI).
*   `agents/`: Definiciones específicas de comportamiento, prompts y LLMs de cada agente.
    *   Gestor de Datos (Minero).
    *   Analista Espacial (Geógrafo).
    *   Científico de Datos.
    *   Consultor Estratégico.
*   `tools/`: Herramientas ejecutables que los agentes invocan para sus tareas. Contiene scripts de GIS.
*   `db/`: Modelos de bases de datos, conexión a PostgreSQL/PostGIS y scripts ETL.

## Próximos pasos (Fase 1)
Descargar microdatos cartográficos (Censo 2017) e información fiscal del SII para el piloto en Santiago de Chile.
