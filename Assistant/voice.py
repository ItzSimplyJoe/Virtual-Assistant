import pvporcupine
import pyaudio
import struct
from assistant_functions.speak_listen import speak_listen
from main import *
import random


class Voice:
    def __init__(self, name):
        self.name = name
        
    def main(self,uuid):
        self.porcupine = None
        pa = None
        audio_stream = None


        self.porcupine = pvporcupine.create(
        access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
        keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
        keywords = ['Oi Badger']
        )   

        pa = pyaudio.PyAudio()
        print("Ready")

        while True:
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                keyword_index = self.porcupine.process(pcm)
                if keyword_index >= 0:
                    print("I heard my name")
                    if audio_stream is not None:
                        audio_stream.close()
                    said = speak_listen.listen()
                    assistant.reply(said,uuid)
            except:
                audio_stream = pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)



voice = Voice("Badger")