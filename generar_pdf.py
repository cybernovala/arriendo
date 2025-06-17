from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter
import io

def generar_pdf(data):
    buffer = io.BytesIO()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Título principal
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "CONTRATO DE ARRIENDO", ln=True, align="C")

    # Texto del contrato
    pdf.set_font("Arial", "", 14)
    texto = f"""
En {data['ciudad']}, a {data['fecha']}, entre: don(ña) {data['arrendador'].upper()}, nacionalidad {data['nacionalidad_arrendador'].upper()}, RUT {data['rut_arrendador']}, con domicilio en {data['domicilio_arrendador'].upper()} (en adelante, el "Arrendador"); y don(ña) {data['arrendatario'].upper()}, nacionalidad {data['nacionalidad_arrendatario'].upper()}, RUT {data['rut_arrendatario']}, con domicilio en {data['domicilio_arrendatario'].upper()} (en adelante, el "Arrendatario"), acuerdan el siguiente contrato:

PRIMERO: El Arrendador da en arriendo al Arrendatario el inmueble ubicado en {data['direccion_inmueble'].upper()}, destinado exclusivamente para {data['uso'].upper()}.

SEGUNDO: El contrato tiene una duración de un año, desde el {data['inicio']} hasta el {data['termino']}, renovable automáticamente salvo aviso en contrario.

TERCERO: El Arrendatario pagará una renta mensual de {data['renta']} pesos, pagaderos dentro de los primeros cinco días de cada mes en la cuenta {data['cuenta']} del banco {data['banco']} a nombre del Arrendador.

CUARTO: El Arrendatario entrega al Arrendador la suma de {data['garantia']} pesos en calidad de garantía, la cual será restituida al término del contrato si no existen deudas ni daños.

QUINTO: El Arrendatario no podrá subarrendar ni ceder total o parcialmente este contrato sin autorización escrita del Arrendador.

SEXTO: El Arrendatario se obliga a mantener en buen estado el inmueble y devolverlo en las mismas condiciones en que lo recibió, salvo deterioro natural por uso legítimo.

SÉPTIMO: El Arrendatario autoriza expresamente al Arrendador a visitar el inmueble previa notificación, para verificar su estado.

OCTAVO: El no pago de la renta dentro del plazo señalado será causal de término anticipado del contrato.

NOVENO: Son de cargo del Arrendatario los gastos comunes, servicios básicos, contribuciones y toda otra obligación que derive del uso del inmueble.

DÉCIMO: El Arrendador se obliga a no alterar la tranquilidad del Arrendatario durante la vigencia del contrato.

DÉCIMO PRI
