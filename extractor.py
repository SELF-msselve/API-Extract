import pandas as pd
import requests
from pprint import pprint

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,wind_speed_10m'
requests.get(url)