from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "OpenAI Chatbot is Live!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if enabled
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response['choices'][0]['message']['content'].strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
