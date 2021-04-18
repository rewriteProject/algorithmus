from flask import Flask, request

app = Flask(__name__)


@app.route('/informations', methods=['POST'])
def informations():



    pass


@app.route('/statistics', methods=['POST'])
def statistics():
    pass


@app.route('/predictions', methods=['POST'])
def predictions():
    pass


if __name__ == "__main__":
    app.run()
