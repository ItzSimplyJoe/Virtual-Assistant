import json
from assistant_functions.determine_most_similar import determine_most_similar_phrase
from assistant_functions.speak_listen import speak_listen
import random

def reply(text, intent,uuid,choice):
    with open(f'samples/{intent}.json') as samplesfile:  
        samples = json.load(samplesfile)

    most_similar = determine_most_similar_phrase(text = text, intent_dict = samples)

    if type(samples[most_similar]) == str:
        print(samples[most_similar])
        speak_listen.say(samples[most_similar],uuid)
    elif type(samples[most_similar]) == list:
        new = random.choice(samples[most_similar])
        print(new)
        speak_listen.say(new,uuid)