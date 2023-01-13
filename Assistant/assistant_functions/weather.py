import requests
import json
from assistant_functions.location import Location
from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import pyowm


class Weather:
    def __init__(self):
        with open(r"C:\Users\Owner\OneDrive\Desktop\keys.key", "r") as file:
            for line in file:
                key1,key2,key3 = line.rstrip("\n").split(",")
        self.own= pyowm.OWM(key3).weather_manager()

    def main(self, text, intent, uuid, choice):
        samples = {
            'what is the weather' : {'function' : self.get_weather_at_current_location, 'type' : 'weather'},
            'whats the temperature' : {'function' : self.get_weather_at_current_location, 'type' : 'temperature'},
            'whats the humidity' : {'function' : self.get_weather_at_current_location, 'type' : 'humidity'},
            'whats the forecast' : {'function' : self.get_weather_forecast, 'type' : 'forecast'},
            'what will the weather be like tomorrow' : {'function' : self.get_weather_forecast, 'type' : 'forecast'},
        }

        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['function']
        tempvar = func(samples[most_similar]['type'], uuid)
        print(tempvar)
        speak_listen.say(tempvar,uuid)
    
    def get_weather_at_current_location(self, type, uuid):
        lat, lng = location.get_lat_lng(uuid)
        weather = self.own.weather_at_coords(lat, lng).weather
        city = location.get_city_state_country(uuid)[0]
        temperature = int(round(weather.temperature(unit='celsius')['temp'], 0))

        if type == 'temperature':
            return f"Currently, the temperature in {city} is {temperature} degrees"
        elif type == 'humidity':
            return f"Currently, the humidity in {city} is {weather.humidity} percent"
        elif type == 'weather':
            return f"Currently in {city}, it's {temperature} degrees and {weather.detailed_status}"

    def get_weather_forecast(self,tempvar, uuid):
        location = Location()
        lat, lng = location.get_lat_lng(uuid)

        r = requests.get(f'https://api.weather.gov/points/{lat},{lng}')
        response = json.loads(r.text)
        r = requests.get(response['properties']['forecast'])
        response = json.loads(r.text)

        return response['properties']['periods']

location = Location()

weather = Weather()
