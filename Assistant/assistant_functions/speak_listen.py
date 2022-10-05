import pyttsx3
import speech_recognition as sr
from playsound import playsound


class Speak_Listen:
    def __init__(self):
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty("rate", 150)

        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def say(self, text):
        self.speech_engine.say(text, "speech")
        self.speech_engine.runAndWait()
        print(text)
        return(text)

    def stop_speaking(self, name, completed):
        self.speech_engine.endLoop()

    def listen(self):
    
        with self.mic as source:
            print("Listening")
            self.r.non_speaking_duration = 0.5
            audio = self.r.listen(source, timeout=7, phrase_time_limit=5)
    
        return (self.r.recognize_google(audio))

speak_listen = Speak_Listen()