from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import math
import random

class maths:
    def main(self, text, intent):
        samples = {
            'add' : {'func' : self.addition},
            '+' : {'func' : self.addition},
            '-' : {'func' : self.subtraction},
            'x' : {'func' : self.multiplication},
            '*' : {'func' : self.multiplication},
            '/' : {'func' : self.division},
            'minus' : {'func' : self.subtraction},
            'take away' : {'func' : self.subtraction},
            'subtract' : {'func' : self.subtraction},
            'times' : {'func' : self.multiplication},
            'multiplied by' : {'func' : self.multiplication},
            '√' : {'func' : self.squareroot},
            'squareroot' :{'func' : self.squareroot},
            'square' :{'func' : self.square},
            'squared' :{'func' : self.square},
            'divded by' : {'func' : self.division}
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
        self.printcalculate(total)

    def subtraction(self,text):
        numbers = self.splittext(text)
        total = int(numbers[0]) - int(numbers[1])
        self.printcalculate(total)

    def multiplication(self,text):
        numbers = self.splittext(text)
        total = 1
        for x in range (0,len(numbers)):
            total = total * int(numbers[x])
        self.printcalculate(total)

    def division(self,text):
        numbers = self.splittext(text)
        total = int(numbers[0]) / int(numbers[1])
        self.printcalculate(total)

    def square(self,text):
        numbers = self.splittext(text)
        total = maths.square(numbers[0])
        self.printcalculate(total)

    def squareroot(self,text):
        numbers = self.splittext(text)
        total = maths.squareroot(numbers[0])
        self.printcalculate(total)
    
    def printcalculate(self, text):
        startofanswer = ["The answer is","The total is", " "]
        text = (random.choice(startofanswer) + " " + str(text))
        speak_listen.say(text)
maths = maths()

