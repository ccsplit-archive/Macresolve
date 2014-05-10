#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Usage: macresolve [options]

Options:
    -h --help           Show this help.
    --version           Show the version.
    -a n --address n    The MAC Address to get information on.
    --update            Check for an update to the database.
"""
__author__ = 'Cory Shay (cshay237@gmail.com)'
__copyright__ = 'Copyright (c) 2014 Cory Shay'
__version__ = '1.1.0'
from docopt import docopt
import cPickle as cp
import urllib2

def main(args):
    print args

def get_updates():
    pass

def find_info(mac_address):
    pass
if __name__ == '__main__':
    main(docopt(__doc__, version="Macresolve v%s"%(__version__)))

