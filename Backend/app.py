from flask import Flask, request, jsonify
from flask_cors import CORS

class Server:
    def __init__(self):
        pass

    index = None

@app.route("/predict", methods=['POST'])
def handle_prediction_request():
    content = request.json
    response = query(content) # params filler for later

    return jsonify({"content": response})

@app.route("/chat", methods=['POST'])
def handle_chat_request():
    content = request.json
    response = chat(content)  # params filler for later, implement methods
    return jsonify({"content": response})


if __name__ == "__main__":
    # launch server
    app.run()

    # load any models that we want continually active into the Server

    # test request
    res = requests.post('http://localhost:5000/predict', json={}) # survey responses
    res2 = requests.post('http://localhost:5000/chat', json={}) # further questions from user
    print(res.json())
    print(res2.json())

