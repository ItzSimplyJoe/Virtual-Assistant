import os
import openai
from assistant_functions.speak_listen import speak_listen
import time
class GPT:
    def __init__(self):
        with open(r"C:\Users\Owner\OneDrive\Desktop\keys.key", "r") as file:
            for line in file:
                key1,key2,key3 = line.rstrip("\n").split(",")
        openai.api_key = key1
    def main(self,text,intent,uuid,choice):
        text = text.lower()
        if "using chat gpt" in text:
            text = text.replace("using chat gpt","")
        elif "using chatgpt" in text:
            text = text.replace("using chatgpt","")
        elif "usingchatgpt" in text:
            text = text.replace("usingchatgpt","")
        print("Give me a moment...")
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