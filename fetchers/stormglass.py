import requests
import arrow
import os
from datetime import date

start = arrow.get(date.today())
api_key = os.getenv("STORMGLASS_API_KEY")

response = requests.get(
    "https://api.stormglass.io/v2/tide/extremes/point",
    params={
        "lat": -34.402377,
        "lng": 18.251149,
        "start": start.to("UTC").timestamp(),  # Convert to UTC timestamp
        "end": start.shift(days=1).to("UTC").timestamp(),
    },
    headers={"Authorization": api_key},
)

# Do something with response data.
json_data = response.json()
print(json_data)
"""
{
    "data": [
        {
            "height": 0.51533429669708,
            "time": "2021-05-15T02:48:00+00:00",
            "type": "high",
        },
        {
            "height": -0.527363546598497,
            "time": "2021-05-15T09:01:00+00:00",
            "type": "low",
        },
        {
            "height": 0.44664058209590257,
            "time": "2021-05-15T15:18:00+00:00",
            "type": "high",
        },
        {
            "height": -0.38993344452907114,
            "time": "2021-05-15T21:15:00+00:00",
            "type": "low",
        },
    ],
    "meta": {
        "cost": 1,
        "dailyQuota": 10,
        "datum": "MSL",
        "end": "2021-05-16 00:00",
        "lat": -34.402377,
        "lng": 18.251149,
        "requestCount": 1,
        "start": "2021-05-15 00:00",
        "station": {
            "distance": 30,
            "lat": -34.183,
            "lng": 18.433,
            "name": "simonstown",
            "source": "sg",
        },
    },
}
"""
# {
#     "data": [
#         {
#             "height": 0.7040424965819757,
#             "time": "2022-10-10T01:20:00+00:00",
#             "type": "high",
#         },
#         {
#             "height": -0.7211373757208358,
#             "time": "2022-10-10T07:24:00+00:00",
#             "type": "low",
#         },
#         {
#             "height": 0.8241181704679359,
#             "time": "2022-10-10T13:33:00+00:00",
#             "type": "high",
#         },
#         {
#             "height": -0.7541569532473421,
#             "time": "2022-10-10T19:50:00+00:00",
#             "type": "low",
#         },
#     ],
#     "meta": {
#         "cost": 1,
#         "dailyQuota": 10,
#         "datum": "MSL",
#         "end": "2022-10-11 00:00",
#         "lat": -34.402377,
#         "lng": 18.251149,
#         "requestCount": 2,
#         "start": "2022-10-10 00:00",
#         "station": {
#             "distance": 30,
#             "lat": -34.183,
#             "lng": 18.433,
#             "name": "simonstown",
#             "source": "sg",
#         },
#     },
# }
