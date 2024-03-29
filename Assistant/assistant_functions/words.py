from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import random
from pydictionary import Dictionary

class Words:
    def main(self, text, intent,uuid,choice):
        samples = {
            'how do i spell' : {'func' : self.spell},
            'what does potato mean' : {'func' : self.definition},
            'what the definition of potato' : {'func' : self.definition},
            'whats another word for' : {'func' : self.synonym},
            'whats the opposite of' : {'func' : self.antonym},
            'how do you spell' : {'func' : self.spell},
            'how to spell' : {'func' : self.spell},
            'what does' : {'func' : self.definition},
            'what is the definition of' : {'func' : self.definition},
            'what is the meaning of' : {'func' : self.definition},
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text,uuid)

    def spell(self,text,uuid):
        spelling = []
        word = self.keywords(text,uuid)
        words = list(word)
        for i in words:
            spelling.append(i)
            spelling.append(' ')
        words = ''.join(spelling)
        print(words)
        speak_listen.say(words,uuid)

    def definition(self,text,uuid):
        word = self.keywords(text,uuid)
        dict = Dictionary(word,0)
        print(dict.meanings())
        speak_listen.say(dict.meanings(),uuid)
    
    def synonym(self,text,uuid):
        stuff = Dictionary.synonyms(text)
        print(stuff)
    
    def antonym(self,text,uuid):
        stuff = Dictionary.antonyms(text)
        print(stuff)


    def keywords(self,text,uuid):
        text = text.lower()
        if 'how to spell' in text:
            text = text.replace('how to spell','')
            self.keywords(text,uuid)
        if 'how do i spell' in text:
            text = text.replace('how do i spell','')
            self.keywords(text,uuid)
        if 'how do you spell' in text:
            text = text.replace('how do you spell','')
            self.keywords(text,uuid)
        if 'whats the opposite of' in text:
            text = text.replace('whats the opposite of','')
            self.keywords(text,uuid)
        if 'mean' in text:
            text = text.replace('mean', '')
            self.keywords(text,uuid)
        if 'what does' in text:
            text = text.replace('what does','')
            self.keywords(text,uuid)
        if ' ' in text:
            text = text.replace(' ', '')
        return text


words = Words()