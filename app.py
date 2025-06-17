from flask import Flask, request, send_file
from flask_cors import CORS
from generar_pdf import generar_pdf

app = Flask(__name__)
CORS(app)

@app.route("/generar_pdf", methods=["POST"])
def generar():
    data = request.get_json()
    pdf_bytes = generar_pdf(data)
    return send_file(pdf_bytes, download_name="arriendo_cybernova.pdf", as_attachment=True)
