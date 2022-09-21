import requests
from requests.exceptions import HTTPError
import json


class Noaa:
    def __init__(
            self,
            lat: float = None,
            lon: float = None,
            grid_id: str = None,
            grid_x: int = None,
            grid_y: int = None,
            station_id: str = None,
            office_id: str = None
    ):
        self.lat = lat
        self.lon = lon
        self.grid_id = grid_id
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.station_id = station_id
        self.office_id = office_id

        self.latest_response = None
        self.latest_error = None
        self.latest_url = None

    def __api_call(self, url, headers):
        print("***" + str(url))
        try:
            response = requests.get(url, headers=headers)
            self.latest_response = response
            print("    ### " + str(response.url))
            response.raise_for_status()

            if response.status_code == 200:
                return json.loads(response.content.decode('utf-8'))
            else:
                return None
        except HTTPError as http_err:
            self.latest_error = http_err
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.latest_error = err
            print(f'Other error occurred: {err}')
