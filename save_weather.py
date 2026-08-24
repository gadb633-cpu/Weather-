import os
import csv
def save_weather_to_csv(weather_result,fieldnames):
    try:
        if os.path.exists("weather_history.csv"):
            with open('weather_history.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=fieldnames,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                writer.writerow(weather_result)
                return True
        else:
            with open('weather_history.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile,fieldnames=fieldnames,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()
                writer.writerow(weather_result) 
                return True          
    except Exception as error:
         print(type(error).__name__)
         return False