import json


class statistics:
    """
    Calculations of statistics

    :Author: Lisa Wachter
    :Version: 2021-02-22
    """

    def s1_products_in_timespan(self, country, min, max, type=""):
        # data request for types in country and timespan + container CLOSED
        # TODO REST GET
        with open('../resources/s1_db_anfrage.json', 'r') as f:
            request = f.read()

        # convert request to json
        request_json = json.loads(request)
        print(request_json)

        # TODO calculate percentage and return new JSON



if __name__ == "__main__":
    s = statistics()
    s.s1_products_in_timespan("a", "1", "2")

s
