from weather import *
from country_code import *
from name_city import *
from datetime import datetime
def process_weather_data(location, weather):
    data = {
    "search_time": datetime.now(),   
    "city": location["city"],
    "state": location["state"],
    "country": location["country"],
    "temperature": weather["main"]["temp"],
    "feels_like":weather["main"]["feels_like"] ,
    "condition": weather["weather"][0]["description"],
    "humidity":weather["main"]["humidity"]  ,
    "wind_speed":weather["wind"]["speed"]}
    return data
def print_weather(weather_result):
    print(f"search_time: {weather_result["search_time"]}\ncity: {weather_result["city"]}\nstate: {weather_result["state"]}\ncountry: {weather_result["country"]}\ntemperature: {weather_result["temperature"]}\nfeels_like: {weather_result["feels_like"]}\ncondition: {weather_result["condition"]}\nhumidity: {weather_result["humidity"]}\nwind_speed: {weather_result["wind_speed"]}")

