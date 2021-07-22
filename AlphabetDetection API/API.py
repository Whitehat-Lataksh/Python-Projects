from logging import debug
from re import L
from flask import Flask, jsonify, request
from AlphabetModel import prediction


app = Flask(__name__)

@app.route("/predict-aplhabet", methods = ["POST"])

def predictAlphabet():
    image = request.files.get("alphabet")

    predict = prediction(image)

    return jsonify({
        "prediction" : predict
    }), 200

if __name__ == "__main__":
    app.run(debug = True)
