from WeatherGetter import *
from datetime import timezone
from dateutil.parser import parse


def utc_to_local_string(utc_time):
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(tz=None)
    formatted_datetime = local_time.strftime("%a, %d-%b-%Y at %H:%M:%S")
    return formatted_datetime


def main():
    location = {"lat": 47.4957, "lon": -121.7868}
    test = WeatherGetter(location)
    output = test.get_nws_weather()
    # print(output)
    for key in output:
        print(key + ": " + str(output[key]))

    print("#####################")
    props = output["properties"]
    updated_time = props["updated"]
    parsed_time = parse(updated_time)
    strf_datetime = utc_to_local_string(parsed_time)
    print("updated: " + strf_datetime)
    periods = props["periods"]
    # print(str(type(periods)) + ": " + str(periods))
    for period in periods:
        period_time = period["startTime"]
        print("    " + period_time)
        parsed_period = parse(period_time)
        strf_datetime = utc_to_local_string(parsed_period)
        print("        " + strf_datetime)


if __name__ == '__main__':
    main()
