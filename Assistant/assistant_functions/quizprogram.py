from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import PySimpleGUI as sg
import sys

class Quiz:
    def main(self,text,intent,uuid,choice):
        print("Would you like to take a quiz?")
        speak_listen.say("Would you like to take a quiz?",uuid)
        if choice == "voice":
            said = speak_listen.listen()
        elif choice == "text":
            lists = ["Yes","No","Stop"]
            layout = [[sg.Text("Would you like to take a quiz?", size =(40, 1), font=40)],
            [sg.Combo(lists, key='-choice-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        said = values["-choice-"]
                        if said == "None":
                            window.close()
                            self.main(text,intent,uuid,choice)
                        window.close()
        samples = {
        'sure' : {'func' : self.subject},
        'of course' : {'func' : self.subject},
        'yes' : {'func' : self.subject},
        'yeah' : {'func' : self.subject},
        'ok' : {'func' : self.subject},
        'no' : {'func' : self.exit},
        'stop' : {'func' : self.exit},
        'nope' : {'func' : self.exit},
        }

        most_similar = determine_most_similar_phrase(said, samples)
        func = samples[most_similar]['func']
        func(uuid,choice)

    def subject(self,uuid,choice):
        print("What subject would you like to take a quiz on?")
        speak_listen.say("What subject would you like to take a quiz on?",uuid)
        if choice == "voice":
            said = speak_listen.listen()
        elif choice == "text":
            lists = ["Maths","Science","English","History","Geography","Stop"]
            layout = [[sg.Text("What subject would you like to take a quiz on?", size =(40, 1), font=40)],
            [sg.Combo(lists, key='-choice-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        said = values["-choice-"]
                        if said == "None":
                            window.close()
                            self.subject(uuid,choice)
                        window.close()
        samples = {
        'maths' : {'func' : self.maths},
        'science' : {'func' : self.science},
        'english' : {'func' : self.english},
        'history' : {'func' : self.history},
        'geography' : {'func' : self.geography},
        'stop' : {'func' : self.exit},
        }

        most_similar = determine_most_similar_phrase(said, samples)
        func = samples[most_similar]['func']
        func(uuid,choice,score=0)
    
    def maths(self,uuid,choice,score):
        import random
        print("Okay good luck!")
        speak_listen.say("Okay good luck!",uuid)
        option1 = random.choice(range(1,100))
        option2 = random.choice(range(1,100))
        symbol = random.choice(["+","-","*","/"])
        print(f"What is {option1} {symbol} {option2}?")
        speak_listen.say(f"What is {option1} {symbol} {option2}?",uuid)
        if choice == "voice":
            said = speak_listen.listen()
        elif choice == "text":
            layout = [[sg.Text("What is the answer?", size =(40, 1), font=40)],
            [sg.Input(key='-choice-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        said = values["-choice-"]
                        if said == "":
                            window.close()
                            self.maths(uuid,choice)
                        window.close()
        print(f"Your answer was {said}")
        speak_listen.say(f"Your answer was {said}",uuid)
        if symbol == "+":
            answer = option1 + option2
        elif symbol == "-":
            answer = option1 - option2
        elif symbol == "*":
            answer = option1 * option2
        elif symbol == "/":
            answer = option1 / option2
        if float(said) == answer:
            print("Correct!")
            speak_listen.say("Correct!",uuid)
            score =+ 1
        else:
            print("Incorrect!")
            speak_listen.say("Incorrect!",uuid)
        print(f"Your score is {score}")
        speak_listen.say(f"Your score is {score}",uuid)
        print("Would you like to continue?")
        speak_listen.say("Would you like to continue?",uuid)
        if choice == "voice":
            said = speak_listen.listen()
        elif choice == "text":
            lists = ["Yes","No","Stop"]
            layout = [[sg.Text("Would you like to continue?", size =(40, 1), font=40)],
            [sg.Combo(lists, key='-choice-', font=16),sg.Button("Submit")]]
            window = sg.Window("Check", layout, resizable=False)
            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                else:
                    if event == "Submit":
                        said = values["-choice-"]
                        if said == "None":
                            window.close()
                            self.maths(uuid,choice)
                        window.close()
        samples = {
        'sure' : {'func' : self.maths},
        'of course' : {'func' : self.maths},
        'yes' : {'func' : self.maths},
        'yeah' : {'func' : self.maths},
        'ok' : {'func' : self.maths},
        'no' : {'func' : self.exit},
        'stop' : {'func' : self.exit},

        }

        most_similar = determine_most_similar_phrase(said, samples)
        func = samples[most_similar]['func']
        func(uuid,choice,score)
    
    def exit(self,uuid,choice,score):
        print("Okay, goodbye!")
        speak_listen.say("Okay, goodbye!",uuid)
        sys.exit()

    def science(self,uuid,choice,score):
        print("Sorry, this feature is not available yet!")
        speak_listen.say("Sorry, this feature is not available yet!",uuid)
        sys.exit()
    
    def english(self,uuid,choice,score):
        print("Sorry, this feature is not available yet!")
        speak_listen.say("Sorry, this feature is not available yet!",uuid)
        sys.exit()
    
    def history(self,uuid,choice,score):
        print("Sorry, this feature is not available yet!")
        speak_listen.say("Sorry, this feature is not available yet!",uuid)
        sys.exit()
    
    def geography(self,uuid,choice,score):
        print("Sorry, this feature is not available yet!")
        speak_listen.say("Sorry, this feature is not available yet!",uuid)
        sys.exit()

    

quiz = Quiz()

        
