from tkinter import CENTER
import PySimpleGUI as sg
import random
from main import *

sg.change_look_and_feel("DarkGrey3")
class Text:
    
    def __init__(self, name):
        
        self.name = name
        
    def main(self,uuid,choice):
        bulletpoints = ["Ask a maths question", "Create a personal profile","Ask for the date", "Ask for the time", "Using chatgpt write an essay", "Using chatgpt write a program", "Ask for a joke", "Play a song", "Ask Badger to quiz you", "Ask a general question", "Ask for a translation into French", "Create a shopping list", "Ask for a definition", "Ask for a synonym", "Ask for an antonym", "Compliment it", "Say Hello", "Ask how it is", "Insult it"]
        titlefont = ("coolvetica compressed hv",35)
        bodyfonts = ("coolvetica rg",12)

        leftside = [
            [sg.Text("Oi Badger!", size =(20, 1), justification=CENTER, font=titlefont)],
            [sg.Text("Suggestions:", justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],  
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            ]

        rightside = [
            [sg.Output(size=(65,10), key='-OUTPUT-')],
            [sg.Text("How can i help?", size =(13, 1), font=bodyfonts),sg.InputText(key='-input-', size = (40,1), do_not_clear=False), sg.Button("Submit", size = (7,1))],
            ]

        layout = [
            [sg.Column(leftside),
            sg.Column(rightside),
            ]
            ]

        window = sg.Window("Oi Badger!", layout, resizable=False, titlebar_background_color="grey", background_color="#8e6dae", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                quit()
            if event == "Submit":
                input = values['-input-']
                if len(input) != 0:
                    print("You:")
                    stufftooutput = assistant.reply(input,uuid,choice)
                    window['-OUTPUT-'].update(stufftooutput)
                else:
                    speak_listen.say("Please dont leave the box blank",uuid)
            else:
                continue

text = Text("Badger")
#text.main("123","text")