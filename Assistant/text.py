from tkinter import CENTER
import PySimpleGUI as sg
import random
from main import *


class Text:
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

        window = sg.Window("Virtual Asisstant", layout, resizable=True)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "Submit":
                input = values['-input-']
                print(input)
                assistant.reply(input)
            else:
                continue

text = Text("Badger")
