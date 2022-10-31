from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import PySimpleGUI as sg

sg.theme = ("Bluemono")
class profile:
    def main(self,text,intent,uuid,choice):
        speak_listen.say("Would you like to set up a personal profile?")
        said = speak_listen.listen()
        samples = {
        'sure' : {'func' : self.createprofile},
        'of course' : {'func' : self.createprofile},
        'yes' : {'func' : self.createprofile},
        'yeah' : {'func' : self.createprofile},
        'ok' : {'func' : self.createprofile},
        'no' : {'func' : self.exit},
        'stop' : {'func' : self.exit},
        'nope' : {'func' : self.exit},
        }
        
        most_similar = determine_most_similar_phrase(said, samples)
        func = samples[most_similar]['func']
        func(uuid,choice)

    def createprofile(self,uuid,choice):
        speak_listen.say("Ok lets begin")
        speak_listen.say("If at any point you wish to stop just say stop")
        speak_listen.say("Firstly, what should i call you?")
        if choice == "voice":
            name = speak_listen.listen()
        elif choice == "text":
            layout = [[sg.Text("What should i call you?", size =(15, 1), font=40)],
            [sg.InputText(key='-name-', font=16),sg.Button("Submit")]]
            window = sg.Window("Name", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        name = values["-name-"]
        if name == "stop" or name == "Stop":
            self.exit()
        speak_listen.say("Ok, thankyou. How old are you")
        if choice == "voice":
            age = speak_listen.listen()
        elif choice == "text":
            layout = [[sg.Text("How old are you?", size =(15, 1), font=40)],
            [sg.InputText(key='-age-', font=16),sg.Button("Submit")]]
            window = sg.Window("Age", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        age = values["-age-"]
        if age == "stop" or age == "Stop":
            self.exit()
        speak_listen.say("And finally, Where are you from?")
        if choice == "voice":
            country = speak_listen.listen()
        elif choice == "text":
            layout = [[sg.Text("What country are you from?", size =(15, 1), font=40)],
            [sg.InputText(key='-country-', font=16),sg.Button("Submit")]]
            window = sg.Window("Country", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        country = values["-country-"]
        if country == "stop" or country == "Stop":
            self.exit()
        speak_listen.say("Ok")
        speak_listen.say("Your name is" + name)
        speak_listen.say("You are " + age + " years old")
        speak_listen.say("And you are from" + country)
        speak_listen.say("Is this all correct?")
        if choice == "voice":
            name = speak_listen.listen()
        elif choice == "text":
            lists = ["Yes","No","Stop"]
            layout = [[sg.Text("Is this correct?", size =(15, 1), font=40)],
            [sg.Combo(lists, key='-correct-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        response = values["-correct-"]
        if response == "stop" or response == "Stop":
            self.exit()

        samples = {
        'sure' : {'func' : self.save},
        'of course' : {'func' : self.save},
        'yes' : {'func' : self.save},
        'yeah' : {'func' : self.save},
        'ok' : {'func' : self.save},
        'no' : {'func' : self.createprofile},
        'stop' : {'func' : self.createprofile},
        'nope' : {'func' : self.createprofile},
        }
        most_similar = determine_most_similar_phrase(response, samples)
        func = samples[most_similar]['func']
        if func == self.createprofile:
            speak_listen.say("Ok, my bad lets try this again")
            func(uuid)
        elif func == self.save:
            func(name,age,country,uuid)

    def save(self,name,age,country,uuid):
        with open (f"{uuid}"+".csv") as file:
            file.write(name + "," + age + "," + country)
            file.close()

    def exit(self,uuid,choice):
        speak_listen.say("Exiting personal profile creation")



        

        