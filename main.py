"""
Script principal para la generación de documentos de árboles.
Este módulo coordina la carga de archivos JSON y la generación de documentos Word.
"""

import json
import os
from src.generador import generar_documento

# Definición de rutas principales del proyecto
CARPETA_ENTRADA = "entrada"    # Carpeta donde se encuentran los archivos JSON
CARPETA_IMAGENES = "imagenes"  # Carpeta donde se almacenan las imágenes de los árboles
CARPETA_SALIDA = "salida"      # Carpeta donde se guardarán los documentos generados

def cargar_jsons(carpeta):
    """
    Carga todos los archivos JSON de una carpeta especificada.
    
    Args:
        carpeta (str): Ruta de la carpeta que contiene los archivos JSON
        
    Returns:
        list: Lista de diccionarios con la información de cada árbol
    """
    archivos = [f for f in os.listdir(carpeta) if f.endswith('.json')]
    datos = []
    for archivo in archivos:
        with open(os.path.join(carpeta, archivo), 'r', encoding='utf-8') as f:
            datos.append(json.load(f))
    return datos

def main():
    """
    Función principal que coordina el proceso de generación de documentos.
    Lee los archivos JSON y genera un documento Word para cada árbol.
    """
    # Cargar todos los datos de los árboles
    arboles = cargar_jsons(CARPETA_ENTRADA)
    
    # Generar un documento para cada árbol
    for arbol in arboles:
        generar_documento(arbol, CARPETA_IMAGENES, CARPETA_SALIDA)

if __name__ == "__main__":
    main()