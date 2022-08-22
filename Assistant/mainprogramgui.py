from ast import Assign
from tkinter import CENTER
import PySimpleGUI as sg
import os.path
from main import assistant


def mainui():
    titlefont = ("coolvetica compressed hv",35)
    bodyfonts = ("coolvetica rg",12)


    leftside = [
            [sg.Text("            Virtual Assistant", size =(20, 1), font=titlefont)],
            [sg.Image('assistant.png', size=(300,511))],
            [sg.Text(" ")],
            [sg.Text("Suggestions", justification=CENTER, font = bodyfonts)],
            [sg.Text("- Joe write something here", justification=CENTER, font = bodyfonts)],
            [sg.Text("- And here", justification=CENTER, font = bodyfonts)],
            [sg.Text("- Dont forget about this one", justification=CENTER, font = bodyfonts)],
    ]

    rightside = [
        [sg.Text(" ")],
        [sg.Text("How can i help?", size =(13, 1), font=bodyfonts),sg.InputText(key='-input-', size = (40,1), do_not_clear=False), sg.Button("Submit")],
    ]

    layout = [
        [
            sg.Column(leftside),
            sg.Column(rightside),
        ]
    ]

    window = sg.Window("Virtual Asisstant", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "submit":
            input = values['-input-']
            print(input)
        else:
            continue
    assistant.main()




def maingui(runfile):
    print("wow you logged in")
