from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import PySimpleGUI as sg
import os

sg.theme = ("Bluemono")
class Profile:
    def main(self,text,intent,uuid,choice):
        value = self.check(uuid,choice)
        speak_listen.say("Would you like to set up a personal profile?")
        if choice == "voice":
            said = speak_listen.listen()
        elif choice == "text":
            lists = ["Yes","No","Stop"]
            layout = [[sg.Text("Would you like to setup a personal profile?", size =(40, 1), font=40)],
            [sg.Combo(lists, key='-choice-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        said = values["-choice-"]
                        window.close()
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
            layout = [[sg.Text("What should i call you?", size =(20, 1), font=40)],
            [sg.InputText(key='-name-', font=16),sg.Button("Submit")]]
            window = sg.Window("Name", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        name = values["-name-"]
                        window.close()
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
                        window.close()
        if age == "stop" or age == "Stop":
            self.exit()
        speak_listen.say("And finally, Where are you from?")
        if choice == "voice":
            country = speak_listen.listen()
        elif choice == "text":
            layout = [[sg.Text("What country are you from?", size =(25, 1), font=40)],
            [sg.InputText(key='-country-', font=16),sg.Button("Submit")]]
            window = sg.Window("Country", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        country = values["-country-"]
                        window.close()
        if country == "stop" or country == "Stop":
            self.exit()
        speak_listen.say("Ok")
        speak_listen.say("Your name is " + name)
        speak_listen.say("You are " + age + " years old")
        speak_listen.say("And you are from " + country)
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
                        window.close()
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
            func(uuid,choice)
        elif func == self.save:
            func(name,age,country,uuid,choice)

    def save(self,name,age,country,uuid,choice):
        file = open(f"UserProfiles/{uuid}"+".csv", "a")
        file.write(f"{name},{age},{country}")
        file.flush()
        file.close()

    def exit(self,uuid,choice):
        speak_listen.say("Exiting personal profile creation")
        exit()
        


    def check(self,uuid,choice):
        try:
            file = open(f"UserProfiles/{uuid}.csv")
            file.close()
            total = 0
        except:
            total = 1
        if total == 1:
            return True
        else:
            speak_listen.say("You alredy have a profile created, would you like to delete your current one?")
            if choice == "voice":
                said = speak_listen.listen()
            elif choice == "text":
                lists = ["Yes","No"]
                layout = [[sg.Text("Are you sure you would like to delete your old one?", size =(40, 1), font=40)],
                [sg.Combo(lists, key='-choice-', font=16),sg.Button("Submit")]]
                window = sg.Window("Check", layout, resizable=False)
                while True:
                    event,values = window.read()
                    if event == sg.WIN_CLOSED:
                        break
                    else:
                        if event == "Submit":
                            said = values["-choice-"]
                            window.close()
                            if said == "No":
                                self.exit(uuid,choice)
                            elif said == "Yes":
                                os.remove(f"UserProfiles/{uuid}.csv")
                                continue

profile = Profile()
        
#profile.main("create profile","Intent","cYGjyYwAJNBJjiuImnCh","text")
        