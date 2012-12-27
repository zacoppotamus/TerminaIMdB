#!/usr/bin/env python

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
    for node in xml.iter('root'):
        if node.get('response') == 'False':
            print "Movie not found!"
            sys.exit()
        else:
            xml = xml.getroot()
            printInfo(xml)


# Search for movie and return plot for all the results
def movieSearch(xml):
    xml = xml.getroot()
    for movie in xml.findall('Movie'):
        retrieveMovie(getXML(i=movie.get('imdbID')))


def printInfo(xml):
    for movie in xml.findall('movie'):
        print "{nl}{0} ({1}) || {2} || {3} || {4}{nl}".decode('utf-8').format(movie.get('title'), movie.get('year'),
                                                                              movie.get('runtime'),
                                                                              movie.get('imdbRating'),
                                                                              movie.get('imdbID'),
                                                                              nl='\n')
        print "Director: {0}{nl}Actors: {1}{nl}".decode('utf-8').format(movie.get('director'),
                                                                        movie.get('actors'), nl='\n')
        print movie.get('plot'), '\n'


def main():
    parser = argparse.ArgumentParser(description='Command-Line Interface for the IMdB')

    parser.add_argument("-t", help="Search by title. Return first result")
    parser.add_argument("-i", help="Search by id")
    parser.add_argument("-s", help="Search and return results")

    args = parser.parse_args()

    if args.t:
        retrieveMovie(getXML(t=args.t))
    elif args.i:
        retrieveMovie(getXML(i=args.i))
    elif args.s:
        movieSearch(getXML(s=args.s))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
