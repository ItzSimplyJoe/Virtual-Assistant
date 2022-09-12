from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from pydictionary import dictionary
import random
class words:
    def main(self, text, intent):
        samples = {
            'how do i spell' : {'func' : self.spell},
            'what does potato mean' : {'func' : self.definition},
            'what the definition of potato' : {'func' : self.definition},
            'whats another word for' : {'func' : self.synonym},
            'whats the opposite of' : {'func' : self.antonym}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)

    def spell(self,text):
        spelling = []
        word = self.keywords(text)
        for letter in word:
            spelling.append(letter)
        words = (spelling + word)
        print (words)
        speak_listen.say(words)

    def definition(self,text):
        word = self.keywords(text)
        dict = Dictionary(word,0)
        speak_listen.say(dict.meanings())
    
    def synonym(self,text):
        stuff = Dictionary.synonyms(text)
        print(stuff)
    
    def antonym(self,text):
        stuff = Dictionary.antonyms(text)
        print(stuff)


    def keywords(self,text):
        text = text.lower()
        if 'how to spell' in text:
            text = text.replace('how to spell','')
            self.keywords(text)
        if 'how do i spell' in text:
            text = text.replace('how do i spell','')
            self.keywords(text)
        if 'how do you spell' in text:
            text = text.replace('how do you spell','')
            self.keywords(text)
        if 'whats the opposite of' in text:
            text = text.replace('whats the opposite of','')
            self.keywords(text)
        if 'mean' in text:
            text = text.replace('mean', '')
            self.keywords(text)
        if 'what does' in text:
            text = text.replace('what does','')
            self.keywords(text)
        if ' ' in text:
            text = text.replace(' ', '')
        return text


words = words()