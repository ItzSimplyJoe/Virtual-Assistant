from assistant_functions.speak_listen import speak_listen
import random
import pyjokes

class Jokes:
    def main(self,variableforlooks,tokeepthecodehappy, uuid, andagain):
        joke = pyjokes.get_joke()
        listofstarters = ["Ive got a great joke for you", "Heres a funny one", "I know a great joke", "Ok", "Here you go"]
        print(random.choice(listofstarters)+joke)
        speak_listen.say(random.choice(listofstarters))
        speak_listen.say(joke, uuid)

jokes = Jokes()