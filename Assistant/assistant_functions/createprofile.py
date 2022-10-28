from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import time


class profile:
    def main(self,text,intent,uuid):
        speak_listen.say("Would you like to set up a personal profile?")
        time.sleep(2)
        said = speak_listen.listen()
        samples = {
        'sure' : {'func' : self.createprofile},
        'of course' : {'func' : self.createprofile},
        'yes' : {'func' : self.createprofile},
        'yeah' : {'func' : self.createprofile},
        'ok' : {'func' : self.createprofile},
        'no' : {'func' : self.exit},
        'stop' : {'func' : self.exit},
        'nope' : {'func' : self.exit},
        }
        
        most_similar = determine_most_similar_phrase(said, samples)
        func = samples[most_similar]['func']
        func(uuid)

    def createprofile(self,uuid):
        speak_listen.say("Ok lets begin")
        speak_listen.say("If at any point you wish to stop just say stop")
        speak_listen.say("Firstly, what should i call you?")
        name = speak_listen.listen()
        if name == "stop" or name == "Stop":
            self.exit()
        speak_listen.say("Ok, thankyou. How old are you")
        age = speak_listen.listen()
        if age == "stop" or age == "Stop":
            self.exit()
        speak_listen.say("And finally, Where are you from?")
        country = speak_listen.listen()
        if country == "stop" or country == "Stop":
            self.exit()
        speak_listen.say("Ok")
        speak_listen.say("Your name is" + name)
        speak_listen.say("You are " + age + " years old")
        speak_listen.say("And you are from" + country)
        speak_listen.say("Is this all correct?")
        response = speak_listen.listen()
        if response == "stop" or response == "Stop":
            self.exit()

        samples = {
        'sure' : {'func' : self.save},
        'of course' : {'func' : self.save},
        'yes' : {'func' : self.save},
        'yeah' : {'func' : self.save},
        'ok' : {'func' : self.save},
        'no' : {'func' : self.createprofile},
        'stop' : {'func' : self.createprofile},
        'nope' : {'func' : self.createprofile},
        }
        most_similar = determine_most_similar_phrase(response, samples)
        func = samples[most_similar]['func']
        if func == self.createprofile:
            speak_listen.say("Ok, my bad lets try this again")
            func(uuid)
        elif func == self.save:
            func(name,age,country,uuid)

    def save(self,name,age,country,uuid):
        with open (f"{uuid}"+".csv") as file:
            file.write(name + "," + age + "," + country)
            file.close()

    def exit(self,uuid):
        speak_listen.say("Exiting personal profile creation")



        

        