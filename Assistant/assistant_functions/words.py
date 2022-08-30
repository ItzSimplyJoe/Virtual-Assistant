from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from pydictionary import Dictionary
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
        word = self.keywords(text)
        spelling = list(word)
        speak_listen.say(spelling , word)

    def definition(self,text):
        word = self.keywords(text)
        dict = Dictionary(word,1)
        speak_listen.say(dict.meanings())


    def keywords(self,text):
        if 'how to spell' in text:
            text.replace('how to spell','')
        if 'how do i spell' in text:
            text.replace('how do i spell','')
        if 'how do you spell' in text:
            text.replace('how do you spell','')
        if 'whats the opposite of' in text:
            text.replace('whats the opposite of','')
        if 'mean' in text:
            text.replace('mean', '')
        return text


words = words()