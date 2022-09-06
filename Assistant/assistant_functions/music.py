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

from assistant_functions.speak_listen import Speak_Listen

class music:
    def main(self,text,intent):
        text = text.lower()
        if 'play' in text:
            text = text.replace('play','')
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
        duration = video.duration
        hours,mins,seconds = duration.split(":")
        seconds = int(seconds)
        seconds2 = (int(mins) * 60)
        seconds3 = (int(hours) * 3600)
        vidlength = seconds + seconds2 + seconds3
        time.sleep(vidlength)
        media.stop()
    
music = music()