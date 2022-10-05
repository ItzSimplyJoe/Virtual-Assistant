import tkinter
import customtkinter
from PIL import Image
from PIL import ImageTk
import pvporcupine
import pyaudio
import struct
from assistant_functions.speak_listen import speak_listen
from settings import *
from main import *
import random
import os

PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    WIDTH = 960
    HEIGHT = 540

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)

################## Creating Left and Right ##################
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

################## Left ##################

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        self.settings_image = self.load_image(r"\ImagesForUI\settings.png", 50)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left, image=self.settings_image, 
                                                text="Settings", width=40, height=40,
                                                command=self.settings)
        self.button_1.grid(row=11, column=0, columnspan=1, padx=20, pady=10, sticky="w")
################## Right ##################
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)



        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Enter Question for Badger")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Submit",
                                                border_width=2,
                                                fg_color=None,
                                                command=self.input)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

    def closing(self):
        self.destroy()

    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def settings(self):
        settings = Settings()
        settings.mainloop()

    def input(self):
        text = self.entry.get()
        assistant.reply(text)





#forlater#
#        vcl = VoiceCommandListener()
#        p1 = multiprocessing.Process(target=vcl.listenForVoiceCommands)
#        p2 = multiprocessing.Process(target=vcl.listenForTextCommands, args=[window])
#        p1.start()
#        p2.start()
#        p1.join()
#        p2.join()
 
    def listening(self):
        self.porcupine = None
        pa = None
        audio_stream = None


        self.porcupine = pvporcupine.create(
        access_key = "K3bYmOitsrCNs5ai3C0qQLkcKhWPaVd59cP5+tkpANbq0NCm1nBc7g==",
        keyword_paths = ['C:/Users/Owner/OneDrive/Desktop/CleeveComp3/Assistant/Keywords/badger.ppn'],
        keywords = ['Oi Badger']
        )   

        pa = pyaudio.PyAudio()
        print("Ready")

        while True:
            try:
                pcm = audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                keyword_index = self.porcupine.process(pcm)
                if keyword_index >= 0:
                    response = (random.choice["yes", "how can i help", "whats up", "how can i be of assistance", "i am listening"])
                    speak_listen.say(response)
                    print(response)
                    if audio_stream is not None:
                        audio_stream.close()
                    text = speak_listen.listen()
                    assistant.reply(text)
            except:
                audio_stream = pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length)


if __name__ == "__main__":
    app = App()
    app.mainloop()