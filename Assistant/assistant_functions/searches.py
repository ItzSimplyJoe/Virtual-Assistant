import os
import openai
from assistant_functions.speak_listen import speak_listen
import time
class Searches:
    def main(self,text,intent,uuid,choice):
        openai.api_key = ("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")
        query = text
        model = "text-davinci-003"
        response = openai.Completion.create(
            engine=model,
            prompt=query,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        print(response)
    
searches = Searches()