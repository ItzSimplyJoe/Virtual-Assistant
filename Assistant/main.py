from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.wikisearch import wikisearch
from assistant_functions.translate import translate
from assistant_functions.music import music
from assistant_functions.words import words
from assistant_functions.jokes import jokes
from assistant_functions.light import light
from assistant_functions.createprofile import profile


class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text,uuid):
        intent = intentclassifier.predict(text)

        replies = {
            'greeting' : reply,
            'leaving' : reply,
            'compliment' : reply,
            'insult' : reply,
            'questions' : reply,
            'maths' : maths.main,
            'wikisearch' : wikisearch.main,
            'translate' : translate.main,
            'words' : words.main,
            'music' : music.main,
            'jokes' : jokes.main,
            'light' : light.main,
            'profile' : profile.main
            }

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                print(text)
                print("Badger:")
                if reply_func == profile.main:
                    profile.main(text,intent,uuid)
                reply_func(text, intent)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("Error: " + str(e))
    
 

intentclassifier = IntentClassifier()
assistant = Assistant("Badger")
