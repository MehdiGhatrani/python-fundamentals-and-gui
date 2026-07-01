# import modules and global variable
from abc import ABC, abstractmethod
import requests


# abstract class

class WeatherAbstract(ABC):

    @abstractmethod
    def get_current_weather(self, lat, lng):
        pass

# get cuurent weather from openmeteo

class OpenMeteoWeather(WeatherAbstract):

    base_url = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self, lat, lng):
        params = {
            "latitude" : lat,
            "longitude" : lng,
            "current" : "temperature_2m,relative_humidity_2m,is_day"
        }
        response = requests.get(self.base_url,params=params)

        normalize_response = {
            "temp": response.json()["current"]["temperature_2m"],
            "humidity": response.json()["current"]["relative_humidity_2m"],
            "is day?": "is day" if response.json()["current"]["is_day"] == "1" else "is night",
            
        }

        return normalize_response
    


latitude = 30.437091 
longitude = 48.199022

current_weather = OpenMeteoWeather()
print(current_weather.get_current_weather(latitude, longitude))