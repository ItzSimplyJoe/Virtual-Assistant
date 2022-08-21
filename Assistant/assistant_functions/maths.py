from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import math
import random

class maths:
    def main(self, text, intent):
        samples = {
            'add' : {'func' : self.addition, 'type' : 'addition'},
            '+' : {'func' : self.addition, 'type' : 'addition'},
            '-' : {'func' : self.subtraction, 'type' : 'subtraction'},
            'x' : {'func' : self.multiplication, 'type' : 'multiplication'},
            '*' : {'func' : self.multiplication, 'type' : 'multiplication'},
            '/' : {'func' : self.division, 'type' : 'division'},
            'minus' : {'func' : self.subtraction, 'type' : 'subtraction'},
            'take away' : {'func' : self.subtraction, 'type' : 'subtraction'},
            'subtract' : {'func' : self.subtraction, 'type' : 'subtraction'},
            'times' : {'func' : self.multiplication, 'type' : 'multiplication'},
            'multiplied by' : {'func' : self.multiplication, 'type' : 'multiplication'},
            'divded by' : {'func' : self.division, 'type' : 'division'}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)


    def splittext(self,text):
        numbers = []
        lower = text.lower()
        split = text.split()
        for word in split:
            if word.isdigit():
                numbers.append(word)
        return numbers
    
    def addition(self,text):
        numbers = self.splittext(text)
        total = 0
        for x in range (0,len(numbers)):
            total = total + int(numbers[x])
        print(total)
        self.printcalculate(total)

    def subtraction(self,text):
        numbers = self.splittext(text)
        total = int(numbers[0]) - int(numbers[1])
        print(total)
        self.printcalculate(total)

    def multiplication(self,text):
        numbers = self.splittext(text)
        total = 1
        for x in range (0,len(numbers)):
            total = total * int(numbers[x])
        print(total)
        self.printcalculate(total)

    def division(self,text):
        numbers = self.splittext(text)
        total = int(numbers[0]) / int(numbers[1])
        print(total)
        self.printcalculate(total)
    
    def printcalculate(self, text):
        startofanswer = ["The answer is","The total is", " "]
        text = (random.choice(startofanswer) + " " + str(text))
        speak_listen.say(text)
maths = maths()

