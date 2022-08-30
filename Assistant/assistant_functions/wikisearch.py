from assistant_functions.speak_listen import speak_listen
import wikipedia
import time

class wikisearch:
    def main(self, text, intent):
        self.search(text)


    def search(self,text):
        try:
            result = wikipedia.summary(text, sentences = 2)
            #print(result)
            speak_listen.say(result)
        except:
            try:
                result = wikipedia.suggest(text)
                #print(result)
                speak_listen.say("Sorry, did you mean "+ result)
                self.search(text)
            except:
                #print("broken")
                speak_listen.say("yeh you have broken everything!")


    def keyword(self,text):
        text = text.lower()
        splitstring = text.split()
        string = ""
        for word in splitstring:
            if word != "what" and word !="when" and word !="how" and word !="where" and word !="a" and word !="is" and word !="who" and word !="was":
                string = (string +" " + word)


wikisearch = wikisearch()