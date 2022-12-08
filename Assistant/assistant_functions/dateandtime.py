from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import datetime

class DateAndTime:
    def main(self,text,intent,uuid,choice):
        samples = {
            'what day is it' : {'func' : self.day},
            'whats todays date' : {'func' : self.date},
            'whats the time' : {'func' : self.time},
            'what time is it' : {'func' : self.time},
            'what is the date' : {'func' : self.date},
            'what day is today' : {'func' : self.day},
            'what is todays date' : {'func' : self.date},
            'what is the time' : {'func' : self.time}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text,uuid)

    def day(self,text,uuid):
        print("Today is a "+(datetime.datetime.now()).strftime("%A"))
        speak_listen.say("Today is a "+(datetime.datetime.now()).strftime("%A"),uuid)
    def date(self,text,uuid):
        print("Today is "+(datetime.datetime.now()).strftime("%d %B %Y"))
        speak_listen.say("Today is "+(datetime.datetime.now()).strftime("%d %B %Y"),uuid)
    def time(self,text,uuid):
        print("The time is "+(datetime.datetime.now()).strftime("%H:%M"))
        speak_listen.say("The time is "+(datetime.datetime.now()).strftime("%H:%M"),uuid)
    

dateandtime = DateAndTime()