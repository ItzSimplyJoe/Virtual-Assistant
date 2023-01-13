import PySimpleGUI as sg
import pyttsx3


class TextFunctions:
    def voicenametocode(self,voice):
        if voice == "English Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM"
        elif voice == "English Female":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_HazelM"
        elif voice == "Australian Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_RyanM"
        elif voice == "Australian Female":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_CatherineM"
        elif voice == "Canadian Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_LiamM"
        elif voice == "Canadian Female":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_HeatherM"
        elif voice == "Indian Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM"
        elif voice == "Indian Female":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_PriyaM"
        elif voice == "American Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_ZiraM"
        elif voice == "American Female":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_JessaM"
        elif voice == "Irish Male":
            return "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIE_DanielM"

    def audiosettings(self,uuid,choice):
        sg.change_look_and_feel("DarkGrey3")
        list = ["English Male","English Female", "Australian Male", "Australian Female","Canadian Male", "Canadian Female","Indian Male","Indian Female","American Male","American Female","Irish Male"]
        layout = [[sg.Text("Audio Settings",font=("Helvetica", 25),text_color="white",background_color="black",justification="center",pad=(5, 3),key="-text-")],
        [sg.Text("Volume",font=("Helvetica", 15),text_color="white",background_color="black",justification="center",pad=(5, 3),key="-text-")],
        [sg.Slider(range=(0, 100), default_value=50, orientation='h', size=(34, 20), font=('Helvetica', 12), key="-volume-")],
        [sg.Text("Voice",font=("Helvetica", 15),text_color="white",background_color="black",justification="center",pad=(5, 3),key="-text-")],
        [sg.Combo(list, key="-voice-"),sg.Button("Play",font=("Helvetica", 15),key="-play-")],
        [sg.Button("Save",font=("Helvetica", 15),key="-save-"),sg.Button("Cancel",font=("Helvetica", 15),key="-cancel-")]]

        window = sg.Window("Audio Settings", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True, return_keyboard_events=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
            elif event == "-save-":
                try:
                    with open(f"assistant_functions/useraudiosettings/{uuid}.txt", "r") as file:
                        for line in file:
                            oldvolume,oldvoice = line.split(",")
                        file.flush()
                        file.close()
                        volume = values["-volume-"]
                        voice = values["-voice-"]
                        voicecode = self.voicenametocode(voice)
                        with open(f"assistant_functions/useraudiosettings/{uuid}.txt", "w") as file:
                            text = (f"{oldvolume},{oldvoice}")
                            file.write(text.replace(text),(f"{volume},{voicecode}"))
                            file.flush()
                            file.close()
                except:
                    volume = values["-volume-"]
                    voice = values["-voice-"]
                    voicecode = self.voicenametocode(voice)
                    with open(f"assistant_functions/useraudiosettings/{uuid}.txt", "w") as file:
                        file.write(f"{volume},{voicecode}")
                        file.flush()
                        file.close()
                    window.close()
                return
            elif event == "-play-":
                voice = values["-voice-"]
                voicecode = self.voicenametocode(voice)
                volume = values["-volume-"]
                engine = pyttsx3.init()
                engine.setProperty('voice', voicecode)
                engine.setProperty('volume', volume)
                engine.say("Hello, I am Badger how can i help?")
                engine.runAndWait()
                engine.stop()
            elif event == "-cancel-":
                window.close()
                return
    def lookscheck(self,uuid):
        with open (f"userconfigs/{uuid}.txt", "r") as file:
            for line in file:
                bodyfont,bodyfontsize,titlefont,titlefontsize,theme = line.split(",")
        return bodyfont,bodyfontsize,titlefont,titlefontsize,theme

    def fontandcolourassigner(self,uuid,choice,font,size,title,body,theme):
        with open (f"userconfigs/{uuid}.txt", "r") as file:
            for line in file:
                oldbodyfont,oldbodyfontsize,oldtitlefont,oldtitlefontsize,oldtheme = line.split(",")
        text = (f"{oldbodyfont},{oldbodyfontsize},{oldtitlefont},{oldtitlefontsize},{oldtheme}")
        if font != None or size != None:
            if title == True and body == True:
                with open(f"userconfigs/{uuid}.txt", "w") as file:
                    file.write(text.replace(text,(f"{font},{size},{font},{size},{oldtheme}")))
                    return
            if title == True:
                with open(f"userconfigs/{uuid}.txt", "w") as file:
                    file.write(text.replace(text,(f"{oldbodyfont},{oldbodyfontsize},{font},{size},{oldtheme}")))
                    return
            if body == True:
                with open(f"userconfigs/{uuid}.txt", "w") as file:
                    file.write(text.replace(text,(f"{font},{size},{oldtitlefont},{oldtitlefontsize},{oldtheme}")))
                    return
        if theme != None:
            with open(f"userconfigs/{uuid}.txt", "w") as file:
                file.write(text.replace(text,(f"{oldbodyfont},{oldbodyfontsize},{oldtitlefont},{oldtitlefontsize},{theme}")))
                return


    def font(self,uuid,choice):
        fonts = sg.Text.fonts_installed_list()
        sg.change_look_and_feel('DarkGrey3')
        layout = [[sg.Text('Oi Badger',
                        size=(20, 1),
                        click_submits=True,
                        relief=sg.RELIEF_GROOVE,
                        font='Courier` 25',
                        text_color='#FFFFFF',
                        background_color='black',
                        justification='center',
                        pad=(5, 3),
                        key='-text-',
                        tooltip='Text to see what it will look like',
                        )],
                [sg.Listbox(fonts, size=(30, 20), change_submits=True, key='-list-')],
                [sg.Text("Font Size", size=(10, 1), justification='right', pad=(0, 0))],
                [sg.Slider(range=(8, 36), orientation='h', size=(34, 20), default_value=25, key='-size-')],
                [sg.Text("**Warning**",size = (10,1),font = 'bold' ), sg.Text("If you make the text too big, it might not fit on the screen")],
                [sg.Text("Would you like to set this at the title font or just the font for the body of the text?", size=(50, 1), justification='right', pad=(0, 0))],                
                [sg.Checkbox("Title Font", key="-title-"), sg.Checkbox("Body Font", key="-body-")],
                [sg.Button('Save'), sg.Button("Exit"), sg.Button("Restore Defaults")]]

        window = sg.Window('Font Selection', layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)

        while True:     # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif event == "Save":
                font = values['-list-'][0]
                size = int(values['-size-'])
                title = values['-title-']
                body = values['-body-']
                window.close()
                if font == None:
                    sg.popup("Please select a font")
                    window.close()
                    self.font(uuid,choice)
                else:
                    return(font,size,title,body)
            elif event == "Restore Defaults":
                self.fontandcolourassigner(uuid,choice,"coolvetica rg",12,False,True,None)
                self.fontandcolourassigner(uuid,choice,"coolvetica compressed hv",35,True,False,None)
                window.close()
                return("Restore Defaults", None, False,False)
            text_elem = window['-text-']
            text_elem.update(font=(values['-list-'][0], int(values['-size-'])))
        window.close()


    def logout(self,uuid,choice):
        sg.change_look_and_feel('DarkGrey3')
        layout = [[sg.Text("Would you like to logout")],
                  [sg.Button("Yes"), sg.Button("No")]]
        window = sg.Window("Logout", layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                quit()
            elif event == "Yes":
                window.close()
                with open ("rememberme.txt", "w") as f:
                    text = f.read()
                    f.write(text.replace(text, ""))
                quit()
            elif event == "No":
                break
            else:
                continue
        window.close()

    def lookandfeelwindow(self,uuid,choice):
        colour_list = sg.list_of_look_and_feel_values()
        colour_list.sort()
        layout = [[sg.Text('Change the colours of the window')],
                [sg.Text('Click a colour to see demo window')],
                [sg.Listbox(values=colour_list,
                            size=(20, 12), key='-LIST-', enable_events=True)],
                [sg.Button('Exit'), sg.Button("Save"), sg.Button("Restore Defaults")]]

        window = sg.Window('Look and Feel Browser', layout, resizable=False, titlebar_background_color="grey", titlebar_text_color="white", titlebar_icon="bager.ico", icon="badger.ico", element_justification="center", finalize=True)

        while True:  # Event Loop
            event, values = window.read()
            if event in (None, 'Exit'):
                break
            elif event == "Save":
                theme = values['-LIST-'][0]
                window.close()
                return(theme)
            elif event == "Restore Defaults":
                window.close()
                return("DarkGrey3")
            sg.change_look_and_feel(values['-LIST-'][0])
            sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
        window.close()

textfunctions = TextFunctions()
