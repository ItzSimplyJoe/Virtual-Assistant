import pvporcupine 
import pyaudio
import random
import struct
from tkinter import CENTER
import PySimpleGUI as sg
import os.path
import asyncio
from assistant_functions.speak_listen import speak_listen
from intentclassification.intent_classification import IntentClassifier
from assistant_functions.reply import reply
from assistant_functions.maths import maths
from assistant_functions.repeat import repeat
from assistant_functions.wikisearch import wikisearch
from assistant_functions.translate import translate
from assistant_functions.music import music
from assistant_functions.words import words


class VoiceCommandListener:
    def __init__(self):
        self.active = True
    
    async def listenForVoiceCommands(self, audio_stream):
        print("voice")
        while self.active:
            self.porcupine = pvporcupine.create(
            access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
            keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
            keywords = ['Oi Badger']
            )   
            print("line 32 test")
            pa = pyaudio.PyAudio()
            try:
                pcm = await audio_stream.read(self.porcupine.frame_length)
                print("Line 35 test")
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                keyword_index = self.porcupine.process(pcm)
                if keyword_index >= 0:
                  print("I heard my name")
                  if audio_stream is not None:
                    audio_stream.close()
                  said = speak_listen.listen()
                  Assistant.reply(said)
            except:
                audio_stream = pa.open(
                print(repr(audio_stream)),
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)
         

    async def listenForTextCommands(self, window):
        print("text")
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                return
            if event == "Submit":
                input = values['-input-']
                print(input)
                Assistant.reply(input)
            else:
                continue


class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self, text):
        intent = IntentClassifier.predict(text)

        replies = {
            'greeting' : reply,
            'leaving' : reply,
            'compliment' : reply,
            'insult' : reply,
            'repeat': repeat.repeat,
            'maths' : maths.main,
            'wikisearch' : wikisearch.main,
            'translate' : translate.main,
            'words' : words.main,
            'music' : music.main
            }

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                reply_func(text, intent)
        except KeyError:
            speak_listen.say("Sorry, I didn't understand")
        except Exception as e:
            print("Error: " + str(e))

    async def main(self):
            bulletpoints = ["- Oi Badger whats 14 x 34", "- Ask a maths question?", "- Ask how Badger is?", "- Why not ask about Alexa?", "- Insult Badger", "- Compliment Badger", "- Ask badger to play a song", "- Ask Badger to translate something into a different language", "- Ask Badger how to spell something", "Ask Badger what something means","- Just say hi"]
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
            print("ready")
            self.porcupine = None
            pa = None
            audio_stream = None

            self.porcupine = pvporcupine.create(
              access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
              keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
              keywords = ['Oi Badger']
            )   
 
            window = sg.Window("Virtual Asisstant", layout)

            voiceCommandListener = VoiceCommandListener()
            voiceTask = asyncio.create_task(voiceCommandListener.listenForVoiceCommands(audio_stream))
            textTask = asyncio.create_task(voiceCommandListener.listenForTextCommands(window))
            await textTask
            self.active = False # Note that you can drop this variable, just doing this for consistency
            await voiceTask

 
def main():
    intentclassifier = IntentClassifier()
    assistant = Assistant("Badger")
    asyncio.run(assistant.main())

if __name__ == "__main__":
    main()