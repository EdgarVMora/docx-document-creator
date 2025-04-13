import json
import os
from manejador_imagenes import ManejadorImagenes
from test_imagenes import crear_imagen_prueba

def crear_imagenes_prueba():
    """
    Crea imágenes de prueba para cada tipo
    """
    imagenes = {
        "principal": crear_imagen_prueba("familia_martinez.png", (1200, 800)),
        "icono1": crear_imagen_prueba("juan.png", (300, 300)),
        "icono2": crear_imagen_prueba("maria.png", (300, 300)),
        "icono3": crear_imagen_prueba("ana.png", (300, 300)),
        "template": crear_imagen_prueba("fondo_familiar.png", (2000, 1500))
    }
    return imagenes

def main():
    print("🚀 Iniciando prueba de procesamiento de JSON con imágenes")
    print("=" * 50)
    
    # 1. Crear imágenes de prueba
    print("\n1. Creando imágenes de prueba...")
    imagenes = crear_imagenes_prueba()
    
    # 2. Cargar JSON de ejemplo
    print("\n2. Cargando JSON de ejemplo...")
    with open("entrada/arbol_ejemplo.json", 'r', encoding='utf-8') as f:
        datos_json = json.load(f)
    
    # 3. Actualizar rutas en el JSON
    print("\n3. Actualizando rutas de imágenes en el JSON...")
    datos_json['imagen_principal']['ruta'] = imagenes['principal']
    for i, miembro in enumerate(datos_json['miembros']):
        miembro['imagen']['ruta'] = imagenes[f'icono{i+1}']
    datos_json['plantilla']['imagen_fondo']['ruta'] = imagenes['template']
    
    # 4. Procesar JSON con imágenes
    print("\n4. Procesando JSON con imágenes...")
    manejador = ManejadorImagenes()
    datos_procesados = manejador.procesar_imagenes_json(datos_json)
    
    # 5. Guardar JSON procesado
    print("\n5. Guardando JSON procesado...")
    ruta_salida = "entrada/arbol_ejemplo_procesado.json"
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(datos_procesados, f, indent=4, ensure_ascii=False)
    print(f"📄 JSON guardado en: {ruta_salida}")
    
    # 6. Limpiar archivos temporales
    print("\n6. Limpiando archivos temporales...")
    for imagen in imagenes.values():
        if os.path.exists(imagen):
            os.remove(imagen)
    os.rmdir(os.path.join("imagenes", "temp"))
    print("🧹 Archivos temporales eliminados")
    
    print("\n✅ Prueba completada con éxito!")
    print("\nEstructura del JSON procesado:")
    print(json.dumps(datos_procesados, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main() 