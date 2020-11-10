# This script gives the current weather according to your location

# Fields of interests ==> Temperature, humidity, rainfall

import requests, json

api_key = "9d7cde1f6d07ec55650544be1631307e"

base_url  = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]

    weather_description = z[0]["description"]

    print("Temperature (in kelvin unit) = " + str(current_temperature))
    print("Atmospheric Pressure (in hPa unit) = " + str(current_pressure))
    print("Humidity (in percentage) = " + str(current_humidity))
    
else:
    print("City not found")


