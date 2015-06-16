#!/usr/bin/env python
# coding: utf-8
#
# demo.py - I2PControl demo, show basic statistics.
# License: public domain / unlicense
#
# This is the same as running `python -m i2pcontrol` from a command line.

import i2py.i2pcontrol

a = i2pcontrol.I2PControl()
print(a.getNetworkSetting())
vals = a.getRouterInfo()
print(''.join([
    'You are running i2p version ', str(vals['i2p.router.version']), '. ',
    'It has been up for ', str(vals['i2p.router.uptime']), 'ms. ',
    'Your router knows ', str(vals['i2p.router.netdb.knownpeers']),' peers.'
    ]))
