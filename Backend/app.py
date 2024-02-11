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
    print(content)
    genders = {
        'male': 0,
        'female': 2,
        'other': 1
    }
    emp_count = {
        '1-5': 0,
        '6-25': 1,
        '26-100': 2,
        '101-500': 3,
        '501-1000': 4,
        '1000+': 5
    }

    remote_work = {
        'always': 1,
        'sometimes': 0.5,
        'never': 0
    }

    disorder = {
        'mood disorder': 2,
        'anxiety': 1,
        'no': -1
    }

    family = {
        'yes': 1,
        'no': 0,
        "i don't know": 0.5,
        "maybe": 0.5
    }

    num_10 = {
        'strong no': 1,
        'little no': 2,
        'maybe': 3,
        'little yes': 4,
        'strong yes': 5
    }

    sharing = {
        "n/a": 0,
        "not open at all": 1,
        "somewhat not open": 2,
        "neutral": 3,
        "somewhat open": 4,
        "very open": 5
    }

    productivity = {
        "n/a": -1,
        'never': 0,
        'rarely': 1,
        'sometimes': 2,
        'often': 3
    }

    formatted = [int(content.get('1')), genders[content.get('2')], emp_count[content.get('3')], remote_work[content.get('4')],
             disorder[content.get('5')], family[content.get('6')],
             family[content.get('7')], family[content.get('8')], family[content.get('9')], num_10[content.get('10')],
             sharing[content.get('11')], productivity[content.get('12')]]
    print(formatted)

    # response = classify.predict(content, Server.indexPredict)
    # Response is 'Anxiety', 'Mood', or 'None'
    # Server.indexLLMModel[1] = []
    # Server.indexLLMModel[3] = response
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
