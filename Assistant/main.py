from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.gpt import gpt
from assistant_functions.music import music
from assistant_functions.words import words
from assistant_functions.searches import searches
from assistant_functions.jokes import jokes
from assistant_functions.light import light
from assistant_functions.createprofile import profile
from assistant_functions.timer import timer
from assistant_functions.shoppinglist import shoppinglist
from assistant_functions.dateandtime import dateandtime
from assistant_functions.quizprogram import quiz
from assistant_functions.location import location
from assistant_functions.weather import weather

class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self,text,uuid,choice):
        intent = intentclassifier.predict(text)

        replies = {
            'greeting' : reply,
            'leaving' : reply,
            'compliment' : reply,
            'insult' : reply,
            'questions' : reply,
            'maths' : maths.main,
            'gpt' : gpt.main,
            'searches' : searches.main,
            'words' : words.main,
            'music' : music.main,
            'jokes' : jokes.main,
            'light' : light.main,
            'profile' : profile.main,
            'timer' : timer.main,
            'shoppinglist' : shoppinglist.main,
            'dateandtime' : dateandtime.main,
            'quiz' : quiz.main,
            'location' : location.main,
            'weather' : weather.main
            }

        try:
            reply_func = replies[intent]
            if callable(reply_func):
                print(text)
                print("Badger:")
                reply_func(text, intent,uuid, choice)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("There has been an error, you can keep on using the program just please report this to Joe :D")
            print("Error: " + str(e))
    
 

intentclassifier = IntentClassifier()
assistant = Assistant("Badger")
