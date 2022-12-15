import os
import openai
from assistant_functions.speak_listen import speak_listen
import time
class Searches:
    def main(self,text,intent,uuid,choice):
        print("Give me a moment...")
        openai.api_key = ("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")
        query = text
        model = "text-davinci-003"
        response = openai.Completion.create(
            engine=model,
            prompt=query, 
            max_tokens=2048,
            n=1,
            temperature=0.5,
        )
        
        words = response["choices"][0]["text"]
        print(words.replace('\n',''))
        speak_listen.say(words,uuid)
searches = Searches()