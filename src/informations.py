import datetime
import json


class informations:
    """
    Simple information management and analysis
    UseCase I1 and I2

    :Author: Lisa Wachter
    :Version: 2021-02-21
    """

    def container_overdue(self, country=''):
        """
        Use Case I1
        How many conatiners are still open?
        Which containers are still open and therefore overdue?
        Maximal opening period is 1 month.
        :param country: optional parameter if country is given
        :return: json with information
        """
        # data request for country, container_id, create_date with status = OPEN
        # TODO REST GET Request as JSON
        if country != '':
            request = '{"container": {' \
                          '"china" : {"container_id" : 1, "open_date" : "2021-01-30"}' \
                          '}}'
        else:
            request = '{"container": {' \
                          '"china" : {"container_id" : 1, "open_date" : "2021-01-30"},' \
                          '"russia" : {"container_id" : 2, "open_date" : "2021-01-24"},' \
                          '"usa" : {"container_id" : 3, "open_date" : "2021-01-19"}' \
                          '}}'

        # convert request to json
        request_json = json.loads(request)
        print(request_json)
        print(request_json['container'])
        print(len(request_json['container']))

        # get current date
        curr_date = datetime.date.today()
        print('current date: {}'.format(curr_date))

        response_json = '{"container: {'
        containers = request_json['container']
        i = 0
        for c in containers:
            i += 1

            response_json += '{}: '.format(c)
            response_json += '{'

            # convert container_open_date to date-object
            # container_open_date format: 'year-month-day'
            container_date = datetime.datetime.strptime(containers[c]['open_date'], '%Y-%m-%d').date()
            print('{}: {}'.format(c, container_date))

            # comparison container_open_date with curr_date
            # 1 month = 4 weeks = 28 days
            diff = abs((curr_date - container_date).days)
            print(diff)
            if diff >= 28:
                overdue = True
            else:
                overdue = False

            # build json infos
            response_json += '"container_id": {}, '.format(containers[c]['container_id'])
            response_json += '"open_date": {}, '.format(containers[c]['open_date'])
            response_json += '"overdue": {}'.format(overdue)
            if i < len(request_json['container']):
                response_json += '}, '
            else:
                response_json += '}'

        response_json += '}}'
        print(response_json)

        # return json
        return response_json

    def conatiner_utilization(self, country: str):
        """
        Use Case I2
        :return: json with information
        """
        pass


if __name__ == "__main__":
    info = informations()
    info.container_overdue()



