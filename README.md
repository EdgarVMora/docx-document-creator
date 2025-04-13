# 🌳 Generador de Documentos de Árboles

Este proyecto automatiza la generación de documentos Word con información detallada sobre árboles, ideal para inventarios forestales, estudios ambientales o registros botánicos.

## 📋 Características

- Generación automática de documentos Word (.docx)
- Procesamiento de imágenes automático
- Monitoreo de carpeta de entrada para procesamiento automático
- Organización automática de archivos procesados
- Soporte para emojis y formato enriquecido
- Sistema de plantillas personalizable

## 🚀 Estructura del Proyecto

```
arboles-doc-generator/
├── entrada/           # Carpeta para archivos JSON de entrada
│   └── procesados/   # Archivos JSON ya procesados
├── imagenes/         # Carpetas de imágenes
│   ├── arboles/     # Imágenes principales de árboles
│   ├── iconos/      # Iconos y miniaturas
│   └── templates/   # Plantillas y fondos
├── salida/          # Documentos Word generados
└── src/             # Código fuente
    ├── generador.py # Generación de documentos
    └── observador.py # Monitoreo de archivos
```

## 🛠️ Requisitos

- Python 3.9 o superior
- Dependencias (en requirements.txt):
  - python-docx==0.8.11
  - watchdog==3.0.0
  - Pillow==10.2.0

## 📥 Instalación

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
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

## 💻 Uso

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
    "imagen": "roble_001.jpg"
}
```

2. Colocar las imágenes en la carpeta `imagenes/arboles/`

3. Iniciar el sistema:
```bash
python watch.py
```

4. Colocar los archivos JSON en la carpeta `entrada/`

El sistema procesará automáticamente los archivos y generará los documentos Word en la carpeta `salida/`.

## 📄 Formato del Documento Generado

El documento Word incluirá:
- Título con emoji
- Descripción destacada
- Tabla de información técnica
- Información extendida (opcional)
- Imagen del árbol con pie de foto
- Fecha de registro
- Formato profesional y consistente

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter)

Link del Proyecto: [https://github.com/tuusuario/arboles-doc-generator](https://github.com/tuusuario/arboles-doc-generator)
