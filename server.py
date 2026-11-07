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

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": messages,
        "system_instruction": {
            "parts": [{"text": "Jesteś Areo AI – inteligentnym asystentem stworzonym przez Marcela. Pomagasz w druku 3D, konfiguracji drukarek oraz automatyzacji. Odpowiadaj zwięźle i po polsku."}]
        }
    }

    try:
        res = requests.post(url, json=payload)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
