from assistant_functions.speak_listen import speak_listen
import random

class Jokes:
    def main(self,variableforlooks,tokeepthecodehappy):
        import pyjokes
        joke = pyjokes.get_joke()
        listofstarters = ["Ive got a great joke for you", "Heres a funny one", "I know a great joke", "Ok"]
        speak_listen.say(random.choice(listofstarters))
        speak_listen.say(joke)

jokes = Jokes()