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
        text = self.keyword(text)
        self.play(text)


    def play(self,text):
        songname = urllib.parse.urlencode({"search_query": text})
        url = urllib.request.urlopen("https://www.youtube.com/results?" + songname)
        results = re.findall(r"watch\?v=(\S{11})", url.read().decode())
        clip = "https://www.youtube.com/watch?v=" + "{}".format(results[0])
        self._dislikes = 0
        video = pafy.new(clip) 
        videolink =video.getbestaudio()
        media = vlc.MediaPlayer(videolink.url)  
        media.play()
        time.sleep(video.duration)
        media.stop()
            
    def keyword(self,text):
        text = text.lower()
        if 'play' in text:
            text.replace('play', '')
        return text
        

music = Music()
