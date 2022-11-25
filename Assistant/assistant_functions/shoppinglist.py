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
        with open (f"{uuid}.txt", "a") as file:
            print("In your shopping list there is")
            for word in file:
                print(word)
    
    def listadd (self,text,uuid):
        text = text.lower()
        for word in text:
            if word == "add" or word == "to" or word == "shopping" or word == "list" or word == "please" or word == "my" or word == "can" or word == "you" or word == "put":
                text.replace(word,"")
        with open (f"{uuid}.txt", "a") as file:
            file.write(text)
            
 
shoppinglist = ShoppingList()