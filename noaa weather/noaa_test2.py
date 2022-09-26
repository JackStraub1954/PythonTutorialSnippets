from noaa_v1 import Noaa

noaaObj = Noaa(lat=47.44826277216945, lon=-121.77702114582527)
try:
    print("######## GRID POINTS ########")
    noaaObj.get_grid_points()
    if noaaObj.latest_response is not None:
        message = f"id={noaaObj.grid_id},gridX={noaaObj.grid_x},gridY={noaaObj.grid_y}"
        print(message)
    else:
        raise Exception(noaaObj.latest_error)

    print("######## FORECAST ########")
    response = noaaObj.get_forecast("SEW")
    if response is not None:
        print(">>> " + str(response))
    else:
        raise Exception(noaaObj.latest_error)

    print("######## GLOSSARY ########")
    response = noaaObj.get_glossary()
    if response is not None:
        pass  # print(">>> " + str(response))
    else:
        raise Exception(noaaObj.latest_error)

    print("######## STATION ########")
    response = noaaObj.get_station("TSR18")
    if response is not None:
        print(">>> " + str(response))
    else:
        raise Exception(noaaObj.latest_error)

    print("######## STATIONS ########")
    response = noaaObj.get_stations()
    if response is not None:
        print(">>> " + str(response))
    else:
        raise Exception(noaaObj.latest_error)

    print("######## STATION LATEST OBSERVATION ########")
    response = noaaObj.get_latest_for_station("TSR18")
    if response is not None:
        print(">>> " + str(response))
    else:
        raise Exception(noaaObj.latest_error)

except Exception as err:
    message = f"exception: {err}"
    print(message)
    raise
