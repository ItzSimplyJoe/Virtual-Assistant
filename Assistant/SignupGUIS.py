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
import string 
from cryptography.fernet import Fernet
from textfunctions import *
QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'


def progress_bar(): ## A pointless progress bar for aethestics, works by increasing the amount completed by 1 each time the function loops
    #sg.theme('BlueMono')
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()

def create_account():#Account creation, broken down into the layout, and the functionality
    #sg.theme('Bluemono')
    layout = [[sg.Text("Sign Up", size =(17, 1), font=40, justification='c')],
             [sg.Text("E-mail", size =(17, 1),font=16), sg.InputText(key='-email-', font=16)],
             [sg.Text("Create Username", size =(17, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(17, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-Enter Password", size =(17, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                  "), sg.Button("Submit")]]

    window = sg.Window("Sign Up", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)

    #while the program is running check to see if the window has been closed
    while True:
        total = 0
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit" or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2): #if the button submit is pressed, it takes the values of the email, username and password boxes and checks if the two password boxes match
                email = values['-email-']
                username = values['-username-']
                if values['-password-'] == "" or email == "" or username == "":
                    sg.popup("Please fill in all of the boxes!", font=16)
                else:
                    if values['-password-'] != values['-rpassword-']:
                        sg.popup("Error! Passwords do not match!", font=16)
                        continue
                    elif values['-password-'] == values['-rpassword-']: ## if they match, it adds all of the credentials to the logincredentials.txt
                        password = values['-password-']
                        if len(password) < 7:
                            sg.popup("Error Password must be at least 8 characters long")
                            total += 1
                            continue
                        elif len(password) > 7:
                            if " " in password:
                                sg.popup("Password must not contain spaces")
                                total +=1
                            else:
                                with open('logincredentials.txt', 'r') as file:
                                    for line in file:
                                        if "b'" in line:
                                            line = line.replace("b'", "")
                                            line = line.replace("'","")
                                        text = line.encode()
                                        line = decrpyt(text)
                                        email1,username1,password1,uuid = line.rstrip("\n").split(",")
                                        if email1 == email:
                                            sg.popup("Someone has already signed up with that email!")
                                            total += 1
                                            continue
                                        elif username1 == username:
                                            total += 1
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

def accountcreation(email,username,password):#The account creation module, broken down into the layout and the functionality
    file = open("logincredentials.txt", "a")
    uuid = ''.join(random.choice(string.ascii_letters) for i in range(20))
    with open (f'userconfigs/{uuid}.txt', 'a') as f:
        f.write("coolvetica rg,12,coolvetica compressed hv,35,DarkGrey3")
        f.flush()
        f.close()
    text = ((email) + "," + (username) + "," + (password) + "," + (uuid))
    text = encrypt(text)
    file.write(str(text) + "\n")
    file.close()
    progress_bar()
    inputchoice(uuid,username)

def login(): # The login module, broken down into the layout and the functionality
    #sg.theme("Bluemono")
    layout = [[sg.Text("Log In", size =(15, 1), font=40), sg.Text("                                                                                        "), sg.Button("Forgotten Password?")],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-username-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-password-', password_char='*', font=16)],
            [sg.Checkbox("Remember Me", key="-rememberme-")],
             [sg.Button("Back"),  sg.Text("                                                                                                                                             "), sg.Button("Submit")]]


    window = sg.Window("Log In", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Back":
                window.close()
                mainpage()
            elif event == "Submit" or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                password = values['-password-']
                username = values['-username-']
                if password == "" or username == "":
                    sg.popup("Please fill in all of the boxes!", font=16)
                    continue
                else:
                    if values['-rememberme-'] == True:
                        window.close()
                        checklogin(username,password,True)
                    else:
                        window.close()
                        checklogin(username,password,False)

            elif event == "Forgotten Password?":
                window.close()
                forgottenpassword()


    window.close()

def forgottenpassword():#The forgotten password module, broken down into the layout and the functionality
    #sg.theme("Bluemono")
    fontsmall = ("Arial",11)
    fontbig = ("Arial",40)
    layout = [[sg.Text("Forgotten your password? ", size =(65, 1), font=40, justification=CENTER)],
            [sg.Text("                  No worries, just input your email here and a one time password will be sent to the email", size =(70, 1), font=fontsmall, justification=CENTER)],
            [sg.Text("                                                    This will allow you to create a new password", size =(65, 1), font=fontsmall)],
            [sg.Text("Email", size =(65, 1), font=16, justification=CENTER)],
            [sg.InputText(justification=CENTER, key='-email-', font=16, size=(65,1))],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                       "), sg.Button("Submit")]]
    window = sg.Window("Forgotten password", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)


    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Back":
                window.close()
                login()
            elif event == "Submit" or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                email = values['-email-']
                window.close()
                checkemail(email)
    window.close()

def checkemail(supplied_email):#Checks if the email is in the system, if it is, it sends an OTP to the email
    total = 0
    with open('Logincredentials.txt', 'r') as file:
        for line in file:
            if "b'" in line:
                line = line.replace("b'", "")
                line = line.replace("'","")
            text = line.encode()
            line = decrpyt(text)
            email, username, password, uuid = line.rstrip("\n").split(",")
            if email == supplied_email:
                total = total + 1
        print(total)
        if total > 0:
            OTP(supplied_email)
        elif total == 0:
            sg.popup("That email does not have an account in the system, create an account instead!")

def checklogin(supplied_username, supplied_password, rememberme):#Checks if the login details are correct
    with open('Logincredentials.txt', 'r') as file:
        for line in file:
            if "b'" in line:
                line = line.replace("b'", "")
                line = line.replace("'","")
            text = line.encode()
            line = decrpyt(text)
            email, username, password,uuid = line.rstrip("\n").split(",")
            uuid = uuid
            if username == supplied_username:
                if password == supplied_password:
                    if rememberme == True:
                        with open('rememberme.txt', 'a') as file:
                            file.write(str(uuid))
                            file.flush()
                            file.close()
                            inputchoice(uuid,username)
                    else:
                        inputchoice(uuid,username)
        if username != supplied_username or password != supplied_password:
            sg.popup("Incorrect login, please try again")
            login()

def mainpage():#The main page module, broken down into the layout and the functionality
    #sg.theme("BlueMono")
    layout = [[sg.Text("    Welcome to my Virtual Assistant", size =(30, 1), font=40)],
            [sg.Button("Log In", size =(30, 1), font=40)],
            [sg.Text("", size =(30, 1), font=40)],
            [sg.Button("Sign Up", size =(30, 1), font=40)]]

    window = sg.Window("Virtual Assistant", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)

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

def OTP(inputted_email):#The OTP module, broken down into the layout and the functionality
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

def OTPscreen(inputted_email,otp):#The OTP screen module, broken down into the layout and the functionality
    #sg.theme('Bluemono')
    layout = [[sg.Text("Change Password, check junk email!", size =(35, 1), font=40, justification='c')],
             [sg.Text("One Time Password", size =(20, 1), font=16), sg.InputText(key='-otp-', font=16)],
             [sg.Text("New Password", size =(20, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Text("Re-Enter New Password", size =(20, 1), font=16), sg.InputText(key='-rpassword-', font=16, password_char='*')],
             [sg.Button("Back"),  sg.Text("                                                                                                                                                  "), sg.Button("Submit")]]

    window = sg.Window("Change Password", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)

    
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit" or event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):
                email = inputted_email
                inputted_otp = values['-otp-']
                inputted_otp = str(inputted_otp)
                otp = str(otp)
                finalList = []
                if inputted_otp == otp:
                    if values['-password-'] != values['-rpassword-']:
                        sg.popup("Error! Passwords do not match!", font=16)
                        continue
                    elif values['-password-'] == values['-rpassword-']:
                        password = values['-password-']
                        password = encrypt(password)
                        password = str(password)
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

def inputchoice(uuid,username):#The input choice module, broken down into the layout and the functionality
    #sg.theme("Bluemono")
    bodyfont,bodyfontsize,titlefont,titlefontsize,style = textfunctions.lookscheck(uuid)
    bodyfonts = (bodyfont,int(bodyfontsize))
    titlefont = (titlefont,int(titlefontsize))
    sg.change_look_and_feel(style)
    layout = [[sg.Text(f"Welcome back {username}", size = (30,1), font = 40, justification = CENTER)],
            [sg.Text("Would you like to use Voice or Text?", size =(30, 1),justification = CENTER,  font=30)],
            [sg.Button("Voice", size =(30, 1), font=40)],
            [sg.Text("", size =(30, 1), font=40)],
            [sg.Button("Text", size =(30, 1), font=40)]]

    window = sg.Window("Virtual Assistant", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Voice":
                window.close()
                voice.main(uuid,"voice")
            elif event == "Text":
                window.close()
                text.main(uuid,"text")

    window.close()

def encrypt(text):# The encryption module
    message = text
    key = b'j5CqBXeLXLEjvHBJm6_RIigxtxx0pjdMZc3d7u65aFY='
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decrpyt(text):# The decryption module
    message = text
    key = b'j5CqBXeLXLEjvHBJm6_RIigxtxx0pjdMZc3d7u65aFY='
    fernet = Fernet(key)
    decMessage = fernet.decrypt(message).decode()
    return decMessage

def checkforsavedlogin():
    with open ("rememberme.txt","r") as f:
        uuid1 = f.read()
        if len(uuid1) == 20:
            with open('Logincredentials.txt', 'r') as file:
                for line in file:
                    if "b'" in line:
                        line = line.replace("b'", "")
                        line = line.replace("'","")
                    text = line.encode()
                    line = decrpyt(text)
                    email, username, password,uuid = line.rstrip("\n").split(",")
                    if uuid == uuid1:
                        file.close()
                        inputchoice(uuid,username)
                    else:
                        continue
        else:
            mainpage()

checkforsavedlogin()
