from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import io
import datetime

def crear_contrato_pdf(data):
    buffer = io.BytesIO()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CONTRATO DE ARRENDAMIENTO", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 14)
    texto = f"""
EN {data['ciudad']} DE CHILE, A {data['dia']} DE {data['mes']} DEL AÑO {data['anio']}, ENTRE: DON(ÑA) {data['arrendador']}, NACIONALIDAD {data['nacionalidad_arrendador']}, CÉDULA DE IDENTIDAD N° {data['rut_arrendador']}, CON DOMICILIO EN {data['direccion_arrendador']}, COMUNA DE {data['comuna_arrendador']} (EN ADELANTE, EL “ARRENDADOR”); Y POR OTRA PARTE DON(ÑA) {data['arrendatario']}, NACIONALIDAD {data['nacionalidad_arrendatario']}, CÉDULA DE IDENTIDAD N° {data['rut_arrendatario']}, CON DOMICILIO EN {data['direccion_arrendatario']} (EN ADELANTE, EL “ARRENDATARIO”), Y CONJUNTAMENTE, LAS “PARTES”.

[CONTENIDO DEL CONTRATO...]

FIRMAS:

___________________________
{data['arrendador']}
RUT: {data['rut_arrendador']}

___________________________
{data['arrendatario']}
RUT: {data['rut_arrendatario']}
    """

    for parrafo in texto.strip().split("\n\n"):
        pdf.multi_cell(0, 8, parrafo.strip(), align="J")
        pdf.ln(2)

    pdf.output(buffer)
    buffer.seek(0)

    # Protección con contraseña
    reader = PdfReader(buffer)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(user_password="@@1234@@", owner_password=None, use_128bit=True)

    final_pdf = io.BytesIO()
    writer.write(final_pdf)
    final_pdf.seek(0)
    return final_pdf
