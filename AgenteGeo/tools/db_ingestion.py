import os
import requests
import zipfile
import geopandas as gpd
from sqlalchemy import create_engine
from langchain.tools import tool

# Configuramos la conexión a tu base de datos PostGIS local o en la nube
DB_USER = "postgres"
DB_PASS = "tu_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "geomarketing_cl"

ENGINE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

@tool("ingestar_datos_postgis")
def ingestar_datos_postgis(url: str, nombre_tabla: str, es_zip: bool = False) -> str:
    """
    Descarga un archivo espacial (GeoJSON o un Shapefile comprimido en ZIP) 
    desde una URL y lo inserta automáticamente en la base de datos PostGIS.
    Parámetros:
    - url: Link directo al archivo de IDE Chile, INE, etc.
    - nombre_tabla: Cómo se llamará la tabla en PostGIS (ej. 'manzanas_ine').
    - es_zip: True si la URL descarga un archivo .zip (muy común en Shapefiles).
    """
    try:
        # 1. Descargar el archivo
        print(f"Descargando datos desde {url}...")
        respuesta = requests.get(url)
        archivo_temporal = "temp_data" + (".zip" if es_zip else ".geojson")
        
        with open(archivo_temporal, "wb") as f:
            f.write(respuesta.content)
            
        # 2. Leer el archivo con GeoPandas
        if es_zip:
            # Si es ZIP, GeoPandas puede leerlo directamente pasándole el protocolo vfs
            filepath = f"zip://{archivo_temporal}"
        else:
            filepath = archivo_temporal
            
        print("Cargando archivo espacial en memoria...")
        gdf = gpd.read_file(filepath)
        
        # 3. Estandarizar Sistema de Coordenadas (Crucial en Chile)
        # Chile suele usar EPSG:32719 (UTM 19S) o EPSG:5361 (SIRGAS). 
        # Lo pasamos a EPSG:4326 (Lat/Lon estándar) para compatibilidad web.
        if gdf.crs and gdf.crs.to_epsg() != 4326:
            gdf = gdf.to_crs(epsg=4326)
            
        # 4. Conectar a PostGIS e Insertar
        print(f"Insertando {len(gdf)} registros en la tabla '{nombre_tabla}' de PostGIS...")
        engine = create_engine(ENGINE_URL)
        
        # to_postgis requiere geoalchemy2 instalado
        gdf.to_postgis(
            name=nombre_tabla,
            con=engine,
            if_exists='replace', # Puede ser 'append' para agregar
            index=False,
            geometry_name='geom' # Estándar de PostGIS
        )
        
        # Limpieza de temporales
        os.remove(archivo_temporal)
        
        return f"¡Éxito! La tabla '{nombre_tabla}' con {len(gdf)} registros geométricos está lista en PostGIS."
        
    except Exception as e:
        return f"Error al procesar los datos: {str(e)}"
