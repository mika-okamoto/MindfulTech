from flask import Flask, request, jsonify, Response
from flask_cors import CORS

import classify
import chat

app = Flask(__name__)
CORS(app)

class Server:
    def __init__(self):
        pass

    indexPredict = None
    indexLLMModel = None



@app.route("/predict", methods=['POST'])
def handle_prediction_request():
    content = request.json
    # TODO: Process input json into list of values for input into model

    #response = classify.predict(content, Server.indexPredict)
    # Response is 'Anxiety', 'Mood', or 'None'
    #Server.indexLLMModel[1] = []
    #Server.indexLLMModel[3] = response
    return jsonify({"content": "Anxiety"})


@app.route("/chat", methods=['POST'])
def handle_chat_request():
    content = request.json
    response = chat.chat(content.get('text'), Server.indexLLMModel)
    print(response)
    return jsonify({"content": response})


@app.route("/reset", methods=['GET'])
def reset():
    Server.indexLLMModel[1] = []
    Server.indexLLMModel[3] = None


if __name__ == "__main__":
    # launch server
    Server.indexPredict = classify.train()
    Server.indexLLMModel = chat.initModel()
    app.run()

    # initialize active models


