from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from googletrans import Translator

class translate:
    def main(self, text, intent):
        samples = {
            'what language is bonjour' : {'func' : self.langdetect},
            'whats hello in french' : {'func' : self.translate},
            'translate' : {'func' : self.translate}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)


    def removaloftext(self,text):
        text = text.lower()
        if 'how do i say' in text:
            text.replace('how do i say', '')
        if 'what is' in text:
            text.replace('what is', '')
        if "what's" in text:
            text.replace("what's",'')
        if 'what language is' in text:
            text.replace('what language is','')
        if 'into' in text:
            text.replace('into','')
        return text            

    def langdetect(self,text):
        text = self.removaloftext(text)
        result = translator.detect(text)
        speak_listen.say(result)
        #print(result)
        

    def translate(self, text):
        lang,text = self.detectlang(text)
        text = self.removaloftext(text)
        translatedtext = translator.translate(text, dest=lang)
        speak_listen.say(translatedtext)
        #print(translatedtext)

    def detectlang(self, text):
        text = text.lower()
        if "french" in text:
            lang = 'fr'
            text.replace('french', '')
        if "spanish" in text:
            lang = 'es'
            text.replace('spanish', '')
        if "chinese" in text:
            lang = 'zh-cn'
            text.replace('chinese', '')
        if "italian" in text:
            lang = 'it'
            text.replace('italian', '')
        if 'english' in text:
            lang = 'en'
            text.replace('english', '')
        if 'japanese' in text:
            lang = 'jp'
            text.replace('japanese', '')
        return lang , text


translator = Translator()
translate = translate()