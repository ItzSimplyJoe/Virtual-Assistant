from tkinter import CENTER
import PySimpleGUI as sg
import random
from main import *
import pvporcupine
import pyaudio
import struct
from assistant_functions.speak_listen import speak_listen



class UI:
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
        bulletpoints = ["Ask whats 124 x 125", "Ask a maths question?", "Ask how the virtual assistant is?", "Insult it", "Compliment it", "Ask it to play a song", "- Ask it to translate something into a different language", "Ask it how to spell something", "Ask it what something means","Just say hi"]
        titlefont = ("coolvetica compressed hv",35)
        bodyfonts = ("coolvetica rg",12)


        leftside = [
            [sg.Text("            Virtual Assistant", size =(20, 1), font=titlefont)],
            [sg.Text(" ")],
            [sg.Text("Suggestions:", justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],  
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            ]

        rightside = [
            [sg.Output(size=(60,10), key='-OUTPUT-')],
            [sg.Text("How can i help?", size =(13, 1), font=bodyfonts),sg.InputText(key='-input-', size = (40,1), do_not_clear=False), sg.Button("Submit")],
            ]

        layout = [
            [sg.Column(leftside),
            sg.Column(rightside),
            ]
            ]

        window = sg.Window("Virtual Asisstant", layout, resizable=True)
        while True:
            event, values = window.read()
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                keyword_index = self.porcupine.process(pcm)
                if keyword_index >= 0:
                    print("I heard my name")
                    if audio_stream is not None:
                        audio_stream.close()
                    said = speak_listen.listen()
                    print("You:")
                    stufftooutput = assistant.reply(said,uuid)
                    window['-OUTPUT-'].update(stufftooutput)
            except:
                audio_stream = pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)
                if event == "Exit" or event == sg.WIN_CLOSED:
                    quit()
                if event == "Submit":
                    input = values['-input-']
                    if input != "" or input != " ":
                        print("You:")
                        stufftooutput = assistant.reply(input,uuid)
                        window['-OUTPUT-'].update(stufftooutput)
                else:
                    continue

ui = UI("Badger")
ui.main("12345679123456789")