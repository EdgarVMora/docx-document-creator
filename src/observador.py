# Importaciones necesarias para el funcionamiento del observador
import time         # Para pausas y manejo de tiempo
import os          # Para operaciones del sistema de archivos
import json        # Para procesar archivos JSON
import shutil      # Para mover archivos
# Importaciones de watchdog para monitoreo de archivos
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.generador import generar_documento
from src.utils import logger, validar_json, crear_carpetas_necesarias

# Definición de las rutas principales del sistema
CARPETA_ENTRADA = "entrada"          # Carpeta donde se colocan los archivos a procesar
CARPETA_IMAGENES = "imagenes"        # Carpeta que contiene las imágenes necesarias
CARPETA_SALIDA = "salida"           # Carpeta donde se generarán los documentos
CARPETA_PROCESADOS = os.path.join(CARPETA_ENTRADA, "procesados")  # Subcarpeta para archivos ya procesados

# Crear estructura de carpetas
CARPETAS_REQUERIDAS = [
    CARPETA_ENTRADA,
    CARPETA_PROCESADOS,
    CARPETA_IMAGENES,
    CARPETA_SALIDA
]

crear_carpetas_necesarias(CARPETAS_REQUERIDAS)

class ManejadorEventos(FileSystemEventHandler):
    """
    Clase que maneja los eventos del sistema de archivos.
    Hereda de FileSystemEventHandler de watchdog.
    """
    def on_created(self, event):
        """
        Se ejecuta cuando se detecta la creación de un nuevo archivo
        
        Args:
            event: Evento que contiene información sobre el archivo creado
        """
        # Ignora eventos de carpetas
        if event.is_directory:
            return

        # Solo procesa archivos JSON
        if event.src_path.endswith('.json'):
            try:
                logger.info(f"📥 Archivo detectado: {event.src_path}")
                
                # Lee y carga el contenido del archivo JSON
                with open(event.src_path, 'r', encoding='utf-8') as f:
                    datos = json.load(f)

                # Validar JSON
                es_valido, mensaje = validar_json(datos)
                if not es_valido:
                    logger.error(f"JSON inválido: {mensaje}")
                    return

                # Genera el documento con los datos del JSON
                generar_documento(datos, CARPETA_IMAGENES, CARPETA_SALIDA)

                # Mueve el archivo JSON a la carpeta de procesados
                nombre_archivo = os.path.basename(event.src_path)
                destino = os.path.join(CARPETA_PROCESADOS, nombre_archivo)
                shutil.move(event.src_path, destino)
                logger.info(f"✅ Archivo procesado y movido a: {destino}")

            except json.JSONDecodeError as e:
                logger.error(f"❌ Error de formato JSON en {event.src_path}: {e}")
            except Exception as e:
                logger.error(f"❌ Error al procesar {event.src_path}: {e}")

def iniciar_observador():
    """
    Función principal que inicia el sistema de observación.
    Configura y mantiene ejecutando el observador hasta que se detenga manualmente.
    """
    try:
        # Crea instancias del observador y manejador
        observador = Observer()
        manejador = ManejadorEventos()
        
        # Configura el observador para monitorear la carpeta de entrada
        observador.schedule(manejador, path=CARPETA_ENTRADA, recursive=False)
        observador.start()
        logger.info("👀 Observando la carpeta de entrada. Presiona Ctrl+C para detener...")

        # Mantiene el programa ejecutándose
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Maneja la interrupción del usuario (Ctrl+C)
        logger.info("🛑 Deteniendo el observador...")
        observador.stop()
        observador.join()
        logger.info("✅ Observador detenido correctamente")
    except Exception as e:
        logger.error(f"❌ Error en el observador: {e}")
    