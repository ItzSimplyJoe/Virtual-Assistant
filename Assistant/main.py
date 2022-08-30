import pvporcupine 
import pyaudio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.repeat import repeat
from assistant_functions.wikisearch import wikisearch
from assistant_functions.translate import translate
from assistant_functions.musicplayer import Music
import struct
import multiprocessing
import os

class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text):
        intent = intentclassifier.predict(text)

        replies = {
            'greeting' : reply,
            'leaving' : reply,
            'compliment' : reply,
            'insult' : reply,
            'repeat': repeat.repeat,
            'maths' : maths.main,
            'wikisearch' : wikisearch.main,
            'translate' : translate.main,
            'music' : Music.main
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


        self.porcupine = pvporcupine.create(
        access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
        keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
        keywords = ['Oi Badger']
        )   

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



intentclassifier = IntentClassifier()
assistant = Assistant("Badger")
assistant.main()