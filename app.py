from flask import Flask,jsonify, request
from model import ModelHandler
import torch
app = Flask(__name__)

device='cuda' if torch.cuda.is_available() else 'cpu' 

model = ModelHandler()
model = model.to(device)

@app.route('/', methods=['POST'])
def home():
    request_data = request.get_json()
    text = request_data['text'].to(device)
    result = model.inference(text)
    return jsonify({"result":result})

@app.route("/health.json")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')