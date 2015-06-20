#!/usr/bin/env python
# coding: utf-8
#
# __main__.py - Interact with an i2p node through json-rpc.

from .control import *

# Little demo on how it could be used.
if __name__ == '__main__':
    a = I2PController()
    print(a.get_network_settings())
    vals = a.get_router_info()
    print(''.join([
        'You are running i2p version ', str(vals['i2p.router.version']), '. ',
        'It has been up for ', str(vals['i2p.router.uptime']), 'ms. ',
        'Your router knows ', str(vals['i2p.router.netdb.knownpeers']),' peers.'
        ]))
