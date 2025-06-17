from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from generar_pdf import generar_pdf
import io
import logging

app = Flask(__name__)
CORS(app, origins=["https://cybernovala.github.io"])

# Registro de errores en consola para Render
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def home():
    return "Generador de contrato de arriendo activo."

@app.route("/generar_pdf", methods=["POST"])
def generar():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos JSON no proporcionados"}), 400

        # Generar el contenido del PDF (bytes)
        pdf_bytes = generar_pdf(data)

        # Envolver los bytes en un buffer para envío
        buffer = io.BytesIO(pdf_bytes)
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name="arriendo_cybernova.pdf",
            mimetype="application/pdf"
        )

    except Exception as e:
        logging.error("Error al generar el PDF: %s", str(e))
        return jsonify({"error": f"Error al generar el PDF: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
