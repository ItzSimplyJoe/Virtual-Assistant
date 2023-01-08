from assistant_functions.determine_most_similar import determine_most_similar_phrase
import geocoder
from assistant_functions.speak_listen import speak_listen
class Location:

    def main(self, text, intent, uuid, choice):
        samples = {
            "where are we" : {'function' : self.say_location, 'type' : 'location'},
            "location" : {'function' : self.say_location, 'type' : 'location'},
            "city" : {'function' : self.say_location, 'type' : 'city'},
            "state" : {'function' : self.say_location, 'type' : 'state'},
            "country" : {'function' : self.say_location, 'type' : 'country'}
        }

        most_similar = determine_most_similar_phrase(text, samples)
        function = samples[most_similar]['function']
        function(samples[most_similar]['type'], uuid)

    def get_lat_lng(self,uuid):
        g = geocoder.ip('me')
        return g.latlng[0], g.latlng[1]

    def get_city_state_country(self, uuid):
        g = geocoder.ip('me')

        return [g.city, g.state, g.country]

    def say_location(self, type, uuid):
        if type == 'location':
            print(" ".join(self.get_city_state_country(uuid)))
            speak_listen.say(" ".join(self.get_city_state_country(uuid)), uuid)
        if type == 'city':
            print(self.get_city_state_country(uuid)[0])
            speak_listen.say(self.get_city_state_country(uuid)[0], uuid)
        if type == 'state':
            print(self.get_city_state_country(uuid)[0])
            speak_listen.say(self.get_city_state_country(uuid)[1], uuid)
        if type == 'country':
            print(self.get_city_state_country(uuid)[0])
            speak_listen.say(self.get_city_state_country(uuid)[2], uuid)

location = Location()