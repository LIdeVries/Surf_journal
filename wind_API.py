"""Fetches Wave data from Weatherstack.com"""

import requests
import os
from datetime import date

user = "Luke"
api_key = os.getenv("WEATHERSTACK_API_KEY")

param = "windSpeed"
# connecting to luno
response = requests.get(
    "http://api.weatherstack.com/current?access_key="
    + api_key
    + "&query="
    + "New York"
    + "& historical_date ="
    + str(date.today())
)
print(response)
# Ask for time surfed.

# Do something with response data.


# Ask for Spot surfed
# Ask for Rating out of 10 (float)
# Ask for comment
# Save to running CSV or google-sheet.
# Print output so you can get more in touch with what is going on .
