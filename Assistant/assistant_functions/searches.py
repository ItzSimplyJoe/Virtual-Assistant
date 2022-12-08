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
            max_tokens=2048,
            n=1,
            temperature=0.5,
        )
        print(response["choices"][0]["text"])
        speak_listen(response["choices"][0]["text"],uuid)
    
searches = Searches()