from noaa_v1 import Noaa

noaaObj = Noaa(lat=47.4957, lon=-121.7868)
noaaObj.get_grid_points()
if noaaObj.latest_response is not None:
    message = f"id={noaaObj.grid_id},gridX={noaaObj.grid_x},gridY={noaaObj.grid_y}"
    print(message)
else:
    print(noaaObj.latest_error)
