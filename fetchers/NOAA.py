"""Fetches Wave data from Weatherstack.com"""

import requests
import os
from datetime import date
import json


api_key = os.getenv("NOAA_API_KEY")

param = "windSpeed"
# Connecting
response = requests.get(
    "https://www.ncei.noaa.gov/cdo-web/api/v2/locations",
    headers={"token": api_key},
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
    "metadata": {"resultset": {"offset": 1, "count": 38862, "limit": 25}},
    "results": [
        {
            "mindate": "1983-01-01",
            "maxdate": "2022-10-05",
            "name": "Abu Dhabi, AE",
            "datacoverage": 0.99,
            "id": "CITY:AE000001",
        },
        {
            "mindate": "1944-03-01",
            "maxdate": "2022-10-05",
            "name": "Ajman, AE",
            "datacoverage": 0.9991,
            "id": "CITY:AE000002",
        },
        {
            "mindate": "1944-03-01",
            "maxdate": "2022-10-05",
            "name": "Dubai, AE",
            "datacoverage": 0.9991,
            "id": "CITY:AE000003",
        },
        {
            "mindate": "1944-03-01",
            "maxdate": "2022-10-05",
            "name": "Sharjah, AE",
            "datacoverage": 0.9991,
            "id": "CITY:AE000006",
        },
        {
            "mindate": "1966-03-02",
            "maxdate": "2021-08-30",
            "name": "Kabul, AF",
            "datacoverage": 0.9969,
            "id": "CITY:AF000007",
        },
        {
            "mindate": "1973-02-01",
            "maxdate": "2020-12-31",
            "name": "Kandahar, AF",
            "datacoverage": 1,
            "id": "CITY:AF000008",
        },
        {
            "mindate": "1877-04-01",
            "maxdate": "2022-10-05",
            "name": "Algiers, AG",
            "datacoverage": 1,
            "id": "CITY:AG000001",
        },
        {
            "mindate": "1909-11-01",
            "maxdate": "2022-10-05",
            "name": "Annaba, AG",
            "datacoverage": 1,
            "id": "CITY:AG000002",
        },
        {
            "mindate": "1973-04-01",
            "maxdate": "2022-10-05",
            "name": "Batna, AG",
            "datacoverage": 1,
            "id": "CITY:AG000003",
        },
        {
            "mindate": "1957-01-01",
            "maxdate": "2022-10-05",
            "name": "Bechar, AG",
            "datacoverage": 1,
            "id": "CITY:AG000004",
        },
        {
            "mindate": "1909-11-01",
            "maxdate": "2022-10-05",
            "name": "Bejaia, AG",
            "datacoverage": 1,
            "id": "CITY:AG000005",
        },
        {
            "mindate": "1880-05-01",
            "maxdate": "2022-10-05",
            "name": "Constantine, AG",
            "datacoverage": 1,
            "id": "CITY:AG000006",
        },
        {
            "mindate": "1995-10-01",
            "maxdate": "2022-10-05",
            "name": "Guelma, AG",
            "datacoverage": 1,
            "id": "CITY:AG000007",
        },
        {
            "mindate": "1888-01-01",
            "maxdate": "2022-10-05",
            "name": "Laghouat, AG",
            "datacoverage": 1,
            "id": "CITY:AG000008",
        },
        {
            "mindate": "1995-10-01",
            "maxdate": "2022-10-05",
            "name": "Medea, AG",
            "datacoverage": 0.991,
            "id": "CITY:AG000009",
        },
        {
            "mindate": "1976-04-01",
            "maxdate": "2022-10-05",
            "name": "Mostaganem, AG",
            "datacoverage": 1,
            "id": "CITY:AG000010",
        },
        {
            "mindate": "1957-01-01",
            "maxdate": "2022-10-05",
            "name": "Oran, AG",
            "datacoverage": 1,
            "id": "CITY:AG000011",
        },
        {
            "mindate": "1985-02-01",
            "maxdate": "2022-10-05",
            "name": "Oum el Bouaghi, AG",
            "datacoverage": 1,
            "id": "CITY:AG000012",
        },
        {
            "mindate": "1981-01-01",
            "maxdate": "2022-10-05",
            "name": "Saida, AG",
            "datacoverage": 1,
            "id": "CITY:AG000013",
        },
        {
            "mindate": "1995-10-01",
            "maxdate": "2022-10-05",
            "name": "Sidi-Bel-Abbes, AG",
            "datacoverage": 0.9995,
            "id": "CITY:AG000014",
        },
        {
            "mindate": "1957-12-31",
            "maxdate": "2022-10-05",
            "name": "Skikda, AG",
            "datacoverage": 0.9993,
            "id": "CITY:AG000015",
        },
        {
            "mindate": "1940-01-01",
            "maxdate": "2014-02-01",
            "name": "Tamanrasset, AG",
            "datacoverage": 0.9973,
            "id": "CITY:AG000016",
        },
        {
            "mindate": "1981-01-01",
            "maxdate": "2022-10-05",
            "name": "Tlemcen, AG",
            "datacoverage": 1,
            "id": "CITY:AG000017",
        },
        {
            "mindate": "1881-07-01",
            "maxdate": "1992-01-25",
            "name": "Baku, AJ",
            "datacoverage": 0.991,
            "id": "CITY:AJ000001",
        },
        {
            "mindate": "1925-09-01",
            "maxdate": "1991-12-31",
            "name": "Naxcivian, AJ",
            "datacoverage": 1,
            "id": "CITY:AJ000002",
        },
    ],
}
