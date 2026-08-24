from country_code import *
from name_city import *
from Process_data import *
from weather import *
from key import *
from save_weather import *
def main():
    city = name_city()
    country = country_code()
    state = state_country(country)
    location = get_location(city,country,state)
    if location == None or location ==[]:
        print("location not fund !")
        return
    get_data = get_data_of_user(city,country,state)
    weather = get_weather(location["lat"],location["lon"])
    data = process_weather_data(get_data,weather)
    print_weather(data)
    fieldnames = get_fieldnames(data)
    check_saving =save_weather_to_csv(data,fieldnames)
    if check_saving == True:
        print("Weather result saved to weather_history.csv")
    else:
        print("The weather was received, but it could not be saved")           
main()