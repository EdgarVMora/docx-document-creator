from docx import Document
from docx.shared import Pt, Inches, RGBColor
import os

def generar_documento(data, carpeta_imagenes, carpeta_salida):
    doc = Document()

    # Título principal
    titulo = doc.add_heading(f"🌳 {data['nombre']}", level=0)
    doc.add_paragraph("")

    # Descripción con estilo
    parrafo_desc = doc.add_paragraph()
    run_desc = parrafo_desc.add_run(data['descripcion'])
    run_desc.bold = True
    run_desc.font.size = Pt(12)
    run_desc.font.color.rgb = RGBColor(0, 102, 204)  # Azul oscuro
    doc.add_paragraph("")

    # Tabla con información adicional
    doc.add_paragraph("📊 Información Técnica:", style='Intense Quote')

    tabla = doc.add_table(rows=5, cols=2)
    tabla.style = 'Light Grid Accent 1'

    campos = [
        ("📍 Ubicación", data.get("ubicacion", "No especificada")),
        ("🧬 Especie", data.get("especie", "Desconocida")),
        ("📏 Altura (m)", str(data.get("altura_metros", "N/A"))),
        ("⏳ Edad Aproximada", data.get("edad_aproximada", "N/A")),
        ("❤️ Estado de Salud", data.get("estado_salud", "No registrado"))
    ]

    for i, (campo, valor) in enumerate(campos):
        tabla.cell(i, 0).text = campo
        tabla.cell(i, 1).text = valor

    doc.add_paragraph("")

    # Fecha del registro
    doc.add_paragraph(f"📅 Fecha de registro: {data['fecha']}")

    doc.add_paragraph("")

    # Imagen si existe
    imagen_path = os.path.join(carpeta_imagenes, data.get("imagen", ""))
    if os.path.exists(imagen_path):
        doc.add_paragraph("📸 Fotografía del Árbol:")
        doc.add_picture(imagen_path, width=Inches(4.0))
    else:
        doc.add_paragraph("⚠️ Imagen no disponible.")

    # Guardar
    filename = f"{data['id']}_{data['nombre'].replace(' ', '_')}.docx"
    ruta_salida = os.path.join(carpeta_salida, filename)
    doc.save(ruta_salida)

    print(f"✅ Documento generado: {ruta_salida}")