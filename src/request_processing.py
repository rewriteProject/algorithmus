from flask import Flask, request

app = Flask(__name__)


@app.route('/informations', methods=['POST', 'GET'])
def informations():



    pass


@app.route('/statistics', methods=['POST', 'GET'])
def statistics():
    pass


@app.route('/predictions', methods=['POST', 'GET'])
def predictions():
    pass

