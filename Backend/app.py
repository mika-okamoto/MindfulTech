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
    # might need to process content into correct format
    response = classify.predict(content, indexTrain)

    # Response is 'Anxiety', 'Mood', or 'None'
    indexLLMModel[3] = response
    return jsonify({"content": response})


@app.route("/chat", methods=['POST'])
def handle_chat_request():
    content = request.json
    response = chat.chat(content, indexLLMModel)
    return jsonify({"content": response})


@app.route("/reset", methods=['GET'])
def reset():
    indexLLMModel[1] = []
    indexLLMModel[3] = 'Anxiety'


if __name__ == "__main__":
    # launch server
    app.run()

    # initialize active models
    indexTrain = classify.train()
    indexLLMModel = chat.initModel()
