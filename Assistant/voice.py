from tkinter import CENTER
import PySimpleGUI as sg
import pvporcupine
import pyaudio
import struct
from assistant_functions.speak_listen import speak_listen
from main import *
import random


class Voice:
    def __init__(self, name):
        self.name = name
        
    def main(self):
        bulletpoints = ["-Oi Badger whats 14 x 34", "- Ask a maths question?", "- Ask how Badger is?", "- Why not ask about Alexa?", "- Insult Badger", "- Compliment Badger", "- Ask badger to play a song", "- Ask Badger to translate something into a different language", "- Ask Badger how to spell something", "Ask Badger what something means","- Just say hi"]
        titlefont = ("coolvetica compressed hv",35)
        bodyfonts = ("coolvetica rg",12)


        leftside = [
            [sg.Text("            Virtual Assistant", size =(20, 1), font=titlefont)],
            [sg.Image('assistant.png', size=(300,511))],
            [sg.Text(" ")],
            [sg.Text("Suggestions:", justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],  
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            ]

        rightside = [
            [sg.Text("How can i help?", size =(13, 1), font=bodyfonts),sg.InputText(key='-input-', size = (40,1), do_not_clear=False), sg.Button("Submit")],
            ]

        layout = [
            [sg.Column(leftside),
            sg.Column(rightside),
            ]
            ]

        sg.Window("Virtual Asisstant", layout, resizable=True)

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
                    assistant.reply(said)
            except:
                audio_stream = pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)

    def new(self,uuid):
        print("WOw")


voice = Voice("Badger")