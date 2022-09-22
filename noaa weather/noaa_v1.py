import requests
from requests.exceptions import HTTPError
import json


class Noaa:
    class_headers = {"User-Agent": "(python_weather_demo, johnstraub1954@gmail.com)"}

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

    def get_grid_points(
            self,
            lat=None,
            lon=None,
            headers={"User-Agent": "(python_weather_demo, johnstraub1954@gmail.com)"}
    ):
        if lat is None:
            lat = self.lat
        if lon is None:
            lon = self.lon
        if lat is None or lon is None:
            message = f"invalid latitude ({lat}) and/or longitude ({lon})"
            raise exception(message)
        url = f"https://api.weather.gov/points/{lat},{lon}"
        response = self.__api_call(url)
        if response is not None:
            props = points["Properties"]
            self.grid_id = properties["gridId"]
            self.grid_x = properties["gridX"]
            self.grid_y = properties["gridY"]

    def __api_call(self, url, headers=class_headers, parameters=None):
        print("***" + str(url))
        print("###" + headers)
        decoded_response = None
        try:
            response = requests.get(url, headers=headers)
            self.latest_response = response
            print("    ### " + str(response.url))
            response.raise_for_status()

            if response.status_code == 200:
                decoded_response = json.loads(response.content.decode('utf-8'))

        except HTTPError as http_err:
            self.latest_error = http_err
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.latest_error = err
            print(f'Other error occurred: {err}')

        return decoded_response
