from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return "WhatsApp Chatbot Running"

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg:
        msg.body("Hi! How can I assist you today?")
    elif 'price' in incoming_msg:
        msg.body("Our pricing depends on the service. What do you need?")
    elif 'help' in incoming_msg:
        msg.body("I’m sorry, I didn't understand. Could you rephrase?")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
