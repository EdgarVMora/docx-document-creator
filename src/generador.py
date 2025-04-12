"""
Módulo para la generación de documentos Word a partir de datos de árboles.
Utiliza python-docx para crear documentos estructurados con texto e imágenes.
"""

from docx import Document
from docx.shared import Inches
import os

def generar_documento(data, carpeta_imagenes, carpeta_salida):
    """
    Genera un documento Word con la información de un árbol.

    Args:
        data (dict): Diccionario con la información del árbol
        carpeta_imagenes (str): Ruta de la carpeta que contiene las imágenes
        carpeta_salida (str): Ruta donde se guardará el documento generado

    El documento incluye:
        - Título con el nombre del árbol
        - Descripción
        - Ubicación
        - Fecha
        - Imagen del árbol (si está disponible)
    """
    # Crear un nuevo documento
    doc = Document()
    
    # Agregar título principal
    doc.add_heading(f"Reporte del Árbol: {data['nombre']}", level=1)

    # Agregar información detallada con emojis para mejor visualización
    doc.add_paragraph(f"📝 Descripción: {data['descripcion']}")
    doc.add_paragraph(f"📍 Ubicación: {data['ubicacion']}")
    doc.add_paragraph(f"📅 Fecha: {data['fecha']}")

    # Procesar y agregar la imagen si existe
    imagen_path = os.path.join(carpeta_imagenes, data.get("imagen", ""))
    if os.path.exists(imagen_path):
        doc.add_picture(imagen_path, width=Inches(3.5))
    else:
        doc.add_paragraph("⚠️ Imagen no encontrada.")

    # Generar nombre del archivo de salida y guardar
    nombre_archivo = f"{data['id']}_{data['nombre'].replace(' ', '_')}.docx"
    output_path = os.path.join(carpeta_salida, nombre_archivo)
    doc.save(output_path)
    print(f"📄 Documento generado: {output_path}")