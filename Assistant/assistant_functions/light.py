from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import tinytuya
import time


class Light:
    def main(self, text, intent):
        samples = {
            'turn my light on' : {'func' : self.on},
            'turn on my light' : {'func' : self.on},
            'turn my light off' : {'func' : self.off},
            'turn off my light' : {'func' : self.on},
            'make my light blue' : {'func' : self.colour},
            r'make the light 30% brightness' : {'func' : self.brightness},
            'set the light to max brightness' : {'func' : self.brightness},
            'make the light white' : {'func' : self.colour},
            'make the light rainbow' : {'func' : self.rainbow}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)
    def connect(self):
        light = tinytuya.BulbDevice('bfcacafeb83ddc1734wxrv', '192.168.1.199', '816a7355360cf18c')
        light.set_version(3.3)
        light.set_socketPersistent(True)
        return light

    def on(self,text):
        light = self.connect()
        light.turn_on()
    
    def off(self,text):
        light = self.connect()
        light.turn_off()

    def colour(self,text):
        light = self.connect()
        if "blue" in text:
            light.turn_on()
            light.set_colour(0,0,255)
        elif "green" in text:
            light.turn_on()
            light.set_colour(0,255,0)
        elif "red" in text:
            light.turn_on()
            light.set_colour(255,0,0)
        elif "aqua" in text:
            light.turn_on()
            light.set_colour(0,255,255)
        elif "white" in text:
            light.turn_on()
            light.set_white_percentage()
        elif "pink" in text:
            light.turn_on()
            light.set_colour(255,62,223)
        elif "orange" in text:
            light.turn_on()
            light.set_colour(255,127,0)
        elif "indigo" in text:
            light.turn_on()
            light.set_colour(46,43,95)
        elif "violet" in text:
            light.turn_on()
            light.set_colour(139,0,255)
        elif "yellow" in text:
            light.turn_on()
            light.set_colour(255,200,0)
        else:
            speak_listen.say("Unknown colour")
    def brightness(self,text):
        light = self.connect()
        if "10%" in text:
            light.set_brightness_percentage(brightness=10)
        elif "20%" in text:
            light.set_brightness_percentage(brightness=20)
        elif "30%" in text:
            light.set_brightness_percentage(brightness=30)
        elif "40%" in text:
            light.set_brightness_percentage(brightness=40)
        elif "50%" in text:
            light.set_brightness_percentage(brightness=50)
        elif "60%" in text:
            light.set_brightness_percentage(brightness=60)
        elif "70%" in text:
            light.set_brightness_percentage(brightness=70)
        elif "80%" in text:
            light.set_brightness_percentage(brightness=80)
        elif "90%" in text:
            light.set_brightness_percentage(brightness=90)
        elif "100%" in text:
            light.set_brightness_percentage(brightness=100)
        elif "max" in text:
            light.set_brightness_percentage(brightness=100)
        elif "Max" in text:
            light.set_brightness_percentage(brightness=100)
        elif "half" in text:
            light.set_brightness_percentage(brightness=50)
        elif "quater" in text:
            light.set_brightness_percentage(brightness=25)
        elif "three quaters" in text:
            light.set_brightness_percentage(brightness=75)
        else:
            speak_listen.say("Unknown value of brightness")
    def rainbow(self,text):
        light = self.connect()
        rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0],
              "green": [0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95],
              "violet": [139, 0, 255]}
        for i in range(10):
            for color in rainbow:
                [r, g, b] = rainbow[color]
                light.set_colour(r, g, b, nowait=True)
                time.sleep(0.25)




light = Light()



