"""
Agente Analista Espacial (El Geógrafo).
Este agente tiene como propósito planificar la ingesta de datos y usar scripts 
con GeoPandas y Shapely.
"""
from typing import Dict, Any
# from langchain.chat_models import init_chat_model
# from tools.spatial_tools import get_demographics_in_radius, calculate_isochrone

class GeographerAgent:
    def __init__(self, llm_model: str = "gpt-4o"):
        self.llm_model = llm_model
        # self.llm = init_chat_model(self.llm_model)
        # self.tools = [get_demographics_in_radius, calculate_isochrone]
        self.system_prompt = \"\"\"
        Eres un experto analista espacial (Geógrafo).
        Recibes coordenadas y tu objetivo es ejecutar cruces de variables sobre
        nuestra base de datos PostGIS empleando GeoPandas.
        Devuelve el análisis descriptivo de las isócronas y buffers solicitados.
        \"\"\"

    def process_query(self, query: str) -> Dict[str, Any]:
        """TBD: Llama a Langchain y ejecuta la herramienta adecuada."""
        print(f"[Agente Geógrafo] Recibiendo tarea: {query}")
        return {"analisis": "El polígono solicitado intersecta con 400 manzanas de NSE Alto."}
