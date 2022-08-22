from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import wikipedia

class wikisearch:
    def main(self, text, intent):
        text = self.keyword(text)


    def search(self,text):
        try:
            result = wikipedia.summary(text, sentences = 2)
            speak_listen.say(result)
        except:
            result = wikipedia.suggest(text)
            speak_listen.say("Sorry, did you mean "+ result)
            self.search(text)


    def keyword(self,text):
        text = text.lower()
        splitstring = text.split()
        string = ""
        for word in splitstring:
            if word != "what" and word !="when" and word !="how" and word !="where" and word !="a" and word !="is" and word !="who" and word !="was":
                string = (string +" " + word)
        self.search(string)
        


wikisearch = wikisearch()
