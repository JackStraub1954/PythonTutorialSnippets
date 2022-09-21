import requests
from requests.exceptions import HTTPError
import json


# properties key from POINTS request
props: str = "properties"

this_headers = {"User-Agent": "(python_weather_demo, johnstraub1954@gmail.com)"}
this_url = "https://api.weather.gov/points/{lat},{lon}"


class WeatherGetter:
    def __init__(self, location):
        self.location = location

    @staticmethod
    def __api_call(url, headers):
        print("***" + str(url))
        try:
            response = requests.get(url, headers=headers)
            print("    ### " + str(response.url))
            response.raise_for_status()

            if response.status_code == 200:
                return json.loads(response.content.decode('utf-8'))
            else:
                return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def get_nws_weather(self):
        points = self.__get_nws_points()
        # print(points)
        properties = points[props]
        office = properties["gridId"]
        grid_x = properties["gridX"]
        grid_y = properties["gridY"]
        url = f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast"
        return self.__api_call(url, this_headers)

    def __get_nws_points(self):
        lat = self.location["lat"]
        lon = self.location["lon"]

        url = f"https://api.weather.gov/points/{lat},{lon}"
        print(url)

        return self.__api_call(url, this_headers)
