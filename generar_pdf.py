from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
import datetime

def generar_pdf(data):
    texto = f"""
EN {data['ciudad'].upper()}, A {data['fecha'].upper()}, ENTRE {data['ARRENDADOR'].upper()} DE NACIONALIDAD {data['nacionalidad_arrendador'].upper()}, CÉDULA {data['cedula_arrendador'].upper()}, DOMICILIO EN {data['domicilio_arrendador'].upper()} Y {data['ARRENDATARIO'].upper()} DE NACIONALIDAD {data['nacionalidad_arrendatario'].upper()}, CÉDULA {data['cedula_arrendatario'].upper()}, SE CELEBRA CONTRATO DE ARRIENDO DEL INMUEBLE UBICADO EN {data['direccion_inmueble'].upper()}, DESTINADO A {data['uso'].upper()}, POR EL PERIODO DESDE {data['inicio'].upper()} HASTA {data['termino'].upper()}, CON RENTA MENSUAL DE {data['renta'].upper()} PAGADERA EN CUENTA {data['cuenta'].upper()} DEL BANCO {data['banco'].upper()}. SE ENTREGA COMO GARANTÍA LA SUMA DE {data['garantia'].upper()}.
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CONTRATO DE ARRIENDO", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 14)
    pdf.multi_cell(0, 10, texto, align="J")
    pdf.ln(20)
    pdf.cell(0, 10, f"Los Ángeles, {datetime.datetime.now().strftime('%d de %B de %Y')}", ln=True, align="R")

    pdf.ln(30)
    pdf.cell(90, 10, "FIRMA ARRENDADOR", ln=0, align="C")
    pdf.cell(0, 10, "FIRMA ARRENDATARIO", ln=1, align="C")
    pdf.cell(90, 10, data["cedula_arrendador"], ln=0, align="C")
    pdf.cell(0, 10, data["cedula_arrendatario"], ln=1, align="C")

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Proteger PDF con contraseña
    reader = PdfReader(buffer)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password="@@1234@@", owner_password="@@1234@@")
    output_buffer = io.BytesIO()
    writer.write(output_buffer)
    output_buffer.seek(0)
    return output_buffer.read()
