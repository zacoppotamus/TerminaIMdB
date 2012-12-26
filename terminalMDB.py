#!/usr/bin/python

import urllib
import argparse
import sys
from xml.etree import ElementTree


def getXML(**url_args):
    url_params = {
        'r': 'xml',
        'plot': 'full'
    }
    url_params.update(url_args)
    url = "http://www.omdbapi.com/?" + urllib.urlencode(url_params)
    xml = ElementTree.parse(urllib.urlopen(url))
    return xml


def retrieveMovie(xml):
    # fall back to movie search if no movie is found
    for A in xml.iter('root'):
        if (A.get('response') == 'False'):
            print "Movie not found!"
            sys.exit()
        else:
            xml = xml.getroot()
            printInfo(xml)


# Search for movie and return plot for all the results
def movieSearch(xml):
    xml = xml.getroot()
    print xml
    for B in xml.findall('Movie'):
        apicall = retrieveMovie(getXML(i = B.get('imdbID')))
    return xml


def printInfo(xml):
    for B in xml.findall('movie'):
        print "\n%s (%s) || %s || %s || %s\n" % (B.get('title'), B.get('year'),
                                           B.get('runtime'),
                                           B.get('imdbRating'),
                                           B.get('imdbID'))
        print "Director: %s\nActors: %s\n" % (B.get('director'),
                                              B.get('actors'))
        print "%s\n" % (B.get('plot'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Command-Line Interface for the IMdB')

    parser.add_argument("-t", help="Search by title. Return first result")
    parser.add_argument("-i", help="Search by id")
    parser.add_argument("-s", help="Search and return results")

    args = parser.parse_args()

    if args.t:
        retrieveMovie(getXML(t = args.t))
    elif args.i:
        retrieveMovie(getXML(i = args.i))
    elif args.s:
        movieSearch(getXML(s = args.s))
    else:
        parser.print_help()
