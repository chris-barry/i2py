#!/usr/bin/env python
# coding: utf-8
#
# iterate.py - Iterate over the netdb and print router information.
# License: public domain / unlicense
#
# This is the same as running `python -m netdb` from a command line.

from i2py.netdb import inspect

def print_entry(ent):
    print (ent)

if __name__ == '__main__':
    inspect(hook=print_entry)

