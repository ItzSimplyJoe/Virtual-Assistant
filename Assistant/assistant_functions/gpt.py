import os
import openai
from assistant_functions.speak_listen import speak_listen
import time
class GPT:
    def main(self,text,intent,uuid,choice):
        text = text.lower()
        if "using chat gpt" in text:
            text = text.replace("using chat gpt","")
        elif "using chatgpt" in text:
            text = text.replace("using chatgpt","")
        elif "usingchatgpt" in text:
            text = text.replace("usingchatgpt","")
        print("Give me a moment...")
        openai.api_key = ("sk-")
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
gpt = GPT()