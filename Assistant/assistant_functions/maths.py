from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import math
import random

class Maths:
    def main(self, text, intent, uuid, choice):
        samples = {
            'add' : {'func' : self.addition},
            '+' : {'func' : self.addition},
            '-' : {'func' : self.subtraction},
            'x' : {'func' : self.multiplication},
            '*' : {'func' : self.multiplication},
            '/' : {'func' : self.division},
            'What is 7 / 4' : {'func' : self.division},
            'What is 8 x 5' : {'func' : self.multiplication},
            'What is 2 + 64' : {'func' : self.addition},
            'What is 35 - 3' : {'func' : self.subtraction},
            'What is 35 / 5' : {'func' : self.division},
            'What is 23 x 35' : {'func' : self.multiplication},
            'What is 9 - 52' : {'func' : self.subtraction},
            'What is 235 + 23' : {'func' : self.addition},
            'minus' : {'func' : self.subtraction},
            'take away' : {'func' : self.subtraction},
            'subtract' : {'func' : self.subtraction},
            'times' : {'func' : self.multiplication},
            'multiplied by' : {'func' : self.multiplication},
            '√' : {'func' : self.squareroot},
            'squareroot' :{'func' : self.squareroot},
            'square' :{'func' : self.square},
            'squared' :{'func' : self.square},
            'divded by' : {'func' : self.division},
            'divide' : {'func' : self.division},
            'divided by' : {'func' : self.division},
            'over' : {'func' : self.division},
            'plus' : {'func' : self.addition},
            'add' : {'func' : self.addition}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text, uuid)


    def splittext(self,text,uuid):
        numbers = []
        lower = text.lower()
        split = lower.split()
        for word in split:
            if word.isdigit():
                numbers.append(word)
        return numbers
    
    def addition(self,text,uuid):
        numbers = self.splittext(text,uuid)
        total = 0
        for x in range (0,len(numbers)):
            total = total + int(numbers[x])
        self.printcalculate(total,uuid)

    def subtraction(self,text,uuid):
        numbers = self.splittext(text,uuid)
        total = int(numbers[0]) - int(numbers[1])
        self.printcalculate(total,uuid)

    def multiplication(self,text,uuid):
        numbers = self.splittext(text,uuid)
        total = 1
        for x in range (0,len(numbers)):
            total = total * int(numbers[x])
        self.printcalculate(total,uuid)

    def division(self,text,uuid):
        numbers = self.splittext(text,uuid)
        total = int(numbers[0]) / int(numbers[1])
        self.printcalculate(total,uuid)

    def square(self,text,uuid):
        numbers = self.splittext(text,uuid)
        total = maths.square(numbers[0])
        self.printcalculate(total,uuid)

    def squareroot(self,text, uuid):
        numbers = self.splittext(text,uuid)
        total = maths.squareroot(numbers[0])
        self.printcalculate(total,uuid)
    
    def printcalculate(self, text, uuid):
        startofanswer = ["The answer is","The total is", " "]
        text = (random.choice(startofanswer) + " " + str(text))
        print(text)
        speak_listen.say(text,uuid)
maths = Maths()

