from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import datetime

class DateAndTime:
    def main(self,text,intent,uuid,choice):
        samples = {
            'what day is it' : {'func' : self.day},
            'whats todays date' : {'func' : self.date},
            'whats the time' : {'func' : self.time}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text,uuid)

    def day(self,text,uuid):
        speak_listen.say((datetime.datetime.now()).strftime("%A"),uuid)
    def date(self,text,uuid):
        speak_listen.say("Today is",(datetime.datetime.now()).strftime("%d %B %Y"),uuid)
    def time(self,text,uuid):
        speak_listen.say("The time is",(datetime.datetime.now()).strftime("%H:%M"),uuid)
    

dateandtime = DateAndTime()