#The Sign Up and Register Modules
#Importing the modules that are used to make this all functional
from tkinter import CENTER
import random
import PySimpleGUI as sg
import smtplib
from email.message import EmailMessage
import ssl
import os
from main import *
from text import *
from voice import *

def progress_bar(): ## A pointless progress bar for aethestics, works by increasing the amount completed by 1 each time the function loops
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

def create_account():#Account creation, broken down into the layout, and the functionality
    sg.theme('Bluemono')
    layout = [[sg.Text("Sign Up", size =(17, 1), font=40, justification='c')],
             [sg.Text("E-mail", size =(17, 1),font=16), sg.InputText(key='-email-', font=16)],
             [sg.Text("Create Username", size =(17, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(17, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-Enter Password", size =(17, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                  "), sg.Button("Submit")]]

    window = sg.Window("Sign Up", layout, resizable=True)

    #while the program is running check to see if the window has been closed
    while True:
        total = 0
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit": #if the button submit is pressed, it takes the values of the email, username and password boxes and checks if the two password boxes match
                email = values['-email-']
                username = values['-username-']
                if values['-password-'] != values['-rpassword-']:
                    sg.popup("Error! Passwords do not match!", font=16)
                    continue
                elif values['-password-'] == values['-rpassword-']: ## if they match, it adds all of the credentials to the logincredentials.txt
                    password = values['-password-']
                    with open('logincredentials.txt', 'r') as file:
                        for line in file:
                            email1,username1,password1 = line.rstrip("\n").split(",")
                            if email1 == email:
                                sg.popup("Someone has already signed up with that email!")
                                total = total + 1
                                continue
                            elif username1 == username:
                                total = total + 1
                                sg.popup("Someone has already signed up with that username!")
                                continue
                    if total > 0:
                        continue
                    elif total == 0:
                        window.close()
                        accountcreation(email,username,password)
                        break                    
            elif event == "Back":
                window.close()
                mainpage()
    window.close()

def accountcreation(email,username,password):
    file = open("logincredentials.txt", "a")
    file.write ((email) + "," + (username) + "," + (password) + "\n")
    file.close()
    progress_bar()
    mainpage()

def login():
    sg.theme("Bluemono")
    layout = [[sg.Text("Log In", size =(15, 1), font=40), sg.Text("                                                                 "), sg.Button("Forgotten Password?")],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-username-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-password-', password_char='*', font=16)],
             [sg.Button("Back"),  sg.Text("                                                                                                               "), sg.Button("Submit")]]


    window = sg.Window("Log In", layout, resizable=True)

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
                window.close()
                checklogin(username,password)
            elif event == "Forgotten Password?":
                window.close()
                forgottenpassword()


    window.close()

def forgottenpassword():
    sg.theme("Bluemono")
    fontsmall = ("Arial",11)
    fontbig = ("Arial",40)
    layout = [[sg.Text("Forgotten your password? ", size =(65, 1), font=40, justification=CENTER)],
            [sg.Text("                  No worries, just input your email here and a one time password will be sent to the email", size =(70, 1), font=fontsmall, justification=CENTER)],
            [sg.Text("                                                    This will allow you to create a new password", size =(65, 1), font=fontsmall)],
            [sg.Text("Email", size =(65, 1), font=16, justification=CENTER)],
            [sg.InputText(justification=CENTER, key='-email-', font=16, size=(65,1))],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                       "), sg.Button("Submit")]]
    window = sg.Window("Forgotten password", layout)


    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Back":
                window.close()
                login()
            elif event == "Submit":
                email = values['-email-']
                window.close()
                checkemail(email)
    window.close()

def checkemail(supplied_email):
    total = 0
    with open('Logincredentials.txt', 'r') as file:
        for line in file:
            email, username, password = line.rstrip("\n").split(",")
            if email == supplied_email:
                total = total + 1
        print(total)
        if total > 0:
            OTP(supplied_email)
        elif total == 0:
            sg.popup("That email does not have an account in the system, create an account instead!")

def checklogin(supplied_username, supplied_password):
    with open('Logincredentials.txt', 'r') as file:
        for line in file:
            email, username, password = line.rstrip("\n").split(",")
            if username == supplied_username:
                if password == supplied_password:
                    inputchoice()
        else:
            sg.popup("Incorrect login, please try again")
            login()

def mainpage():
    sg.theme("Bluemono")
    layout = [[sg.Text("    Welcome to my Virtual Assistant", size =(30, 1), font=40)],
            [sg.Button("Log In", size =(30, 1), font=40)],
            [sg.Text("", size =(30, 1), font=40)],
            [sg.Button("Sign Up", size =(30, 1), font=40)]]

    window = sg.Window("Virtual Assistant", layout, resizable=True)

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

def OTP(inputted_email):
    otp = random.randint(100000,999999)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('joesvirtualassistant@gmail.com' ,'kpflqtzddozqgjlj')

        subject = 'One Time Password'
        body = ('Your one time password is '+ str(otp))
        footer = ('This is an incredible virtual assistant created by Joe, the virtual assistant probably doesnt work very well. \n If this email is not for you please just ignore it. \n Thankyou very much,\n Joe')

        msg = f'Subject: {subject}\n\n{body}\n\n{footer}'

        smtp.sendmail('joesvirtualassistant@gmail.com', inputted_email, msg)
    OTPscreen(inputted_email,otp)

def OTPscreen(inputted_email,otp):
    sg.theme('Bluemono')
    layout = [[sg.Text("Change Password, check junk email!", size =(35, 1), font=40, justification='c')],
             [sg.Text("One Time Password", size =(20, 1), font=16), sg.InputText(key='-otp-', font=16)],
             [sg.Text("New Password", size =(20, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-Enter New Password", size =(20, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                  "), sg.Button("Submit")]]

    window = sg.Window("Change Password", layout, resizable=True)

    
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                email = inputted_email
                inputted_otp = values['-otp-']
                inputted_otp = int(inputted_otp)
                otp = int(otp)
                finalList = []
                if inputted_otp == otp:
                    if values['-password-'] != values['-rpassword-']:
                        sg.popup("Error! Passwords do not match!", font=16)
                        continue
                    elif values['-password-'] == values['-rpassword-']:
                        password = values['-password-']
                        with open("logincredentials.txt",'r') as file:
                            for line in file:
                                if line[-1] == "\n":
                                    finalList.append(line[:-1].split(','))
                                else:
                                    finalList.append(line.split(','))
                            data = finalList
                            for index in range(len(data)):
                                if inputted_email == data[index][0]:
                                    data[index][2] = password
                                    break
                            with open('logincredentials.txt', 'w') as file:
                                for line in data:
                                    print(','.join(line), file=file)
                            window.close()
                            login()
                            break 
                elif inputted_otp != otp:
                    sg.popup("One time password is not valid!")                       
            elif event == "Back":
                window.close()
                mainpage()
    window.close()

def inputchoice():
    sg.theme("Bluemono")
    layout = [[sg.Text("    Would you like to use Voice or Text?", size =(30, 1), font=40)],
            [sg.Button("Voice", size =(30, 1), font=40)],
            [sg.Text("", size =(30, 1), font=40)],
            [sg.Button("Text", size =(30, 1), font=40)]]

    window = sg.Window("Virtual Assistant", layout, resizable=True)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Voice":
                window.close()
                voice.main()
            elif event == "Text":
                window.close()
                text.main()

    window.close()

mainpage()