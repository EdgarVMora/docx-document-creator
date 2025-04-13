"""
Módulo de Utilidades para el Generador de Documentos de Árboles
Este módulo proporciona funciones y configuraciones comunes utilizadas en todo el proyecto.

Características principales:
- Sistema de logging centralizado
- Validación de imágenes y JSON
- Gestión de archivos y carpetas
- Generación de nombres únicos
"""

import os
import logging
from datetime import datetime
from typing import List, Dict, Union, Tuple
from PIL import Image

# Configuración del sistema de logging
# Establece dos handlers: uno para archivo (app.log) y otro para consola
# Formato: [Fecha y Hora] - [Nivel de Log] - Mensaje
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # Almacena logs en archivo
        logging.StreamHandler()          # Muestra logs en consola
    ]
)
logger = logging.getLogger(__name__)

# Definición de constantes para validación de imágenes
EXTENSIONES_PERMITIDAS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
TAMANO_MAXIMO = 10 * 1024 * 1024  # 10MB en bytes

# Dimensiones máximas permitidas según el tipo de imagen
DIMENSIONES_MAXIMAS = {
    'arboles': (2000, 2000),     # Imágenes principales de árboles
    'iconos': (500, 500),        # Iconos y miniaturas
    'templates': (3000, 3000)    # Plantillas y fondos
}

def validar_imagen(ruta_imagen: str, tipo: str = 'arboles') -> Tuple[bool, str]:
    """
    Valida una imagen según múltiples criterios de seguridad y calidad.

    Criterios de validación:
    1. Existencia del archivo
    2. Extensión permitida
    3. Tamaño máximo del archivo
    4. Dimensiones según el tipo de imagen

    Args:
        ruta_imagen (str): Ruta completa al archivo de imagen
        tipo (str): Tipo de imagen ('arboles', 'iconos', 'templates')

    Returns:
        Tuple[bool, str]: (es_valida, mensaje)
            - es_valida: True si la imagen cumple todos los criterios
            - mensaje: Descripción del resultado o error
    """
    try:
        if not os.path.exists(ruta_imagen):
            return False, f"El archivo no existe: {ruta_imagen}"

        extension = os.path.splitext(ruta_imagen)[1].lower()
        if extension not in EXTENSIONES_PERMITIDAS:
            return False, f"Extensión no permitida. Use: {EXTENSIONES_PERMITIDAS}"

        tamano = os.path.getsize(ruta_imagen)
        if tamano > TAMANO_MAXIMO:
            return False, f"Archivo demasiado grande. Máximo: {TAMANO_MAXIMO/1024/1024}MB"

        with Image.open(ruta_imagen) as img:
            ancho, alto = img.size
            max_ancho, max_alto = DIMENSIONES_MAXIMAS[tipo]
            if ancho > max_ancho or alto > max_alto:
                return False, f"Dimensiones exceden el máximo para {tipo}: {max_ancho}x{max_alto}"

        return True, "Imagen válida"
    except Exception as e:
        logger.error(f"Error al validar imagen {ruta_imagen}: {str(e)}")
        return False, f"Error al procesar la imagen: {str(e)}"

def validar_json(datos: Dict) -> Tuple[bool, str]:
    """
    Valida la estructura y contenido de un JSON de árbol.

    Validaciones:
    1. Campos requeridos presentes
    2. Formato de fecha válido (YYYY-MM-DD)
    3. Tipos de datos correctos
    4. Valores numéricos válidos (si existen)

    Args:
        datos (Dict): Diccionario con los datos del árbol

    Returns:
        Tuple[bool, str]: (es_valido, mensaje)
            - es_valido: True si el JSON es válido
            - mensaje: Descripción del resultado o error
    """
    campos_requeridos = ['id', 'nombre', 'descripcion', 'fecha']
    
    try:
        for campo in campos_requeridos:
            if campo not in datos:
                return False, f"Campo requerido faltante: {campo}"

        try:
            datetime.strptime(datos['fecha'], '%Y-%m-%d')
        except ValueError:
            return False, "Formato de fecha inválido. Use: YYYY-MM-DD"

        if 'altura_metros' in datos:
            try:
                float(datos['altura_metros'])
            except ValueError:
                return False, "La altura debe ser un número"

        return True, "JSON válido"
    except Exception as e:
        logger.error(f"Error al validar JSON: {str(e)}")
        return False, f"Error al validar JSON: {str(e)}"

def crear_carpetas_necesarias(rutas: List[str]) -> None:
    """Crea las carpetas necesarias si no existen"""
    for ruta in rutas:
        try:
            os.makedirs(ruta, exist_ok=True)
            logger.info(f"Carpeta creada/verificada: {ruta}")
        except Exception as e:
            logger.error(f"Error al crear carpeta {ruta}: {str(e)}")
            raise

def generar_nombre_archivo(nombre_base: str, extension: str) -> str:
    """Genera un nombre de archivo único"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nombre_limpio = ''.join(c for c in nombre_base if c.isalnum() or c in '-_')
    return f"{nombre_limpio}_{timestamp}{extension}"
