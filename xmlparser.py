#!/usr/bin/python

import urllib2
import urllib
from xml.etree import ElementTree
##from xml.etree.ElementTree import parse

title=raw_input("Movie: ")
title=urllib2.quote(title.encode("utf8"))
URL="http://www.omdbapi.com/?r=xml&t=%s" % title
apicall=urllib.urlopen(URL)
result=apicall.read()

f=open("output.xml", "w")
f.write(result)
f.close()

xml = ElementTree.parse('output.xml')
xml=xml.getroot()
for B in xml.findall('movie'):
	print "Title: %s (%s), %s" %(B.get('title'),B.get('year'),B.get('imdbRating'))
	print "%s" %(B.get('plot'))
apicall.close()





