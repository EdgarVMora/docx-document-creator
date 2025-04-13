# 🌳 Generador de Documentos de Árboles

Este proyecto automatiza la generación de documentos Word con información detallada sobre árboles, ideal para inventarios forestales, estudios ambientales o registros botánicos. El sistema implementa un observador de archivos que procesa automáticamente los datos cuando se agregan nuevos registros.

## 📋 Características

- Generación automática de documentos Word (.docx) con formato profesional
- Sistema de observación continua de la carpeta de entrada
- Procesamiento automático de imágenes con optimización y redimensionamiento
- Organización inteligente de archivos procesados
- Soporte para emojis y formato enriquecido en documentos
- Sistema de plantillas personalizable para diferentes tipos de reportes
- Manejo de errores robusto y logging informativo
- Procesamiento asíncrono de archivos

## 🎯 Casos de Uso

- Inventarios forestales
- Estudios ambientales
- Registros botánicos
- Documentación de árboles patrimoniales
- Catálogos de especies
- Informes técnicos forestales

## 🚀 Estructura del Proyecto

```
arboles-doc-generator/
├── entrada/           # Carpeta para archivos JSON de entrada
│   └── procesados/   # Archivos JSON ya procesados
├── imagenes/         # Carpetas de imágenes organizadas
│   ├── arboles/     # Imágenes principales de árboles
│   ├── iconos/      # Iconos y miniaturas
│   └── templates/   # Plantillas y fondos
├── salida/          # Documentos Word generados
└── src/             # Código fuente
    ├── generador.py # Generación de documentos Word
    └── observador.py # Sistema de monitoreo de archivos
```

## 🛠️ Requisitos Técnicos

- Python 3.9 o superior
- Sistema operativo: Windows, macOS o Linux
- Dependencias principales (requirements.txt):
  - python-docx==0.8.11 (Generación de documentos)
  - watchdog==3.0.0 (Monitoreo de archivos)
  - Pillow==10.2.0 (Procesamiento de imágenes)

## 📥 Instalación y Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/EdgarVMora/arboles-doc-generator.git
cd arboles-doc-generator
```

2. Crear y activar entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Guía de Uso

1. Preparar el archivo JSON con la información del árbol:
```json
{
    "id": "ARB001",
    "nombre": "Roble Centenario",
    "descripcion": "Roble antiguo ubicado en el parque central",
    "ubicacion": "Parque Central",
    "especie": "Quercus robur",
    "altura_metros": 15.5,
    "edad_aproximada": "150 años",
    "estado_salud": "Bueno",
    "fecha": "2024-04-12",
    "imagen": "roble_001.jpg",
    "tabla_extendida": [
        {
            "atributo": "Diámetro del tronco",
            "valor": "1.2 metros"
        },
        {
            "atributo": "Tipo de corteza",
            "valor": "Agrietada y gruesa"
        }
    ],
    "pie_imagen": "Vista frontal del roble centenario"
}
```

2. Preparar las imágenes:
   - Colocar imágenes principales en `imagenes/arboles/`
   - Formato soportado: JPG, PNG, GIF, BMP
   - Resolución recomendada: mínimo 1200x800 píxeles

3. Iniciar el sistema de monitoreo:
```bash
python watch.py
```

4. Colocar los archivos JSON en la carpeta `entrada/`

El sistema automáticamente:
- Detecta nuevos archivos JSON
- Procesa las imágenes asociadas
- Genera documentos Word formatados
- Mueve los archivos procesados a sus respectivas carpetas

## 📄 Formato del Documento Generado

El documento Word generado incluye:
- Título con emoji personalizado 🌳
- Descripción destacada en azul y negrita
- Tabla de información técnica con emojis
- Información extendida en formato tabular
- Imagen del árbol optimizada
- Pie de foto en formato elegante
- Fecha de registro
- Formato profesional y consistente

## 🔄 Flujo de Trabajo

1. El observador monitorea la carpeta `entrada/`
2. Al detectar un nuevo archivo JSON:
   - Valida el formato y contenido
   - Procesa y optimiza las imágenes
   - Genera el documento Word
   - Mueve el JSON a `entrada/procesados/`
3. El documento generado se guarda en `salida/`

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Abre un pull request

Para cambios mayores, por favor abre primero un issue para discutir los cambios propuestos.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👤 Contacto

Edgar Vázquez Mora
- LinkedIn: [Edgar Vázquez Mora](https://www.linkedin.com/in/edgar-v%C3%A1zquez-mora-1125bb263/)
- GitHub: [EdgarVMora](https://www.github.com/EdgarVMora)

🔗 Link del Proyecto: [https://github.com/EdgarVMora/arboles-doc-generator](https://github.com/EdgarVMora/arboles-doc-generator)
