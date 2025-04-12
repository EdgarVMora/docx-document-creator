# Generador de Documentación con Árboles

Este proyecto es una herramienta de generación de documentación que convierte archivos JSON con información de árboles en documentos Word (.docx) estructurados, incluyendo imágenes y detalles específicos de cada árbol.

## Estructura del Proyecto

```
arboles-doc-generator/
├── src/               # Código fuente del proyecto
│   └── generador.py   # Módulo para generar documentos Word
├── entrada/           # Archivos JSON de árboles
├── salida/           # Documentos Word generados
├── imagenes/         # Imágenes de los árboles
├── main.py           # Punto de entrada de la aplicación
├── requirements.txt  # Dependencias del proyecto
└── env/              # Entorno virtual de Python
```

## Funcionalidad

### Estructura de los Archivos JSON
Los archivos de entrada deben ser JSON con la siguiente estructura:
```json
{
    "id": "001",
    "nombre": "Nombre del Árbol",
    "descripcion": "Descripción detallada",
    "ubicacion": "Ubicación del árbol",
    "fecha": "YYYY-MM-DD",
    "imagen": "nombre_imagen.jpg"
}
```

### Componentes Principales

1. **main.py**
   - Punto de entrada de la aplicación
   - Gestiona la carga de archivos JSON desde la carpeta `entrada/`
   - Procesa cada archivo JSON y genera su documento correspondiente

2. **src/generador.py**
   - Contiene la lógica para crear documentos Word
   - Genera documentos con:
     - Título con el nombre del árbol
     - Descripción del árbol
     - Ubicación
     - Fecha
     - Imagen del árbol (si está disponible)

### Proceso de Generación
1. El sistema lee todos los archivos JSON de la carpeta `entrada/`
2. Para cada árbol:
   - Crea un nuevo documento Word
   - Agrega la información estructurada
   - Incluye la imagen correspondiente desde la carpeta `imagenes/`
   - Guarda el documento en la carpeta `salida/`

## Requisitos Previos

- Python 3.x
- Entorno virtual (recomendado)
- Dependencias principales:
  - python-docx (para generación de documentos Word)

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL-del-repositorio]
cd arboles-doc-generator
```

2. Crear y activar el entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Unix/macOS
# o
.\env\Scripts\activate  # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Prepara tus archivos:
   - Coloca los archivos JSON en la carpeta `entrada/`
   - Asegúrate que las imágenes referenciadas estén en la carpeta `imagenes/`

2. Ejecuta el programa:
```bash
python main.py
```

3. Los documentos generados se encontrarán en el directorio `salida/` con el formato:
   `[ID]_[Nombre_del_Árbol].docx`

## Estructura de Directorios

- `src/`: Contiene el código fuente del proyecto
  - `generador.py`: Módulo principal para la generación de documentos
- `entrada/`: Archivos JSON con información de árboles
- `salida/`: Documentos Word generados
- `imagenes/`: Imágenes de los árboles referenciadas en los JSON

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter)

Link del Proyecto: [https://github.com/tuusuario/arboles-doc-generator](https://github.com/tuusuario/arboles-doc-generator)
