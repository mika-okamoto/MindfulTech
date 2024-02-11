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
        '100-500': 3,
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

    survey = f"Age: {content.get('1')}\nGender: {content.get('2')}\nNumber of Employees at Company: {content.get('3')}\n" + \
                f"Does remote work: {content.get('4')}\nFamily history of mental disorders: {content.get('6')}\n" + \
                f"Does your employer offer resources to learn more about mental health concerns and options for seeking help?: {content.get('7')}\n" + \
                f"Do you think that discussing a mental health disorder with your employer would have negative consequences?: {content.get('8')}\n" + \
                f"Would you feel comfortable discussing a mental health disorder with your fellow employees?: {content.get('9')}\n" + \
                f"Do you feel that being identified as a person with a mental health issue would hurt your career?: {content.get('10')}\n" + \
                f"How willing would you be to share with friends and family that you have a mental illness?: {content.get('11')}\n" + \
                f"Do you believe your productivity/work is ever affected by a mental health issue?: {content.get('12')}"
    
    response = classify.predict(formatted, Server.indexPredict)
    # Response is 'Anxiety', 'Mood', or 'None'
    Server.indexLLMModel[1] = []
    Server.indexLLMModel[3] = response
    Server.indexLLMModel[4] = survey
    return jsonify({"content": response})


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
    Server.indexLLMModel[4] = ""


if __name__ == "__main__":
    # launch server
    Server.indexPredict = classify.train()
    Server.indexLLMModel = chat.initModel()
    app.run()

    # initialize active models
