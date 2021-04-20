import json

import requests


class statistics:
    """
    Calculations of statistics

    :Author: Lisa Wachter
    :Version: 2021-02-22
    """

    @staticmethod
    def s1_products_in_timespan(country, min, max, type=""):
        """
        Use Case S1
        Calculate the absolute and relative amount of a product category in a certain timespan.
        :param country: The specific country
        :param min: The start date of the calculation
        :param max: The end date of the calculation
        :param type: The product category (if none all product categories will be taken)
        :return: JSON with information
        """
        # data request for types in country and timespan + container CLOSED
        # REST GET
        if type == '':
            url = 'localhost:8081/analytics/statistics/{}/all'.format(country)
            params = {'minDate': min, 'maxDate': max}
            request = requests.post(url, params)
        else:
            url = 'localhost:8081/analytics/statistics/{}/{}'.format(country, type)
            print(url)
            params = {'minDate': min, 'maxDate': max}
            request = requests.post(url, params)

        with open('../resources/s1_db_anfrage.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)

        container = request_json['container']

        # calculate sum
        all_dict = {}
        for c in container['country']:
            for ma in container['country'][c]:
                all = 0
                for m in container['country'][c][ma]:
                    all += container['country'][c][ma][m]
                all_dict[ma] = all
        print(all_dict)

        # calculate percentage
        response_json = '{"container": {'
        i = 0
        for c in container['country']:
            i += 1
            i_c = 0

            response_json += '"{}": '.format(c)
            response_json += '{'

            for ma in container['country'][c]:
                i_c += 1
                i_ma = 0

                response_json += '"{}": '.format(ma)
                response_json += '{'

                for m in container['country'][c][ma]:
                    i_ma += 1

                    abs = container['country'][c][ma][m]
                    rel = (container['country'][c][ma][m]/all_dict[ma])*100

                    response_json += '"{}": '.format(m)
                    response_json += '{'
                    response_json += '"abs": {}, '.format(abs)
                    response_json += '"rel": {}'.format(rel)
                    if i_ma < len(container['country'][c][ma]):
                        response_json += '}, '
                    else:
                        response_json += '}'

                if i_c < len(container['country'][c]):
                    response_json += '}, '
                else:
                    response_json += '}'
            if i < len(container['country']):
                response_json += '}, '
            else:
                response_json += '}'

        response_json += '}}'
        print(response_json)
        return response_json


if __name__ == "__main__":
    statistics.s1_products_in_timespan("a", "1", "2")
