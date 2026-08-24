from country_code import *
from name_city import *
from Process_data import *
from weather import *
from key import *
def main():
    city = name_city()
    country = country_code()
    state = state_country(country)
    location = get_location(city,country,state)
    get_data = get_data_of_user(city,country,state)
    weather = get_weather(location["lat"],location["lon"])
    data = process_weather_data(get_data,weather)
    print_weather(data)
main()
