import os
import shutil
from PIL import Image
import uuid
from datetime import datetime

class ManejadorImagenes:
    """
    Clase para manejar el procesamiento y almacenamiento de imágenes
    """
    
    def __init__(self, carpeta_base="imagenes"):
        self.carpeta_base = carpeta_base
        self.carpeta_arboles = os.path.join(carpeta_base, "arboles")
        self.carpeta_iconos = os.path.join(carpeta_base, "iconos")
        self.carpeta_templates = os.path.join(carpeta_base, "templates")
        
        # Crear las carpetas si no existen
        for carpeta in [self.carpeta_arboles, self.carpeta_iconos, self.carpeta_templates]:
            os.makedirs(carpeta, exist_ok=True)
    
    def procesar_imagen_desde_json(self, datos_imagen, tipo="iconos", tamano_max=None):
        """
        Procesa una imagen desde los datos del JSON
        
        Args:
            datos_imagen: Diccionario con información de la imagen
            tipo: Tipo de imagen (arboles, iconos, templates)
            tamano_max: Tupla (ancho, alto) para redimensionar
            
        Returns:
            dict: Información actualizada de la imagen
        """
        if not datos_imagen or 'ruta' not in datos_imagen:
            return datos_imagen

        ruta_original = datos_imagen['ruta']
        
        # Si la imagen ya está en nuestra estructura, la validamos
        if self.es_ruta_valida(ruta_original):
            return datos_imagen
            
        # Si es una ruta externa, la procesamos
        if os.path.exists(ruta_original):
            nueva_ruta = self.guardar_imagen(ruta_original, tipo, tamano_max)
            datos_imagen['ruta'] = os.path.relpath(nueva_ruta, self.carpeta_base)
            
        return datos_imagen
    
    def es_ruta_valida(self, ruta):
        """
        Verifica si una ruta de imagen ya está en nuestra estructura
        """
        ruta_completa = os.path.join(self.carpeta_base, ruta)
        return os.path.exists(ruta_completa) and any([
            ruta.startswith(tipo + "/") 
            for tipo in ["arboles", "iconos", "templates"]
        ])
    
    def guardar_imagen(self, imagen_path, tipo="arboles", tamano_max=None):
        """
        Guarda una imagen en la carpeta correspondiente
        
        Args:
            imagen_path: Ruta de la imagen a guardar
            tipo: Tipo de imagen (arboles, iconos, templates)
            tamano_max: Tupla (ancho, alto) para redimensionar
            
        Returns:
            str: Ruta donde se guardó la imagen
        """
        # Verificar que el archivo existe
        if not os.path.exists(imagen_path):
            raise FileNotFoundError(f"No se encontró la imagen: {imagen_path}")
            
        # Verificar que es una imagen válida
        try:
            with Image.open(imagen_path) as img:
                # Redimensionar si es necesario
                if tamano_max and (img.width > tamano_max[0] or img.height > tamano_max[1]):
                    img.thumbnail(tamano_max)
                
                # Generar nombre único para la imagen
                extension = os.path.splitext(imagen_path)[1].lower()
                nuevo_nombre = f"{datetime.now().strftime('%Y%m%d')}_{str(uuid.uuid4())[:8]}{extension}"
                
                # Determinar carpeta destino
                if tipo == "arboles":
                    carpeta_destino = self.carpeta_arboles
                elif tipo == "iconos":
                    carpeta_destino = self.carpeta_iconos
                elif tipo == "templates":
                    carpeta_destino = self.carpeta_templates
                else:
                    raise ValueError(f"Tipo de imagen no válido: {tipo}")
                
                # Ruta completa del destino
                ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
                
                # Guardar la imagen optimizada
                img.save(ruta_destino, optimize=True, quality=85)
                
                return ruta_destino
                
        except Exception as e:
            raise ValueError(f"Error al procesar la imagen: {str(e)}")
    
    def obtener_imagen(self, nombre, tipo="arboles"):
        """
        Obtiene la ruta de una imagen almacenada
        
        Args:
            nombre: Nombre de la imagen
            tipo: Tipo de imagen (arboles, iconos, templates)
            
        Returns:
            str: Ruta completa de la imagen
        """
        if tipo == "arboles":
            carpeta = self.carpeta_arboles
        elif tipo == "iconos":
            carpeta = self.carpeta_iconos
        elif tipo == "templates":
            carpeta = self.carpeta_templates
        else:
            raise ValueError(f"Tipo de imagen no válido: {tipo}")
            
        ruta = os.path.join(carpeta, nombre)
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No se encontró la imagen: {ruta}")
            
        return ruta
    
    def listar_imagenes(self, tipo="arboles"):
        """
        Lista todas las imágenes de un tipo específico
        
        Args:
            tipo: Tipo de imagen (arboles, iconos, templates)
            
        Returns:
            list: Lista de nombres de imágenes
        """
        if tipo == "arboles":
            carpeta = self.carpeta_arboles
        elif tipo == "iconos":
            carpeta = self.carpeta_iconos
        elif tipo == "templates":
            carpeta = self.carpeta_templates
        else:
            raise ValueError(f"Tipo de imagen no válido: {tipo}")
            
        return [f for f in os.listdir(carpeta) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    def procesar_imagenes_json(self, datos_json):
        """
        Procesa todas las imágenes en un JSON
        
        Args:
            datos_json: Diccionario con datos del árbol genealógico
            
        Returns:
            dict: JSON actualizado con las rutas de imágenes procesadas
        """
        # Procesar imagen principal
        if 'imagen_principal' in datos_json:
            datos_json['imagen_principal'] = self.procesar_imagen_desde_json(
                datos_json['imagen_principal'],
                'arboles',
                (1200, 800)  # Tamaño máximo para imagen principal
            )
        
        # Procesar imágenes de miembros
        if 'miembros' in datos_json:
            for miembro in datos_json['miembros']:
                if 'imagen' in miembro:
                    miembro['imagen'] = self.procesar_imagen_desde_json(
                        miembro['imagen'],
                        'iconos',
                        (300, 300)  # Tamaño máximo para iconos
                    )
        
        # Procesar plantilla
        if 'plantilla' in datos_json and 'imagen_fondo' in datos_json['plantilla']:
            datos_json['plantilla']['imagen_fondo'] = self.procesar_imagen_desde_json(
                datos_json['plantilla']['imagen_fondo'],
                'templates',
                (2000, 2000)  # Tamaño máximo para plantillas
            )
        
        return datos_json 