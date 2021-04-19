import csv
import datetime
import json
import math
import statistics
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA


class predictions:
    """
    Calculation of predictions

    :Author: Lisa Wachter
    :Version: 2021-02-27
    """

    @staticmethod
    def p1_estimated_delivery(country):
        """
        Use Case P1
        Predicts the estimated delivery/closing date of a container that goes into a certain country
        :param country: the country the container will be delivered to
        :return: JSON with information
        """
        # **********************************************************************************************
        # ***** calculate average opening time of the containers that go into this certain country *****
        # **********************************************************************************************
        # data request from DB
        # create_date and close_date of closed containers (status=CLOSED)
        # from a specific country (e.g. China) from a specific timespan (e.g. last 2 years)
        # TODO REST GET Request as JSON
        with open('../resources/p1_db_anfrage_1.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)

        # calculate opening time
        open_times = []
        dates = request_json["container"]["dates"]
        for d in dates:
            open_date = datetime.strptime(dates[d]["open_date"], '%Y-%m-%d').date()
            close_date = datetime.strptime(dates[d]["close_date"], '%Y-%m-%d').date()
            duration = close_date - open_date
            dif = duration.days
            open_times.append(dif)
        open_times.sort()                                            # sort list for median calculation
        median = int(math.ceil(statistics.median(open_times)))       # calculate median
        median_days = pd.Timedelta(days=median)

        # **********************************************************************************************
        # *** calculate estimated delivery of the open conatiner that goes into this certain country ***
        # **********************************************************************************************
        # date request from DB
        # create_date of current container (status=OPEN) from certain country
        # TODO REST GET Requst as JSON
        with open('../resources/p1_db_anfrage_2.json', 'r') as f:
            request_2 = f.read()
        # convert request to json
        request_json_2 = json.loads(request_2)
        open_date_2 = request_json_2["container"]["create_date"]

        # calculate delivery date
        close_date_forecast = datetime.strptime(open_date_2, '%Y-%m-%d').date() + median_days

        # **********************************************************************************************
        # **************** calculate accuracy of the estimated delivery date prediction ****************
        # **********************************************************************************************
        # make array a numpy array
        open_times_numpy = np.array(open_times)
        # calculate absolute frequency
        count_median_abs = np.count_nonzero(open_times_numpy == median)
        # calculate relative frequency
        list_length = len(open_times)
        accuracy = (count_median_abs / list_length) * 100  # in percent

        # build response JSON
        response_json = '{"container": {'
        response_json += '"country": "{}", '.format(country)
        response_json += '"create_date": "{}", '.format(open_date_2)
        response_json += '"close_date_forecast": "{}", '.format(close_date_forecast)
        response_json += '"accuracy": "{}"'.format(accuracy)
        response_json += '}}'
        print(response_json)
        return response_json

    @staticmethod
    def p2_sales_prediction(country, f_type, feature):
        """
        Use Case P2
        Predicts the sales of a certain protuct type
        :return: JSON with information
        """
        # **********************************************************************************************
        # **************************************** data mining *****************************************
        # **********************************************************************************************
        # data request from DB
        # sold types from closed containers (status=CLOSED) from a specific country (e.g. China)
        # from a specific min time (e.g. 01-01-2020) in an specific intervall (e.g. m for months)
        # TODO REST GET Request as JSON
        with open('../resources/p2_db_anfrage.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)

        # convert to csv
        with open('data.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Date', 'Amount'])
            for c in request_json['container']['colors']:
                for t in request_json['container']['colors'][c]:
                    filewriter.writerow([t, request_json['container']['colors'][c][t]])

        # **********************************************************************************************
        # **************************************** handle data  ****************************************
        # **********************************************************************************************
        rcParams['figure.figsize'] = 10, 6

        # import data as csv
        dataset = pd.read_csv('data.csv', delimiter=',', encoding="utf-8-sig")

        # ready data
        dataset['Date'] = pd.to_datetime(dataset['Date'], infer_datetime_format=True)
        indexed_dataset = dataset.set_index(['Date'])
        #print("Dataset: {}".format(indexed_dataset))

        # plot original data
        #plt.xlabel('Date')
        #plt.ylabel('Amount')
        #print("Plotting original dataset")
        #plt.plot(indexed_dataset)

        # test stationary of indexed data
        #predictions.stationary_test(indexed_dataset)

        # **********************************************************************************************
        # ************************************ make data stationary *************************************
        # **********************************************************************************************
        # take the log of the data
        indexed_dataset_log_scale = np.log(indexed_dataset)
        #pd.set_option('display.max_rows', None)
        print("indexed_dataset_log_scale start")
        print(indexed_dataset_log_scale)
        print("indexed_dataset_log_scale end")
        #predictions.stationary_test(indexed_dataset_log_scale)

        # **********************************************************************************************
        # ************************************ timeseries analalysis ***********************************
        # **********************************************************************************************
        '''
        # seasonal analysis
        decomposition = seasonal_decompose(indexed_dataset_log_scale)
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
        residual.dropna(inplace=True)
        print("residual start")
        print(residual)
        print("residual end")

        plt.subplot(411)
        plt.plot(indexed_dataset_log_scale, label="Original")
        plt.legend(loc='best')
        plt.subplot(412)
        plt.plot(trend, label='Trend')
        plt.legend(loc='best')
        plt.subplot(413)
        plt.plot(seasonal, label='Seasonality')
        plt.legend(loc='best')
        plt.subplot(414)
        plt.plot(residual, label='Residuals')
        plt.legend(loc='best')
        plt.tight_layout()
        '''

        # **********************************************************************************************
        # ***************************************** ARIMA model ****************************************
        # **********************************************************************************************
        model = ARIMA(indexed_dataset_log_scale, order=(0, 1, 4))
        results_arima = model.fit(disp=-1)
        #plt.plot(dataset_log_diff_shifting)
        #plt.plot(results_arima.fittedvalues, color='red')
        #plt.title('RSS: %.4f' % sum((results_arima.fittedvalues - dataset_log_diff_shifting['Amount'])**2))

        # **********************************************************************************************
        # ***************************************** predictions ****************************************
        # **********************************************************************************************
        #print('Plotting ARIMA Model')
        #results_arima.plot_predict(1, 99)          # 75 rows + 2 years to predict = 99 steps
        x = results_arima.forecast(steps=24)        # 24 steps = 2 years
        #print(x)

        # **********************************************************************************************
        # ***************************************** build JSON *****************************************
        # **********************************************************************************************
        last_date = indexed_dataset.tail(1).index[0]
        date1 = last_date + pd.DateOffset(months=1)

        # build forecast as json
        forecast_json = '{ "forecast": { '

        # add average forecast
        forecast_json += '"averages": { '
        d = last_date + pd.DateOffset(months=1)
        i = 1
        for a in x[0]:
            if i < len(x[0]):
                forecast_json += '"{}": {}, '.format(str(d)[:10], math.exp(a))
            else:
                forecast_json += '"{}": {}'.format(str(d)[:10], math.exp(a))
            d = d + pd.DateOffset(months=1)
            i += 1
        forecast_json += ' }, '

        # add standard deviation
        forecast_json += '"deviations": { '
        d = last_date + pd.DateOffset(months=1)
        i = 1
        for s in x[1]:
            if i < len(x[1]):
                forecast_json += '"{}": {}, '.format(str(d)[:10], math.exp(s))
            else:
                forecast_json += '"{}": {}'.format(str(d)[:10], math.exp(s))
            d = d + pd.DateOffset(months=1)
            i += 1
        forecast_json += ' }, '

        # add confidence intervall
        forecast_json += '"confidence": { '
        d = last_date + pd.DateOffset(months=1)
        i = 1
        for c in x[2]:
            if i < len(x[2]):
                forecast_json += '"{}": '.format(str(d)[:10])
                forecast_json += '{ '
                forecast_json += '"lower": {},  '.format(math.exp(c[0]))
                forecast_json += '"upper": {}'.format(math.exp(c[1]))
                forecast_json += ' }, '
            else:
                forecast_json += '"{}": '.format(str(d)[:10])
                forecast_json += '{ '
                forecast_json += '"lower": {},  '.format(math.exp(c[0]))
                forecast_json += '"upper": {}'.format(math.exp(c[1]))
                forecast_json += ' }'
            d = d + pd.DateOffset(months=1)
            i += 1
        forecast_json += '}'
        forecast_json += '}}'
        forecast_json = json.loads(forecast_json)

        # add old data to forecast data
        response_json = "{ 'response': "
        response_json += "{},".format(request_json)
        response_json += "{}".format(str(forecast_json)[1:(len(str(forecast_json))-1)])
        response_json += "}"
        #print(response_json.replace("'", "\""))
        response_json = response_json.replace("'", "\"")

        # show plot
        #plt.show()

        # return JSON with information
        return response_json

    @staticmethod
    def stationary_test(timeseries):
        """
        Tests the stationaryity of timesries data
        :param timeseries: the timeseries data
        :return: non
        """
        # rolling statistics test
        moving_average = timeseries.rolling(window=12).mean()       # mean of 12 months
        moving_std = timeseries.rolling(window=12).std()            # standard deviation of 12 months

        orig = plt.plot(timeseries, color='blue', label='Orginial')
        mean = plt.plot(moving_average, color='red', label='Rolling Mean')
        std = plt.plot(moving_std, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')

        # Dickey-Fuller test
        print('Dickey-Fuller test results:')
        print(timeseries)
        dftest = adfuller(timeseries['Amount'], autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test statistic', 'p-value', '#Lags used', 'Number of observations used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value (%s)' % key] = value
        print(dfoutput)


if __name__ == "__main__":
    #predictions.p1_estimated_delivery('china')
    predictions.p2_sales_prediction('china', '2020-01-01', 'm')


