# Archivo principal que inicia el sistema de observación
# Importa la función principal del módulo observador
from src.observador import iniciar_observador

# Punto de entrada principal del programa
# Solo se ejecuta si este archivo se ejecuta directamente
if __name__ == "__main__":
    # Inicia el sistema de observación de la carpeta de entrada
    iniciar_observador()