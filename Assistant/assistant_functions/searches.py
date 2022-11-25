from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import time
from serpapi import GoogleSearch


class Searches:
    def main(self,text,intent):
        samples = {
            'translate hello into french' : {'func' : self.translationsearch},
            'whats the population in china' : {'func' : self.websearch},
            'how old is king charles' : {'func' : self.websearch},
            'when did dianna die' : {'func' : self.websearch},
            'how long is a drive to london from bishops cleeve' : {'func' : self.websearch},
            'what was the england vs iran score' : {'func' : self.sportsresults}
        }
        
        most_similar = determine_most_similar_phrase(text, samples)
        func = samples[most_similar]['func']
        func(text)

    def translationsearch(self,text,intent):
        params = {
        "q": text,
        "hl": "en",
        "gl": "uk",
        "api_key": "66389e9d77c7a748284122ebe6862574e12d62c7ec9b1b37774c279adebc5a77"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        try:
            translation = results["answer_box"]
            abss = str(translation)
            
            start ="'target': "
            end="}"
            boxmessage = (abss.split(start))[1].split(end)[0]
            start = "'text': '"
            end = "'"
            boxmessage = (boxmessage.split(start))[1].split(end)[0]
            speak_listen.say(boxmessage)
        except:
            print("Something is broken please try again")


    def websearch(self,text,intent):
        params = {
        "q": text,
        "hl": "en",
        "gl": "uk",
        "api_key": "66389e9d77c7a748284122ebe6862574e12d62c7ec9b1b37774c279adebc5a77"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        try:
            answer_box = results["answer_box"]
            abss = str(answer_box)
            start ="'answer': '"
            end="', '"
            boxmessage = (abss.split(start))[1].split(end)[0]
            speak_listen.say(boxmessage)
        except:
            try:
                organic_results = results['organic_results']
                abss = str(organic_results)
                start = "'snippet': '"
                end = "', '"
                boxmessage = (abss.split(start))[1].split(end)[0]
                speak_listen.say(boxmessage)  
                speak_listen.say("For more info, just google it.")
            except:
                try:
                    related_questions = results["related_questions"]
                    abss = str(related_questions)
                    start = "'snippet' : "
                    end = ", '"
                    boxmessage = (abss.split(start))[1].split(end)[0]
                    speak_listen.say(boxmessage)  
                except:
                    print("Something is broken please try again")

    def sportsresults(self,text,intent):
        params = {
        "q": text,
        "hl": "en",
        "gl": "uk",
        "api_key": "66389e9d77c7a748284122ebe6862574e12d62c7ec9b1b37774c279adebc5a77"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        try:
            sports_results = results['sports_results']
            abss = str(sports_results)
            # leugue, team 1, team 2, score
            leustart = " {'league': '"
            leuend = "', '"
            league = (abss.split(leustart))[1].split(leuend)[0]
            teamonestart = "'teams': [{'name': '"
            teamoneend = "', 'thumbnail': "
            teamone = (abss.split(teamonestart))[1].split(teamoneend)[0]
            teamone_score_start = "', 'score': '"
            teamone_score_end = "'}, {'name': '"
            teamone_score = (abss.split(teamone_score_start))[1].split(teamone_score_end)[0]
            teamtwostart = "'}, {'name': '"
            teamtwoend = "', 'thumbnail': '"
            teamtwo = (abss.split(teamtwostart))[1].split(teamtwoend)[0]
            abss = (abss.split(", {'name': "))[1].split(r"}}")[0]
            teamtwo_score_start = "', 'score': '"
            teamtwo_score_end = "'}]"
            teamtwo_score = (abss.split(teamtwo_score_start))[1].split(teamtwo_score_end)[0]
            speak_listen.say(f"{league} - {teamone} {teamone_score} - {teamtwo_score} {teamtwo}")
        except:
            print("Something is broken please try again")



searches = Searches()
searches.sportsresults("What is the Qatar score", "intent")