import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta
import csv
from name_city import *
from country_code import *
def get_key():
    load_dotenv()
    SECRET_KEY = os.getenv('API_key')
    return SECRET_KEY
def get_location(city, country, state=""):
    limit = 1        
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={get_key()}")
    req = r.json()
    if req == []:
        return "Location not found !"
    location = [req[0]["lat"],req[0]["lon"]]
    return location  