from flask import Flask, request, jsonify
import classify
import chat

app = Flask(__name__)


class Server:
    def __init__(self):
        pass

    indexPredict = None
    indexLLMModel = None


@app.route("/predict", methods=['POST'])
def handle_prediction_request():
    content = request.json
    # TODO: Process input json into list of values for input into model

    response = classify.predict(content, indexTrain)
    # Response is 'Anxiety', 'Mood', or 'None'
    indexLLMModel[1] = []
    indexLLMModel[3] = response
    return jsonify({"content": response})


@app.route("/chat", methods=['POST'])
def handle_chat_request():
    content = request.json
    # TODO: Process chat content into input string

    response = chat.chat(content, indexLLMModel)
    return jsonify({"content": response})


@app.route("/reset", methods=['GET'])
def reset():
    indexLLMModel[1] = []
    indexLLMModel[3] = None


if __name__ == "__main__":
    # launch server
    app.run()

    # initialize active models
    indexTrain = classify.train()
    indexLLMModel = chat.initModel()
