"""Fetches Wave data from stormglass.io"""

import requests
import os

api_key = os.getenv("API_KEY")

param = "windSpeed"
# connecting to luno
response = requests.get(
    "https://api.stormglass.io/v2/weather/point",
    params={
        "lat": -34.402377,
        "lng": 18.251149,
        # "params": ["windSpeed",
        # ]
    },
    headers={"Authorization": api_key},
)

# Ask for time surfed.

# Do something with response data.
json_data = response.json()
print(json_data)

# Ask for Spot surfed
# Ask for Rating out of 10 (float)
# Ask for comment
# Save to running CSV or google-sheet.
# Print output so you can get more in touch with what is going on .
""" get Tide

import arrow
import requests

start = arrow.now().floor('day')
end = arrow.now().shift(days=1).floor('day')

response = requests.get(
  'https://api.stormglass.io/v2/tide/extremes/point',
  params={
    'lat': 60.936,
    'lng': 5.114,
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp(),  # Convert to UTC timestam
  },
  headers={
    'Authorization': 'example-api-key'
  }
)

# Do something with response data.
json_data = response.json()


{
    "data": [
        {
            "height": "1.18",
            "time": "2019-03-15 03:40:44+00:00",
            "type": "high"
        },
        {
            "height": "0.60",
            "time": "2019-03-15 09:53:54+00:00",
            "type": "low"
        },
        {
            "height": "1.20",
            "time": "2019-03-15 16:23:29+00:00",
            "type": "high"
        },
        {
            "height": "0.61",
            "time": "2019-03-15 22:39:15+00:00",
            "type": "low"
        }
    ],
    "meta": {
        "cost": 1,
        "dailyQuota": 800,
        "end": "2019-03-16 00:00",
        "lat": 60.936,
        "lng": 5.114,
        "requestCount": 145,
        "start": "2019-03-15 00:00",
        "station": {
            "distance": 61,
            "lat": 60.398046,
            "lng": 5.320487,
            "name": "bergen",
            "source": "sehavniva.no"
        }
    }
}"""
