#!/usr/bin/python

import urllib
import argparse
from xml.etree import ElementTree
from termcolor import colored
import sys

def retrieveMovie (title):
	title=urllib.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&plot=full&t=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	#fall back to movie search if no movie is found
	for A in xml.iter('root'):
		if (A.get('response')=='False'):
			print "Movie not found!"
			sys.exit()
	xml=xml.getroot()
	printInfo(xml)
	return xml

#Search for movie and return plot for all the results
def movieSearch (title):
	title=urllib.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&s=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	xml=xml.getroot()
	for B in xml.findall('Movie'):
		apicall=retrieveMovie(B.get('Title'))
		printInfo(apicall)
	return xml

def printInfo(xml):
	for B in xml.findall('movie'):
			print colored("\n%s (%s) || %s || %s\n" %(B.get('title'),B.get('year'),
				B.get('runtime'),B.get('imdbRating')),'red')
			print colored("Director: %s\nActors: %s\n" %(B.get('director'),B.get('actors')), 'red')
			print colored("%s\n" %(B.get('plot')),'red')

if __name__=='__main__':
	parser=argparse.ArgumentParser(description='Command-Line Interface for the IMdB')

	parser.add_argument("-t", help="Search by title. Return first result")
	parser.add_argument("-s", help="Search and return results")

	args=parser.parse_args()
	choices=["None"]
	try:
		choices[0]=sys.argv[1]
		title=sys.argv[2]
	except:
		parser.print_usage()
		sys.exit()

	if choices[0]=="-t":	
		retrieveMovie(title)
	else:
		movieSearch(title)

	