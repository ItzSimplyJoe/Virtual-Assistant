from venv import create
import PySimpleGUI as sg
from mainprogramgui import maingui

def progress_bar():
    sg.theme('BlueMono')
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()



def create_account():
    sg.theme('Bluemono')
    layout = [[sg.Text("Sign Up", size =(17, 1), font=40, justification='c')],
             [sg.Text("E-mail", size =(17, 1),font=16), sg.InputText(key='-email-', font=16)],
             [sg.Text("Create Username", size =(17, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(17, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-Enter Password", size =(17, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                  "), sg.Button("Submit")]]

    window = sg.Window("Sign Up", layout)

    
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                email = values['-email-']
                username = values['-username-']
                if values['-password-'] != values['-rpassword-']:
                    sg.popup_error("Error! Passwords do not match!", font=16)
                    continue
                elif values['-password-'] == values['-rpassword-']:
                    password = values['-password-']
                    window.close()
                    accountcreation(email,username,password)
                    break
            elif event == "Back":
                window.close()
                mainpage()
    window.close()

def accountcreation(email,username,password):
    file = open("logincredentials.txt", "a")
    file.write ((email) + "," + (username) + "," + (password))
    file.write("\n")
    file.close()
    progress_bar()
    mainpage()

def login():
    sg.theme("Bluemono")
    layout = [[sg.Text("Log In", size =(15, 1), font=40)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-username-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-password-', password_char='*', font=16)],
             [sg.Button("Back"),  sg.Text("                                                                                                                                             "), sg.Button("Submit")]]


    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Back":
                window.close()
                mainpage()
            elif event == "Submit":
                password = values['-password-']
                username = values['-username-']
                checklogin(username,password)


    window.close()

def checklogin(supplied_username, supplied_password):
    logged_in = False
    with open('logincredentials.txt', 'r') as file:
        email, username, password = file.read().split('\n')
    file.close()
    if username == supplied_username and password == supplied_password:
        maingui()
    else:
        sg.popup("Invalid Login. Try again")


def mainpage():
    sg.theme("Bluemono")
    layout = [[sg.Text("    Welcome to my Virtual Assistant", size =(30, 1), font=40)],
            [sg.Button("Log In", size =(30, 1), font=40)],
            [sg.Text("", size =(30, 1), font=40)],
            [sg.Button("Sign Up", size =(30, 1), font=40)]]

    window = sg.Window("Virtual Assistant", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Log In":
                window.close()
                login()
            elif event == "Sign Up":
                window.close()
                create_account()

    window.close()


mainpage()