from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VALIDACION_URL = "https://servicio-validacion.onrender.com/validar"

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    try:
        respuesta = requests.post(VALIDACION_URL, json=data)
        resultado = respuesta.json()
    except Exception as e:
        return jsonify({"error": "Error al validar"}), 500

    return jsonify({
        "mensaje": "Registro recibido.",
        "resultado_validacion": resultado
    })

# ❌ No pongas app.run()
