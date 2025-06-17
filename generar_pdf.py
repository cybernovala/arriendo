from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
import unicodedata

def limpiar_texto(texto):
    return unicodedata.normalize("NFKD", texto).encode("latin-1", "ignore").decode("latin-1")

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 10, txt=limpiar_texto("CONTRATO DE ARRENDAMIENTO"), align="C")
    pdf.ln()

    cuerpo = f"""
En {data['ciudad']} de Chile, a {data['fecha']}, entre: don(ña) {data['arrendador']}, nacionalidad {data['nacionalidad_arrendador']}, cédula de identidad N° {data['rut_arrendador']} con domicilio en {data['domicilio_arrendador']} (en adelante, el “Arrendador”); por una parte, y por la otra don(ña) {data['arrendatario']}, nacionalidad {data['nacionalidad_arrendatario']}, cédula de identidad N° {data['rut_arrendatario']} con domicilio en {data['direccion_inmueble']} (en adelante, el “Arrendatario”), acuerdan el siguiente contrato...

OBJETO: El Arrendador da en arriendo la propiedad ubicada en {data['direccion_inmueble']} para uso exclusivo de {data['uso_inmueble']}. La vigencia será del {data['inicio_vigencia']} al {data['termino_vigencia']}. La renta será de {data['renta']} pagada a la cuenta {data['cuenta']} del Banco {data['banco']}. Garantía: {data['garantia']}.

El resto de cláusulas legales se aplican conforme al contrato estándar y legislación chilena vigente.
    """

    pdf.multi_cell(0, 10, limpiar_texto(cuerpo), align="J")

    temp = io.BytesIO()
    pdf.output(temp)
    temp.seek(0)

    reader = PdfReader(temp)
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.encrypt(user_password="@@1234@@", owner_password="@@1234@@")
    
    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    return output
