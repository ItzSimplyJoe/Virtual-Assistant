import pvporcupine 
import pyaudio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.repeat import repeat
import struct
import multiprocessing

class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text):
        intent = intentclassifier.predict(text)
        if intent == 'leaving':
            speak_listen.say("Exiting")
            quit()

        replies = {
            'greeting' : reply,
            'insult' : reply,
            'personal_q' : reply,
            'repeat': repeat.repeat,
            'maths' : maths
            }

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                reply_func(text, intent)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("Error: " + str(e))

    def main(self):
        print("ready")
        self.porcupine = None
        pa = None
        audio_stream = None


        self.porcupine = pvporcupine.create(access_key = access_key,keywords=["jarvis"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=self.porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.porcupine.frame_length)
        
        while True:
            
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            except:
                audio_stream = pa.open(
                        rate=self.porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=self.porcupine.frame_length)

            keyword_index = self.porcupine.process(pcm)

            if keyword_index >= 0:
                print("I heard my name")

                if audio_stream is not None:
                    audio_stream.close()
                said = speak_listen.listen()
                print(said)

                self.reply(said)
                
    
access_key = "k+dAStF62RACtJcNtYFHyseWvW7mWw6fFuUrpPDDeXZ0UA44VVIBZA=="
intentclassifier = IntentClassifier()
assistant = Assistant("Assistant")
Assistant.main()