"""Fetches Wave data from Weatherstack.com"""

import requests
import os
from datetime import date
import json


api_key = os.getenv("WEATHERSTACK_API_KEY")

param = "windSpeed"
# Connecting
response = requests.get(
    "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/cape%20town?unitGroup=metric&key=HFRTPS28BUTPP2XDVLZ2PLF92&contentType=json"
).json()
print(response)
# file = json.load(response)
# print(file)
# Ask for time surfed.

# Do something with response data.

# Serializing json
json_object = json.dumps(response, indent=4)

# Writing to sample.json
with open("visualcrossing.json", "w") as outfile:
    outfile.write(json_object)
# Ask for Spot surfed
# Ask for Rating out of 10 (float)
# Ask for comment
# Save to running CSV or google-sheet.
# Print output so you can get more in touch with what is going on .
