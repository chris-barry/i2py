#!/usr/bin/env python
# coding: utf-8
#
# __main__.py - Main driver for i2py.netdb.

from .netdb import inspect

def print_entry(ent):
    print (ent)

if __name__ == '__main__':
    inspect(hook=print_entry)
