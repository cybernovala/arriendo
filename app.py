from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from generar_pdf import generar_pdf
import io

app = Flask(__name__)
CORS(app)

@app.route("/generar_pdf", methods=["POST"])
def crear_pdf():
    try:
        datos = request.get_json()
        pdf_bytes = generar_pdf(datos)
        return send_file(
            io.BytesIO(pdf_bytes),
            download_name="arriendo_cybernova.pdf",
            as_attachment=True,
            mimetype="application/pdf"
        )
    except Exception as e:
        print("Error al generar PDF:", e)
        return jsonify({"error": "Error interno del servidor"}), 500
