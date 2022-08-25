from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from googletrans import Translator

class translate:
    def main(self, text, intent):
        samples = {
            'what language' : {'func' : self.langdetect},
            'translate' : {'func' : self.translate}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)


    def removaloftext(self,text):
        text = text.lower()
        if 'how do i say' in text:
            text.replace('how do i say', '')
        elif 'what is' in text:
            text.replace('what is', '')
        elif "what's" in text:
            text.replace("what's",'')
        elif 'what language is' in text:
            text.replace('what language is','')
        return text            

    def langdetect(self,text):
        text = self.removaloftext(text)
        




    def translate(self, text):
        lang,text = self.detectlang(text)
        text = self.removaloftext(text)
        translatedtext = translator.translate(text, dest=lang)
        speak_listen.say(translatedtext)

    def detectlang(self, text):
        text = text.lower()
        if "french" in text:
            lang = 'fr'
            text.replace('french', '')
        elif "spanish" in text:
            lang = 'es'
            text.replace('spanish', '')
        elif "chinese" in text:
            lang = 'zh-cn'
            text.replace('chinese', '')
        elif "italian" in text:
            lang = 'it'
            text.replace('italian', '')
        elif 'english' in text:
            lang = 'en'
            text.replace('english', '')
        return lang,text


translator = Translator()
translate = translate()