from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io
from datetime import datetime

def generar_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)

    # Título
    pdf.cell(0, 10, "CONTRATO DE ARRIENDO", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", "", 14)

    # Construcción del texto legal
    texto = f"""
En la ciudad de {data['ciudad'].upper()}, con fecha {data['fecha'].upper()}, comparecen: por una parte don {data['nombre_arrendador'].upper()}, RUT {data['rut_arrendador']}, en adelante el ARRENDADOR; y por la otra, don {data['nombre_arrendatario'].upper()}, RUT {data['rut_arrendatario']}, en adelante el ARRENDATARIO. Ambas partes convienen en celebrar el presente contrato de arriendo sujeto a las siguientes cláusulas:

PRIMERA: El ARRENDADOR da en arriendo al ARRENDATARIO el inmueble ubicado en {data['direccion_inmueble'].upper()}.

SEGUNDA: El plazo del presente contrato es de {data['plazo_contrato'].upper()}, comenzando el {data['inicio_contrato'].upper()}.

TERCERA: El canon mensual de arriendo será de ${data['monto_arriendo']} ({data['monto_palabras'].upper()}), pagaderos por adelantado dentro de los primeros cinco días de cada mes.

CUARTA: Los pagos deberán efectuarse en {data['lugar_pago'].upper()} o mediante transferencia a la cuenta {data['cuenta_bancaria']}.

QUINTA: El ARRENDATARIO se obliga a usar el inmueble exclusivamente como {data['uso_inmueble'].upper()}.

SEXTA: No podrá subarrendar ni ceder el contrato sin autorización escrita del ARRENDADOR.

SÉPTIMA: El ARRENDATARIO es responsable de mantener el inmueble en buen estado y responderá por los daños que se causen.

OCTAVA: El ARRENDATARIO deberá permitir la inspección del inmueble por parte del ARRENDADOR previo aviso razonable.

NOVENA: Los gastos comunes, contribuciones y servicios básicos serán de cargo del ARRENDATARIO, salvo pacto en contrario.

DÉCIMA: El incumplimiento de alguna de las cláusulas facultará al ARRENDADOR para poner término anticipado al contrato.

DÉCIMA PRIMERA: El contrato podrá renovarse previo acuerdo por escrito de ambas partes.

DÉCIMA SEGUNDA: El ARRENDATARIO deberá restituir el inmueble en las condiciones en que lo recibió, salvo deterioros por uso legítimo.

DÉCIMA TERCERA: En caso de controversias, las partes fijan su domicilio en la ciudad de {data['ciudad'].upper()} y se someten a la jurisdicción de sus tribunales.

DÉCIMA CUARTA: Las partes declaran haber leído y entendido el presente contrato.

DÉCIMA QUINTA: Este contrato se firma en dos ejemplares del mismo tenor y fecha, quedando uno en poder de cada parte.

DÉCIMA SEXTA: El ARRENDATARIO constituye domicilio especial en el inmueble objeto de este contrato.

DÉCIMA SÉPTIMA: Las partes acuerdan que toda comunicación deberá realizarse al correo electrónico o número telefónico declarado.

Y en prueba de conformidad, firman.
"""

    # Insertar el texto con justificación
    for parrafo in texto.strip().split("\n\n"):
        pdf.multi_cell(0, 10, parrafo.strip(), align="J")
        pdf.ln(2)

    # Fecha al pie
    fecha_actual = datetime.now().strftime("%d de %B de %Y")
    ciudad = data['ciudad'].capitalize()
    pdf.ln(10)
    pdf.cell(0, 10, f"{ciudad}, {fecha_actual}", ln=True, align="R")

    # Firmas centradas y ordenadas
    pdf.ln(20)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "FIRMADO:", ln=True, align="C")

    pdf.set_font("Arial", "", 14)
    pdf.ln(5)
    pdf.cell(0, 10, f"ARRENDADOR: {data['nombre_arrendador'].upper()}", ln=True, align="C")
    pdf.cell(0, 10, f"RUT: {data['rut_arrendador']}", ln=True, align="C")

    pdf.ln(5)
    pdf.cell(0, 10, f"ARRENDATARIO: {data['nombre_arrendatario'].upper()}", ln=True, align="C")
    pdf.cell(0, 10, f"RUT: {data['rut_arrendatario']}", ln=True, align="C")

    # Convertir a bytes y aplicar protección
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    reader = PdfReader(pdf_output)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(user_password="@@1234@@", owner_password=None, use_128bit=True)

    final_output = io.BytesIO()
    writer.write(final_output)
    final_output.seek(0)
    return final_output
