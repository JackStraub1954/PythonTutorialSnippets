from noaaV1.noaa_v1 import Noaa
from noaaV1.NOAAForecastResponse import NoaaForecastResponse
from noaaV1.NOAAPeriod import NOAAPeriod
import traceback

noaaObj = Noaa(lat=47.44840789954482, lon=-121.77699967729914)
try:
    response = noaaObj.get_grid_points()
    if response is None:
        raise Exception("no response from get_grid_points")
    response = noaaObj.get_forecast()
    fc_response = NoaaForecastResponse(response)
    coords = fc_response.coordinates(0)
    pstr = f'latitude: {coords["lat"]}'
    print(pstr)
    pstr = f'longitude: {coords["lon"]}'
    print(pstr)
    period1 = NOAAPeriod(response)
    print(period1.start_time)
    print(period1.icon)
    if period1.icon is not None:
        pass # period1.icon.show()
    print(period1.details_forecast)

except Exception as exc:
    message = f"Error: {exc}"
    print(message)
    print(noaaObj.latest_error)
    traceback.print_exc()
