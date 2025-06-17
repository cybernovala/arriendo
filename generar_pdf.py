from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import io

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CONTRATO DE ARRENDAMIENTO", ln=True, align="C")
    pdf.set_font("Arial", "", 14)
    pdf.multi_cell(0, 10, txt=f"""
EN {data['ciudad'].upper()} DE CHILE, A {data['fecha'].upper()}, ENTRE: DON(ÑA) {data['arrendador'].upper()}, NACIONALIDAD {data['nacionalidad_arrendador'].upper()}, CÉDULA {data['ci_arrendador']}, DOMICILIO {data['domicilio_arrendador'].upper()} (ARRENDADOR), Y DON(ÑA) {data['arrendatario'].upper()}, NACIONALIDAD {data['nacionalidad_arrendatario'].upper()}, CÉDULA {data['ci_arrendatario']} (ARRENDATARIO).

LA PROPIEDAD ESTÁ UBICADA EN {data['direccion_inmueble'].upper()} Y SE ARRIENDA PARA FINES DE {data['uso'].upper()}.

VIGENCIA: DESDE {data['inicio']} HASTA {data['termino']}.

RENTA MENSUAL: {data['renta']}, CUENTA: {data['cuenta']}, BANCO: {data['banco']}, GARANTÍA: {data['garantia']}.

FIRMAS:
ARRENDADOR: RUT {data['ci_arrendador']}
ARRENDATARIO: RUT {data['ci_arrendatario']}
""", align="J")

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Protección con contraseña
    reader = PdfReader(buffer)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(user_password="@@1234@@", owner_password="@@1234@@")
    output_buffer = io.BytesIO()
    writer.write(output_buffer)
    output_buffer.seek(0)
    return output_buffer
