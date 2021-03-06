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
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA, ARIMA_DEPRECATION_WARN



class predictions:
    """
    Calculation of predictions

    :Author: Lisa Wachter
    :Version: 2021-02-27
    """

    def p1_estimated_delivery(self, country):
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
        average_times = []
        dates = request_json["container"]["dates"]
        for d in dates:
            open_date = datetime.strptime(dates[d]["open_date"], '%Y-%m-%d').date()
            close_date = datetime.strptime(dates[d]["close_date"], '%Y-%m-%d').date()
            duration = close_date - open_date
            dif = duration.days
            average_times.append(dif)
        average_times.sort()  # sort list for median calculation
        median = int(math.ceil(statistics.median(average_times)))  # calculate median
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
        average_times_numpy = np.array(average_times)
        # calculate absolute frequency
        count_median_abs = np.count_nonzero(average_times_numpy == median)
        # calculate relative frequency
        list_length = len(average_times)
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

    def p2_sales_prediction(self, country, min_time, intervall):
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
        # TODO make new MockData
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
        #print(indexed_dataset)
        mean = indexed_dataset.mean(axis=0)
        #print("mean: {}".format(mean))
        median = indexed_dataset.median(axis=0)
        #print("median: {}".format(median))


        # plot original data
        plt.xlabel('Date')
        plt.ylabel('Amount')
        #plt.plot(indexed_dataset)

        # test stationary of indexed data
        #self.stationary_test(indexed_dataset)

        # **********************************************************************************************
        # ************************************ make data stationary *************************************
        # **********************************************************************************************
        # take the log of the data
        indexed_dataset_log_scale = np.log(indexed_dataset)
        #pd.set_option('display.max_rows', None)

        print("indexed_dataset_log_scale start")
        print(indexed_dataset_log_scale)
        print("indexed_dataset_log_scale end")
        #moving_average = indexed_dataset_log_scale.rolling(window=12).mean()
        #indexed_dataset_log_scale_minus_moving_average = (indexed_dataset_log_scale - moving_average)

        # remove NaN values
        #indexed_dataset_log_scale_minus_moving_average.dropna(inplace=True)
        #indexed_dataset_log_scale_minus_moving_average.fillna(0)
        # TODO NAN vs NA values rausnehmen
        # TODO alle 0 werte zu einem 1 machen - log(1) = 0 // befor ich log anwende

        #print("start 1")
        #print(indexed_dataset_log_scale_minus_moving_average)
        #print("end 1")

        # test stationary of data
        #self.stationary_test(indexed_dataset_log_scale_minus_moving_average)

        # exponential transformation
        #exponential_decay_weight_average = indexed_dataset_log_scale.ewm(halflife=12, min_periods=0, adjust=True).mean()
        #plt.plot(indexed_dataset_log_scale)
        #plt.plot(exponential_decay_weight_average, color='red')

        # log scale - weigthed average transformation
        #dataset_log_scale_minus_moving_exponential_decay_average = indexed_dataset_log_scale - exponential_decay_weight_average
        #self.stationary_test(dataset_log_scale_minus_moving_exponential_decay_average)

        # **********************************************************************************************
        # ************************************ timeseries analalysis ***********************************
        # **********************************************************************************************
        dataset_log_diff_shifting = (indexed_dataset_log_scale - indexed_dataset_log_scale.shift(fill_value=0))
        print("dataset_log_diff_shifting start")
        print(dataset_log_diff_shifting)
        print("dataset_log_diff_shifting end")
        plt.plot(dataset_log_diff_shifting)
        dataset_log_diff_shifting.dropna(inplace=True)
        #self.stationary_test(dataset_log_diff_shifting)

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

        decomposed_log_data = residual
        decomposed_log_data.dropna(inplace=True)
        print("decomposed_log_data start")
        print(decomposed_log_data)
        print("decomposed_log_data end")
        self.stationary_test(decomposed_log_data)      # TODO error occurs
        '''

        '''
        # ACF & PACF plots
        lag_acf = acf(dataset_log_diff_shifting, nlags=20)
        lag_pacf = pacf(dataset_log_diff_shifting, nlags=20, method='ols')


        # autocorrelation graph (for Q)
        plt.subplot(121)
        plt.plot(lag_acf)
        plt.axhline(y=0, linestyle='--', color='gray')
        plt.axhline(y=-1.96/np.sqrt(len(dataset_log_diff_shifting)), linestyle='--', color='gray')
        plt.axhline(y=1.96/np.sqrt(len(dataset_log_diff_shifting)), linestyle='--', color='gray')
        plt.title('Autocorrelation function')

        # partial atocorrelation graph (for P)
        plt.subplot(122)
        plt.plot(lag_pacf)
        plt.axhline(y=0, linestyle='--', color='gray')
        plt.axhline(y=-1.96/np.sqrt(len(dataset_log_diff_shifting)), linestyle='--', color='gray')
        plt.axhline(y=1.96/np.sqrt(len(dataset_log_diff_shifting)), linestyle='--', color='gray')
        plt.title('Partial Autocorrelation function')
        plt.tight_layout()
        '''

        # https://www.youtube.com/watch?v=e8Yw4alG16Q - 31:00

        # **********************************************************************************************
        # ***************************************** ARIMA model ****************************************
        # **********************************************************************************************

        print("indexed_dataset_log_scale")
        pd.set_option('display.max_rows', None)
        print(indexed_dataset_log_scale)
        model = ARIMA(indexed_dataset_log_scale, order=(0, 1, 4))
        results_arima = model.fit(disp=-1)
        #plt.plot(dataset_log_diff_shifting)
        #plt.plot(results_arima.fittedvalues, color='red')
        #plt.title('RSS: %.4f' % sum((results_arima.fittedvalues - dataset_log_diff_shifting['Amount'])**2))
        print('Plotting ARIMA Model')

        # **********************************************************************************************
        # ***************************************** predictions ****************************************
        # **********************************************************************************************
        
        predictions_arima_diff = pd.Series(results_arima.fittedvalues, copy=True)
        print("predictions_arima_diff")
        print(predictions_arima_diff.head())

        # convert to cumulative sum
        predictions_arima_diff_cumsum = predictions_arima_diff.cumsum()
        print("predictions_arima_diff_cumsum")
        print(predictions_arima_diff_cumsum.head())

        predictions_arima_log = pd.Series(indexed_dataset_log_scale['Amount'], index=indexed_dataset_log_scale.index)
        predictions_arima_log = predictions_arima_log.add(predictions_arima_diff_cumsum, fill_value=0)
        print("testtest start")
        print('a: {}'.format(predictions_arima_log.head()))
        print("testtest end")

        predictions_arima = np.exp(predictions_arima_log)
        plt.plot(indexed_dataset, color='black')
        plt.plot(predictions_arima, color='red')

        # predict future values
        #print(indexed_dataset_log_scale)
        results_arima.plot_predict(1, 99)           # 75 rows + 2 years to predict = 99 steps
        x = results_arima.forecast(steps=24)
        print(x)

        # show plot
        plt.show()

        # TODO sending JSON back

    def stationary_test(self, timeseries):
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
    pred = predictions()
    #pred.p1_estimated_delivery('china')
    pred.p2_sales_prediction('china', '2020-01-01', 'm')


