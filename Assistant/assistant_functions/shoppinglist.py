from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase

class ShoppingList:
    def main(self,text,intent,uuid,choice):
        samples = {
            'whats on my shopping list' : {'func' : self.listcheck},
            'add tomatoes to my shopping list' : {'func' : self.listadd},
            'list whats on my shopping list' : {'func' : self.listcheck}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text,uuid)
    def listcheck (self,text,uuid):
        with open (f"assistant_functions/shoppinglists/{uuid}.txt", "r") as file:
            speak_listen.say("In your shopping list there is",uuid)
            for line in file:
                speak_listen.say(line,uuid)
    
    def listadd (self,text,uuid):
        text = text.lower().split(" ")
        new = []
        for word in text:
            if word == "add" or word == "to" or word == "shopping" or word == "list" or word == "please" or word == "my" or word == "can" or word == "you" or word == "put":
                continue
            else:
                new.append(word)
        with open (f"assistant_functions/shoppinglists/{uuid}.txt", "a") as file:
            new = str(new)
            new = new.replace("[","")
            new = new.replace("]","")
            new = new.replace("'","")
            file.write(f"{new}\n")
            
 
shoppinglist = ShoppingList()