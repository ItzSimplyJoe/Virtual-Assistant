from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.searches import searches
from assistant_functions.music import music
from assistant_functions.words import words
from assistant_functions.jokes import jokes
from assistant_functions.light import light
from assistant_functions.createprofile import profile
from assistant_functions.timer import timer
from assistant_functions.shoppinglist import shoppinglist


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
            'searches' : searches.main,
            'words' : words.main,
            'music' : music.main,
            'jokes' : jokes.main,
            'light' : light.main,
            'profile' : profile.main,
            'timer' : timer.main
            }

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                print(text)
                if reply_func == profile.main or reply_func == shoppinglist.main:
                    reply_func(text,intent,uuid,choice)
                elif reply_func == timer.main:
                    reply_func(text,intent,choice)
                reply_func(text, intent)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("There has been an error, you can keep on using the program just please report this to Joe :D")
            print("Error: " + str(e))
    
 

intentclassifier = IntentClassifier()
assistant = Assistant("Badger")
