import os
import subprocess
import requests
import pyautogui
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder"

def find_blender():
    possible_paths = [
        r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return "blender"

def call_llm(history, system_instruction=""):
    identity_prompt = (
        "Jesteś Areo AI – inteligentnym i pomocnym asystentem stworzonym przez Marcela. "
        "Pomagasz w druku 3D, generowaniu modeli oraz automatyzacji zadań. "
        "Odpowiadaj bezpośrednio, zwięźle i precyzyjnie. Pamiętaj kontekst wcześniejszej rozmowy."
    )
    
    full_system = f"{identity_prompt}\n{system_instruction}" if system_instruction else identity_prompt
    
    formatted_prompt = f"<|im_start|>system\n{full_system}<|im_end|>\n"
    for role, text in history:
        formatted_prompt += f"<|im_start|>{role}\n{text}<|im_end|>\n"
    formatted_prompt += "<|im_start|>assistant\n"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": formatted_prompt,
        "stream": False
    }
    try:
        res = requests.post(OLLAMA_URL, json=payload)
        return res.json().get("response", "").strip()
    except Exception as e:
        return f"Błąd połączenia z serwerem Ollama: {e}"

def clean_code(raw_code):
    code = raw_code.strip()
    if code.startswith("```python"):
        code = code[9:]
    if code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
    return code.strip()

# Nowoczesny interfejs z menu bocznym, nowym tematem i historią
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Areo AI ⚡ created by Marcel</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #121212; color: #e0e0e0; margin: 0; display: flex; height: 100vh; overflow: hidden; }
        
        /* Menu Boczne */
        .sidebar { width: 260px; background: #181818; border-right: 1px solid #282828; display: flex; flex-direction: column; padding: 15px; }
        .new-chat-btn { background: #ff9800; color: black; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 14px; margin-bottom: 20px; text-align: center; }
        .new-chat-btn:hover { background: #e68900; }
        .history-title { font-size: 12px; color: #888; text-transform: uppercase; margin-bottom: 10px; letter-spacing: 1px; }
        .history-list { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 5px; }
        .history-item { background: #222; padding: 10px; border-radius: 5px; font-size: 13px; color: #ccc; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .history-item:hover { background: #2a2a2a; color: white; }

        /* Główny panel czatu */
        .main-content { flex: 1; display: flex; flex-direction: column; background: #121212; }
        .chat-header { padding: 15px 20px; background: #181818; border-bottom: 1px solid #282828; font-size: 16px; font-weight: bold; color: #ff9800; display: flex; justify-content: space-between; align-items: center; }
        .chat-box { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; }
        .message { padding: 12px 16px; border-radius: 8px; max-width: 75%; line-height: 1.4; word-break: break-word; font-size: 15px; }
        .user { background: #007acc; color: white; align-self: flex-end; }
        .ai { background: #222; color: #e0e0e0; align-self: flex-start; border: 1px solid #333; }
        
        /* Dolny pasek wpisywania */
        .input-area { padding: 20px; background: #181818; border-top: 1px solid #282828; display: flex; gap: 10px; }
        input { flex: 1; padding: 14px; border: 1px solid #333; background: #222; color: white; border-radius: 6px; font-size: 15px; outline: none; }
        input:focus { border-color: #ff9800; }
        button.send-btn { padding: 0 24px; background: #ff9800; border: none; color: black; font-weight: bold; border-radius: 6px; cursor: pointer; font-size: 15px; }
        button.send-btn:hover { background: #e68900; }
    </style>
</head>
<body>

    <!-- Boczne Menu -->
    <div class="sidebar">
        <button class="new-chat-btn" onclick="startNewChat()">+ Nowy temat</button>
        <div class="history-title">Historia konwersacji</div>
        <div class="history-list" id="historyList">
            <!-- Tutaj wskoczą zapisane tematy -->
        </div>
    </div>

    <!-- Okno Główne -->
    <div class="main-content">
        <div class="chat-header">
            <span>⚡ Areo AI (Stworzone przez Marcela)</span>
        </div>
        <div class="chat-box" id="chatBox">
            <div class="message ai">Cześć! Jestem Areo AI. W czym mogę Ci dzisiaj pomóc?</div>
        </div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Napisz wiadomość lub polecenie 3D..." onkeypress="handleKey(event)">
            <button class="send-btn" onclick="sendMessage()">Wyślij</button>
        </div>
    </div>

    <script>
        let chatHistory = [];

        function startNewChat() {
            chatHistory = [];
            const chatBox = document.getElementById('chatBox');
            chatBox.innerHTML = '<div class="message ai">Rozpoczęliśmy nowy temat. W czym mogę pomóc?</div>';
        }

        async function sendMessage() {
            const input = document.getElementById('userInput');
            const chatBox = document.getElementById('chatBox');
            const text = input.value.trim();
            if (!text) return;

            chatBox.innerHTML += `<div class="message user">${text}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            chatHistory.push(["user", text]);

            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ history: chatHistory })
            });
            const data = await res.json();

            chatBox.innerHTML += `<div class="message ai">${data.response}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;

            chatHistory.push(["assistant", data.response]);
            updateSidebarHistory(text);
        }

        function updateSidebarHistory(firstMessage) {
            const historyList = document.getElementById('historyList');
            // Dodaj skrót do historii po lewej stronie
            const item = document.createElement('div');
            item.className = 'history-item';
            item.innerText = firstMessage;
            item.onclick = () => { alert("Wybrano zapisany temat: " + firstMessage); };
            historyList.prepend(item);
        }

        function handleKey(e) {
            if (e.key === 'Enter') sendMessage();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    history = data.get("history", [])
    if not history:
        return jsonify({"response": "Brak historii wiadomości."})

    user_input = history[-1][1]
    cmd_lower = user_input.lower()
    blender_exe = find_blender()

    # 1. Tworzenie modeli 3D w Blenderze
    if any(w in cmd_lower for w in ["stl", "blender", "model 3d", "kostka", "kwadrat", "waza", "kula", "doniczka"]):
        output_stl = os.path.abspath("model_areo.stl")
        sys_prompt = f"Napisz WYŁĄCZNIE czysty kod Python bpy dla Blendera tworzący obiekt '{user_input}' i eksportujący go do STL pod ścieżkę: '{output_stl}'. Bez komentarzy i bez znaczników markdown."
        code = clean_code(call_llm(history, sys_prompt))
        
        script_file = "temp_script.py"
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(code)
        try:
            subprocess.run([blender_exe, "--background", "--python", script_file], check=True)
            response_text = f"✅ Wygenerowano model 3D i zapisano na serwerze jako: model_areo.stl"
        except Exception as e:
            response_text = f"❌ Błąd generowania modelu w Blenderze: {e}"

    # 2. Zwykła konwersacja
    else:
        response_text = call_llm(history)

    return jsonify({"response": response_text})

if __name__ == "__main__":
    print("🚀 Areo AI z panelem webowym uruchomione!")
    app.run(host="0.0.0.0", port=5000, debug=True)
