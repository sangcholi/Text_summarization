from flask import Flask,jsonify, request
from model import ModelHandler

app = Flask(__name__)

model = ModelHandler()

@app.route('/', methods=['POST'])
def home():
    request_data = request.get_json()
    text = request_data['text']
    result = model.inference(text)
    return jsonify({"result":result})

@app.route("/health.json")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')