import pywapi, os, sys

class weatherClass:
    def init(x):
        if "weather" in x:
            pragueWeather = pywapi.get_weather_from_weather_com("EZXX0012", units="metric")
            print("Conditions : " + pragueWeather['current_conditions']['text'])
            print("Temperature : " + pragueWeather['current_conditions']['temperature'])
        
