from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import PySimpleGUI as sg
from time import sleep

class Timer:
    def main(self, text, intent, uuid, choice):
        samples = {
            'create a 10 minute timer' : {'func' : self.timerset},
            'start a 30 second timer' : {'func' : self.timerset},
            'create a timer' : {'func' : self.timercreate},
            'can i start a timer' : {'func' : self.timercreate},
            'start a timer' : {'func' : self.timercreate},
            'start timer' : {'func' : self.timercreate},
            'create timer' : {'func' : self.timercreate},
            'create a timer' : {'func' : self.timercreate},
            'start a 10 minute timer' : {'func' : self.timerset},
            'start a 30 minute timer' : {'func' : self.timerset},
            'start a 30 second timer' : {'func' : self.timerset},
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text,uuid)

    def timerset(self,text,uuid):
        text = text.lower()
        text = text.split()
        for word in text:
            if word.isdigit():
                timeperiod = word
            elif word == "hour" or word =="hours" or word =="minute" or word == "minutes" or word == "second" or word == "seconds":
                periodoftime = word
        self.timechecker(periodoftime,timeperiod,uuid)

    def timechecker(self,periodoftime,timeperiod,uuid) :   
        if periodoftime == "hour" or periodoftime == "hours":
            time = timeperiod * 3600
        elif periodoftime == "minute" or periodoftime == "minutes":
            time = timeperiod * 60
        else:
            time = timeperiod
        self.timerscreen(time,uuid)

    def timercreate(self,text,uuid):
        layout = [[sg.Text("   Input Your Time")],
                  [sg.Text("Hours", size =(7, 1)),sg.InputText("0", size =(7, 1),key = "-hours-")],
                  [sg.Text("Minutes", size =(7, 1)),sg.InputText("0", size =(7, 1),key = "-mins-")],
                  [sg.Text("Seconds", size =(7, 1)),sg.InputText("0", size =(7, 1),key = "-secs-")],
                  [sg.Button("Close"),sg.Text("  "),sg.Button("Submit")]]
        window = sg.Window("Create a Timer", layout)
        while True:
            event,values = window.read()
            if event == sg.WIN_CLOSED or event == "Close":
                break
            if event == "Submit":
                hours = values["-hours-"]
                minutes = values["-mins-"]
                seconds = values["-secs-"]
                time = (hours*3600) + (minutes*60) + seconds
                window.close()
                self.timerscreen(time,uuid)
            else:
                continue


    def timerscreen(self,time,uuid):
        layout = [[sg.Text("Time:"), sg.Text("TimeRemaining", size=(10,1), key="t")]]

        window = sg.Window("Timer",layout)
        hours = 0
        mins = 0
        seconds = 0
        time = int(time)
        while True:
            event, values = window.read(1000)
            if time >= 3600:
                hours = (time // 3600)
                time - (hours*3600)
            elif time >= 60:
                mins = (time//60)
                time - (mins*60)
            else:
                seconds = time
            time -= 1
            output = (f'{hours}:{mins}:{seconds}')
            window['t'].update(output)
            sleep(0.88)
            if event != sg.TIMEOUT_KEY:
                window.close()
                break
            elif event == sg.WIN_CLOSED:
                window.close()
                break
            elif time == 0:
                speak_listen.say("AHHHHHHHHHHHHHHHHHHHHHHHHhhhhhhhhH Your timer is up!",uuid)
                window.close()


timer = Timer()