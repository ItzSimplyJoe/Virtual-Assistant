from assistant_functions.speak_listen import speak_listen
from assistant_functions.determine_most_similar import determine_most_similar_phrase
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class wikisearch:
    def main(self, text, intent):
        text = self.keyword(text)


    def search(self,text):

        try:
            question = text
            query = question.replace(' ','+')
            driver = webdriver.Chrome(r'C:\Users\Owner\OneDrive\Desktop\CleeveComp3\Assistant\ChromeSetup.exe')
            driver.get('https://www.google.com/search?q='+query)
            time.sleep(1.5)
            box = driver.find_element("xpath",'/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').click()
            content = driver.find_element("xpath",'//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div').get_attribute("textContent")
        except:
            try:
                result = wikipedia.summary(text, sentences = 2)
                speak_listen.say(result)
            except:
                try:
                    result = wikipedia.suggest(text)
                    speak_listen.say("Sorry, did you mean "+ result)
                    self.search(text)
                except:
                    speak_listen.say("yeh you have broken everything!")


    def keyword(self,text):
        text = text.lower()
        splitstring = text.split()
        string = ""
        for word in splitstring:
            if word != "what" and word !="when" and word !="how" and word !="where" and word !="a" and word !="is" and word !="who" and word !="was":
                string = (string +" " + word)
        self.search(string)
        


wikisearch = wikisearch()
