from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hungry Hub - Chatbot Backend Services"

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}  # Change "answer:" to "answer"
    return jsonify(message)

if __name__ == "__main__":
    app.run()