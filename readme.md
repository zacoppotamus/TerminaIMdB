#TerminalMdB#

**TerminalMdB** is a *NIX command-line interface for the IMdB. It makes use of the excellent API over at www.omdbapi.com to retrieve
basic movie information.

##Usage

It would be useful to set up an alias for the command:

```alias imdb = python path/to/terminalMDB.py```

TerminalMDB can be used with one of two flags:

```imdb -t "foo" => search by title and return first result```

```imdb -s "bar" => search by title and return all results```


![Example](https://github.com/zacoppotamus/TerminaIMdB/raw/master/Screenshot.png)

##Notes

Requires Python 2.7+

Tested on OS X 10.8

Cool things can be done with data returned from **TerminalMdB**. Use your imagination!

##License

**TerminalMdB** is made available under the [GPL](http://www.gnu.org/licenses/gpl.html) (version 3 or later) 
