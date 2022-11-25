from assistant_functions.speak_listen import speak_listen
import time
from serpapi import GoogleSearch


class wikisearch:
    def main(self,text,intent):

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
            print(boxmessage)
        except:
            try:
                organic_results = results['organic_results']
                abss = str(organic_results)
                start = "'snippet': '"
                end = "', '"
                boxmessage = (abss.split(start))[1].split(end)[0]
                print(boxmessage)  
                print("For more info, just google it.")
            except:
                try:
                    related_questions = results["related_questions"]
                    abss = str(related_questions)
                    print(abss)
                    start = "'snippet' : "
                    end = ", '"
                    boxmessage = (abss.split(start))[1].split(end)[0]
                    print(boxmessage)  
                except:
                    print("wgheriuhgieh")


wikisearch = wikisearch()