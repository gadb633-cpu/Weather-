import requests
import os
import json
from datetime import datetime, timedelta
import csv
from name_city import *
from country_code import *
from key import *
def get_location(city, country, state=""):     
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={get_key()}")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        if r.status_code == 401:
            print("Invalid API key")
        else:
            print(r.req.status_code)  
        return None    
    req= r.json() 
    if req == []:
        return []         
    location = {"lat":req[0]["lat"],"lon":req[0]["lon"]}
    return location  
def get_weather(latitude, longitude):
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=Metric&appid={get_key()}").json()
    return weather