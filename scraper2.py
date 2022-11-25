#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib, urllib2      
import re, time, random

searchForWhat = "Art is"
seitenAnzahl = 10
textAusgabe = ""

### Create opener with Google-friendly user agent
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0')]

### Returns span tags from search results
def getResults(opener, searchTerm, pageIndex):
	# Prepare the url string
	urlstring = "https://www.google.ch/search?"
	searchPath = "q=\"%s\"&start=%d" %(searchTerm,pageIndex)
	path = searchPath.replace(' ','+')
	urlstring += path
	# open page
	page = opener.open(urlstring)
	htmlSource = page.read() 
	# cook the soup
	soup = BeautifulSoup(htmlSource, 'html.parser')
	spans = soup.find_all('span', {'class' : 'st'})
	links = soup.find_all('h3', {'class' : 'r'})
	return spans

for i in range(seitenAnzahl):
	results = getResults(opener, searchForWhat,i*10)
	time.sleep(random.random())
	for j in range(len(results)):
		try:
			customRegex = r"(" + re.escape(searchForWhat) + ".*)"
			match = re.search(customRegex, results[j].text,re.IGNORECASE)
			textAusgabe += match.group().encode('utf-8') + "\n"
		except AttributeError:
			continue

print (textAusgabe)
