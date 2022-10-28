import pvporcupine 
import pyaudio
import random
import struct
from tkinter import CENTER
import PySimpleGUI as sg
import multiprocessing
from assistant_functions.speak_listen import speak_listen
from main import *


class VoiceCommandListener:
    def __init__(self):
        self.active = True
    
    def listenForVoiceCommands(self, window, uuid):
        while self.active:
            self.porcupine = pvporcupine.create(
            access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
            keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
            keywords = ['Oi Badger']
            )   
            pa = pyaudio.PyAudio()
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
                    #window['-OUTPUT-'].update(stufftooutput)
            except:
                audio_stream = pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)
         

    def listenForTextCommands(self, window, uuid):
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                    quit()
            if event == "Submit":
                input = values['-input-']
                if input != "" or input != " ":
                    print("You:")
                    stufftooutput = assistant.reply(input,uuid)
                    #window['-OUTPUT-'].update(stufftooutput)
            else:
                continue


class Assistant:

    def __init__(self, name):
        self.name = name

    def main(self, uuid):
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
        print("ready")
        self.porcupine = None
        pa = None

        window = sg.Window("Virtual Asisstant", layout, finalize = True, resizable = True)

        vcl = VoiceCommandListener()
        p1 = multiprocessing.Process(target=vcl.listenForVoiceCommands, args=[window, uuid])
        p2 = multiprocessing.Process(target=vcl.listenForTextCommands, args=[window, uuid])
        p1.start()
        p2.start()
        p1.join()
        p2.join()
 
def main():
    assistant = Assistant("Badger")
    uuid = "cYGjyYwAJNBJjiuImnCh"
    assistant.main(uuid)

if __name__ == "__main__":
    main()