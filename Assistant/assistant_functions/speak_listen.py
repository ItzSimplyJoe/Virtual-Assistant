import pyttsx3
import speech_recognition as sr
from playsound import playsound
from translate import Translator

class Speak_Listen:
    def __init__(self):
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty("rate", 150)

        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def say(self, text, uuid):
        print("Badger:")
        text = self.uuidcheckandtranslate(text, uuid)
        print(text)
        self.speech_engine.say(text, "speech")
        self.speech_engine.runAndWait()
        return(text)

    def stop_speaking(self, name, completed):
        self.speech_engine.endLoop()

    def listen(self):
    
        with self.mic as source:
            print("Listening")
            self.r.non_speaking_duration = 0.5
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5)
    
        return (self.r.recognize_google(audio))

    def uuidcheckandtranslate(self,text, uuid):
        try:
            file = open(f"UserProfiles/{uuid}"+".csv", "r")
            name,age,lang = file.read().split(",")
            target_language = lang
            target_language.lower()
            if target_language == "french":
                target_language = "fr"
            elif target_language == "spanish":
                target_language = "es"
            elif target_language == "japanese":
                target_language = "jp"
            elif target_language == "taiwanese":
                target_language = "tw"
            elif target_language == "german":
                target_language = "de"
            elif target_language == "english":
                target_language = "en"
            elif target_language == "italian":
                target_language = "it"
            elif target_language == "dutch":
                target_language = "nl"
            elif target_language == "norwegian":
                target_language = "no"
            elif target_language == "arabic":
                target_language = "sa"
            elif target_language == "estonian":
                target_language == "ee"
            elif target_language == "finish":
                target_language = "fi"
            elif target_language == "swedish":
                target_language = "se"
        except:
            target_language = 'en'
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation


speak_listen = Speak_Listen()