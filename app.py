from flask import Flask,jsonify, request
from model import ModelHandler

app = Flask(__name__)

model = ModelHandler()

@app.route('/', methods=['POST'])
def home():
    request_data = request.get_json()
    text = request_data['text']
    result = model.handle(text)
    return jsonify({"result":result})


    
if __name__ == '__main__':
    app.run(debug=True)