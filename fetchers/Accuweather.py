"""Fetches Wave data from Weatherstack.com"""

import requests
import os
from datetime import date
import json


api_key = os.getenv("WEATHERSTACK_API_KEY")

param = "windSpeed"
# Connecting
response = requests.get(
    "http://api.weatherstack.com/current?access_key="
    + api_key
    + "&query="
    + "Cape Town"
    + "& historical_date = "
    + str(date.today())
    + "hourly = 1"
).json()
print(response)
# file = json.load(response)
# print(file)
# Ask for time surfed.

# Do something with response data.


# Ask for Spot surfed
# Ask for Rating out of 10 (float)
# Ask for comment
# Save to running CSV or google-sheet.
# Print output so you can get more in touch with what is going on .

{
    "request": {
        "type": "City",
        "query": "Cape Town, South Africa",
        "language": "en",
        "unit": "m",
    },
    "location": {
        "name": "Cape Town",
        "country": "South Africa",
        "region": "Western Cape",
        "lat": "-33.917",
        "lon": "18.417",
        "timezone_id": "Africa/Johannesburg",
        "localtime": "2022-10-07 17:20",
        "localtime_epoch": 1665163200,
        "utc_offset": "2.0",
    },
    "current": {
        "observation_time": "03:20 PM",
        "temperature": 18,
        "weather_code": 113,
        "weather_icons": [
            "https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
        ],
        "weather_descriptions": ["Sunny"],
        "wind_speed": 31,
        "wind_degree": 190,
        "wind_dir": "S",
        "pressure": 1020,
        "precip": 0,
        "humidity": 64,
        "cloudcover": 0,
        "feelslike": 18,
        "uv_index": 5,
        "visibility": 10,
        "is_day": "yes",
    },
}
