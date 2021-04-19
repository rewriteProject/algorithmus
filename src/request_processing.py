import json

from flask import Flask, request
from werkzeug.exceptions import abort

import informations
import satistics
import predictions

app = Flask(__name__)


@app.route('/informations', methods=['POST'])
def informations_route():
    """
    Routes the informations
        case (I1 or I2)
        country
    :return:
    """
    if request.form['case'] == "I1":
        response = informations.informations.i1_container_overdue(request.form['country'])
        response = json.loads(response)
        print(response)
        return response
    elif request.form['case'] == "I2":
        response = informations.informations.i2_container_utilization(request.form['country'])
        response = json.loads(response)
        print(response)
        return response
    else:
        return abort(404)


@app.route('/statistics', methods=['POST'])
def statistics_route():
    """
    Routes the statistics
        case (S1)
        country
        min
        max
        type
    :return:
    """
    if request.form['case'] == "S1":
        response = satistics.statistics.s1_products_in_timespan(
            request.form['country'], request.form['min'], request.form['max'], request.form['type'])
        response = json.loads(response)
        print(response)
        return response
    else:
        return abort(404)


@app.route('/predictions', methods=['POST'])
def predictions_route():
    """
    Routes the predictions
        case (P1 or P2)
        country
        (feature_type)
        (feature)
    :return:
    """
    if request.form['case'] == "P1":
        response = predictions.predictions.p1_estimated_delivery(request.form['country'])
        response = json.loads(response)
        print(response)
        return response
    elif request.form['case'] == "P2":
        response = predictions.predictions.p2_sales_prediction(
            request.form['country'], request.form['feature_type'], request.form['feature'])
        response = json.loads(response)
        print(response)
        return response
    else:
        return abort(404)


if __name__ == "__main__":
    app.run()
