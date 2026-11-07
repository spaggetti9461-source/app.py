import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route("/api/chat", methods=["POST"])
def chat():
    if not GEMINI_API_KEY:
        return jsonify({"error": "Brak klucza API na serwerze."}), 500

    data = request.json
    messages = data.get("messages", [])

    # Użycie najnowszego modelu opartego o zaawansowane wnioskowanie
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": messages,
        "system_instruction": {
            "parts": [{"text": "Jesteś Areo AI – inteligentnym asystentem stworzonym przez Marcela. Pomagasz w druku 3D, konfiguracji drukarek oraz automatyzacji. Jeśli użytkownik prosi o wygenerowanie obrazu, powiedz mu, aby użył komendy /obraz [opis]."}]
        }
    }

    try:
        res = requests.post(url, json=payload)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/generate-image", methods=["POST"])
def generate_image():
    if not GEMINI_API_KEY:
        return jsonify({"error": "Brak klucza API."}), 500

    data = request.json
    prompt = data.get("prompt", "")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:predict?key={GEMINI_API_KEY}"

    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": "1:1"}
    }

    try:
        res = requests.post(url, json=payload)
        res_data = res.json()

        if "predictions" in res_data and len(res_data["predictions"]) > 0:
            b64_img = res_data["predictions"][0]["bytesBase64Encoded"]
            return jsonify({"image_url": f"data:image/png;base64,{b64_img}"})
        else:
            return jsonify({"error": "Nie udało się wygenerować obrazu."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
