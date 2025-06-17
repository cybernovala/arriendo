from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from generar_pdf import generar_pdf
import io

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API de generación de contrato de arriendo activa."})

@app.route("/generar_pdf", methods=["POST"])
def generar():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400

        pdf_bytes = generar_pdf(data)

        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype="application/pdf",
            as_attachment=True,
            download_name="arriendo_cybernova.pdf"
        )

    except Exception as e:
        print(f"Error al generar el PDF: {str(e)}")
        return jsonify({"error": "Error al generar el PDF"}), 500

if __name__ == "__main__":
    app.run(debug=True)
