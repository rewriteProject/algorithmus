import datetime
import json


class informations:
    """
    Simple information management and analysis

    :Author: Lisa Wachter
    :Version: 2021-02-21
    """

    def i1_container_overdue(self, country=''):
        """
        Use Case I1
        How many conatiners are still open?
        Which containers are still open and therefore overdue?
        Maximal opening period is 1 month.
        :param country: optional parameter if country is given
        :return: JSON with information
        """
        # data request for country, container_id, create_date with status = OPEN
        # TODO REST GET Request as JSON
        with open('../resources/i1_db_anfrage.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)

        # get current date
        curr_date = datetime.date.today()

        response_json = '{"container": {'
        containers = request_json['container']
        i = 0
        for c in containers['country']:
            i += 1

            response_json += '"{}": '.format(c)
            response_json += '{'

            # convert container_open_date to date-object
            # container_open_date format: 'year-month-day'
            container_date = datetime.datetime.strptime(containers['country'][c]['open_date'], '%Y-%m-%d').date()

            # comparison container_open_date with curr_date
            # 1 month = 4 weeks = 28 days
            diff = abs((curr_date - container_date).days)
            if diff >= 28:
                overdue = True
            else:
                overdue = False

            # build json infos
            response_json += '"container_id": {}, '.format(containers['country'][c]['container_id'])
            response_json += '"open_date": "{}", '.format(containers['country'][c]['open_date'])
            response_json += '"overdue": {}'.format(overdue)
            if i < len(request_json['container']):
                response_json += '}, '
            else:
                response_json += '}'

        response_json += '}}'
        print(response_json)

        # return json
        return response_json

    def i2_conatiner_utilization(self, country=''):
        """
        Use Case I2
        container weight utilization
        :param country: optional parameter if country is given
        :return: json with information
        """
        # data request for country, container_id, curr_weight_kg, max_weight_kg with status = OPEN
        # TODO REST GET Request as JSON
        with open('../resources/i2_db_anfrage.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)

        response_json = '{"container": {'
        containers = request_json['container']
        i = 0
        for c in containers['country']:
            i += 1

            response_json += '"{}": '.format(c)
            response_json += '{'

            # get maximal weight
            max_weight = containers['country'][c]['max_weight_kg']

            # get current weight
            curr_weight = containers['country'][c]['curr_weight_kg']

            # calculate utilization
            utilization = (curr_weight/max_weight)*100

            # build json infos
            response_json += '"container_id": {}, '.format(containers['country'][c]['container_id'])
            response_json += '"curr_weight_kg": {}, '.format(containers['country'][c]['curr_weight_kg'])
            response_json += '"max_weight_kg": {}, '.format(containers['country'][c]['max_weight_kg'])
            response_json += '"utilization": {}'.format(utilization)
            if i < len(request_json['container']):
                response_json += '}, '
            else:
                response_json += '}'

        response_json += '}}'
        print(response_json)

        # return json
        return response_json


if __name__ == "__main__":
    info = informations()
    info.i1_container_overdue()
    info.i1_container_overdue('china')
    info.i2_conatiner_utilization()
    info.i2_conatiner_utilization('china')
