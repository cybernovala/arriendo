from flask import Flask, request, send_file
from flask_cors import CORS
from generar_pdf import crear_contrato_pdf

app = Flask(__name__)
CORS(app)

@app.route("/generar_pdf", methods=["POST"])
def generar_pdf():
    data = request.get_json()
    pdf_bytes = crear_contrato_pdf(data)
    return send_file(pdf_bytes, mimetype="application/pdf", download_name="arriendo_cybernova.pdf", as_attachment=True)
