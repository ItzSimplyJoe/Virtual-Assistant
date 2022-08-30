import os
import pafy 
import vlc 
import time
import random
import re
import requests
import subprocess
import urllib.parse
import urllib.request

class Music:
    def main(self,text,intent):
        text = self.keywords(text)
        self.play(text)


    def play(self,text):
            query_string = urllib.parse.urlencode({"search_query": text})
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
            video = pafy.new(clip2) 
            videolink =video.getbestaudio()  
            print("audio is playing")  
            media = vlc.MediaPlayer(videolink.url)  
            media.play()
            time.sleep(30)
            media.stop()
            
    def keywords(self,text):
        text = text.lower()
        if 'play' in text:
            text.replace('play', '')
        

music = Music()
