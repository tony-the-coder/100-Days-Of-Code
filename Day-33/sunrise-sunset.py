import requests
from datetime import datetime

"""Basic API call for the Runrise and Sunset times"""


def my_sunrise_api_call(
    MY_LAT=39.863392, MY_LONG=-81.907509, MY_TZ="America/Kentucky/Louisville"
):
    """You would think that the course would have mentioned how to set the timezone. Good thing there is documentation. It was not that helpful, but it still made sense."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": MY_TZ,
    }

    url = "https://api.sunrise-sunset.org/json"

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)
    """Part of the course to get just the hour, but it does not seem very useful. Right now, the API is returning the time in UTC+0."""

    timenow = datetime.now()
    # print(timenow.hour)

    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0].split("-")
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0].split("-")
    print(f"The sunrise is at {sunrise[0]}")
    print(f"The sunset is at {sunset[0]}")


my_sunrise_api_call()
