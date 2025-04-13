from PIL import Image
import os
from manejador_imagenes import ManejadorImagenes

def crear_imagen_prueba(nombre="imagen_prueba.png", size=(800, 600), color=(255, 255, 255)):
    """
    Crea una imagen de prueba con un patrón simple
    """
    # Crear una imagen en blanco
    imagen = Image.new('RGB', size, color)
    
    # Calcular dimensiones del patrón
    ancho, alto = size
    margen_x = int(ancho * 0.1)
    margen_y = int(alto * 0.1)
    area_x = ancho - 2 * margen_x
    area_y = alto - 2 * margen_y
    
    # Dibujar un patrón simple (un rectángulo)
    for x in range(margen_x, margen_x + area_x):
        for y in range(margen_y, margen_y + area_y):
            if (x + y) % 50 < 25:
                imagen.putpixel((x, y), (0, 128, 255))
    
    # Guardar la imagen temporalmente
    ruta_temporal = os.path.join("imagenes", "temp")
    os.makedirs(ruta_temporal, exist_ok=True)
    ruta_imagen = os.path.join(ruta_temporal, nombre)
    imagen.save(ruta_imagen)
    
    print(f"✨ Imagen de prueba creada: {ruta_imagen}")
    return ruta_imagen

def main():
    # Crear instancia del manejador
    manejador = ManejadorImagenes()
    
    print("🚀 Iniciando prueba del sistema de manejo de imágenes")
    print("=" * 50)
    
    # 1. Crear imagen de prueba
    print("\n1. Creando imagen de prueba...")
    ruta_imagen = crear_imagen_prueba()
    
    # 2. Guardar imagen en diferentes categorías
    print("\n2. Guardando imagen en diferentes categorías...")
    
    # Guardar como árbol
    ruta_arbol = manejador.guardar_imagen(ruta_imagen, tipo="arboles")
    print(f"📁 Guardada como árbol: {ruta_arbol}")
    
    # Guardar como icono
    ruta_icono = manejador.guardar_imagen(ruta_imagen, tipo="iconos")
    print(f"📁 Guardada como icono: {ruta_icono}")
    
    # 3. Listar imágenes
    print("\n3. Listando imágenes guardadas:")
    print("\nÁrboles:")
    for img in manejador.listar_imagenes("arboles"):
        print(f"  - {img}")
    
    print("\nIconos:")
    for img in manejador.listar_imagenes("iconos"):
        print(f"  - {img}")
    
    # 4. Obtener una imagen
    print("\n4. Probando obtención de imagen:")
    nombre_imagen = os.path.basename(ruta_arbol)
    ruta_recuperada = manejador.obtener_imagen(nombre_imagen, "arboles")
    print(f"📂 Imagen recuperada: {ruta_recuperada}")
    
    # 5. Limpiar imagen temporal
    print("\n5. Limpiando archivos temporales...")
    os.remove(ruta_imagen)
    os.rmdir(os.path.join("imagenes", "temp"))
    print("🧹 Archivos temporales eliminados")
    
    print("\n✅ Prueba completada con éxito!")

if __name__ == "__main__":
    main() 