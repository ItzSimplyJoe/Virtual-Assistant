from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import math
import random

class maths:
    def main(self, input_text, text, intent):
        samples = {
            'add' : {'func' : self.printcalculate, 'type' : 'addition'},
            '+' : {'func' : self.printcalculate, 'type' : 'addition'},
            '-' : {'func' : self.printcalculate, 'type' : 'subtraction'},
            'x' : {'func' : self.printcalculate, 'type' : 'multiplication'},
            '*' : {'func' : self.printcalculate, 'type' : 'multiplication'},
            '/' : {'func' : self.printcalculate, 'type' : 'division'},
            'minus' : {'func' : self.printcalculate, 'type' : 'subtraction'},
            'take away' : {'func' : self.printcalculate, 'type' : 'subtraction'},
            'subtract' : {'func' : self.printcalculate, 'type' : 'subtraction'},
            'times' : {'func' : self.printcalculate, 'type' : 'multiplication'},
            'multiplied by' : {'func' : self.printcalculate, 'type' : 'multiplication'},
            'divded by' : {'func' : self.printcalculate, 'type' : 'division'}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        params = samples[most_similar]['param']
        speak_listen.say(func(params))
    
    def addition(self,input_text):
        numbers = []
        splitstring = input_text.split()
        for word in splitstring:
            if word.isdigit():
                numbers.append = int(word)
        total = 0
        for x in range (0,len(numbers)):
            total = total + numbers[x]
        return total

    def subtraction(self,input_text):
        numbers = []
        splitstring = input_text.split()
        for word in splitstring:
            if word.isdigit():
                numbers.append = int(word)
        total = numbers[0] - numbers [1]
        return total

    def multiplication(self,input_text):
        numbers = []
        splitstring = input_text.split()
        for word in splitstring:
            if word.isdigit():
                numbers.append = int(word)
        total = 0
        for x in range (0,len(numbers)):
            total = total * numbers[x]
        return total

    def division(self,input_text):
        numbers = []
        splitstring = input_text.split()
        for word in splitstring:
            if word.isdigit():
                numbers.append = int(word)
        total = numbers[0] / numbers [1]
        return total 
    
    def printcalculate(self, input_text, text):
        total = 0
        startofanswer = ["The answer is","The total is", " "]
        if type == 'addition':
            speak_listen.say(random.choice(startofanswer) + " " + self.addition(input_text))
        elif type == 'subtraction':
            speak_listen.say(random.choice(startofanswer) + " " + self.subtraction(input_text))
        elif type == 'multiplication':
            speak_listen.say(random.choice(startofanswer) + " " + self.multiplication(input_text))
        elif type == 'division':
            speak_listen.say(random.choice(startofanswer) + " " + self.division(input_text))


maths = maths()




