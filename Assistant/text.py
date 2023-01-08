from tkinter import CENTER
import PySimpleGUI as sg
import random
from main import *
import webbrowser
from textfunctions import *   
from assistant_functions.createprofile import *
class Text:
    
    def __init__(self, name):
        self.name = name
        
    def main(self,uuid,choice):
        bodyfont,bodyfontsize,titlefont,titlefontsize,style = textfunctions.lookscheck(uuid)
        bodyfonts = (bodyfont,int(bodyfontsize))
        titlefont = (titlefont,int(titlefontsize))
        sg.change_look_and_feel(style)

        QT_ENTER_KEY1 = 'special 16777220'
        QT_ENTER_KEY2 = 'special 16777221'
        bulletpoints = ["Ask a maths question", "Create a personal profile","Ask for the date", "Ask for the time", "Using chatgpt write an essay", "Using chatgpt write a program", "Ask for a joke", "Play a song", "Ask Badger to quiz you", "Ask a general question", "Ask for a translation into French", "Create a shopping list", "Ask for a definition", "Ask for a synonym", "Ask for an antonym", "Compliment it", "Say Hello", "Ask how it is", "Insult it"]

        leftside = [
            [sg.Text("Oi Badger!", size =(20, 1), justification=CENTER, font=titlefont)],
            [sg.Text("Suggestions:", justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],  
            [sg.Text(random.choice(bulletpoints), justification=CENTER, font = bodyfonts)],
            [sg.Button("Logout", size = (7,1))]
            ]

        rightside = [
            [sg.Output(size=(65,10), key='-OUTPUT-')],
            [sg.Text("How can i help?", size =(13, 1), font=bodyfonts),sg.InputText(key='-input-', size = (40,1), do_not_clear=False), sg.Button("Submit", size = (7,1))],
            ]

        menu_def = [['View', ['Font Settings', 'Colour Settings']],
                    ['Audio', 'Audio Settings'],
                    ['Account', 'Create a personal profile','Logout'],
                    ['Help', 'About...']
                    ]

        layout = [[sg.Menu(menu_def)],
            [sg.Column(leftside),
            sg.Column(rightside),
            ]
            ]

        window = sg.Window("Oi Badger!", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
            if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                input = values['-input-']
                window['-input-'].update('')
                if len(input) != 0:
                    print("You:")
                    stufftooutput = assistant.reply(input,uuid,choice)
                    window['-OUTPUT-'].update(stufftooutput)
            elif event == "Submit":
                input = values['-input-']
                if len(input) != 0:
                    print("You:")
                    stufftooutput = assistant.reply(input,uuid,choice)
                    window['-OUTPUT-'].update(stufftooutput)
                else:
                    speak_listen.say("Please dont leave the box blank",uuid)
            elif event == "Logout":
                window.close()
                textfunctions.logout(uuid,choice)
            elif event == "About...":
                webbrowser.open("https://github.com/ItzSimplyJoe/Virtual-Assistant/blob/main/README.md", new=0, autoraise=True)
            elif event == "Font Settings":
                try:
                    font,size,title,body = textfunctions.font(uuid,choice)
                    if font == "Restore Defaults":
                        sg.popup("For these changes to take place please restart the application")
                    else:
                        textfunctions.fontandcolourassigner(uuid,choice,font,size,title,body,None)
                        sg.popup("For these changes to take place please restart the application")

                except:
                    continue  
            elif event == "Colour Settings":
                try:
                    colour = textfunctions.lookandfeelwindow(uuid,choice)
                    textfunctions.fontandcolourassigner(uuid,choice,None,None,None,None,colour)
                    sg.popup("For these changes to take place please restart the application")
                except:
                    continue
            elif event == "Create a personal profile":
                profile.main(uuid,choice)
            elif event == "Audio Settings":
                try:
                    textfunctions.audiosettings(uuid,choice)
                    speak_listen.say("New Voice Settings Saved", uuid)
                except:
                    continue
            else:
                continue

    


text = Text("Badger")
#text.main("rRevaBfENYYgplhlzIfO","text")