#!/usr/bin/python

import urllib2
import urllib
from xml.etree import ElementTree
from termcolor import colored
import sys
##from xml.etree.ElementTree import parse

def retrieveXML (title):
	title=urllib2.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&t=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	#fall back to movie search if no movie is found
	for A in xml.iter('root'):
		if (A.get('response')=='False'):
			print "Movie not found!"
			sys.exit()
	xml=xml.getroot()
	return xml

#Search for movie and return plot for all the results
def movieSearch (title):
	title=urllib2.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&s=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	xml=xml.getroot()
	for B in xml.findall('Movie'):
		apicall=retrieveXML(B.get('Title'))
		printInfo(apicall)
	return xml

def printInfo(xml):
	for B in xml.findall('movie'):
			print colored("\n%s (%s) || %s || %s\n" %(B.get('title'),B.get('year'),B.get('runtime'),B.get('imdbRating')),'red')
			print colored("%s\n" %(B.get('plot')),'red')

if __name__=='__main__':
	title=raw_input("Movie: ")
	xml=movieSearch(title)
	printInfo(xml)







