#!/usr/bin/env python
# coding: utf-8
#
# restart.py - I2PControl demo, restart your router.
# License: public domain / unlicense

import i2py.control

a = i2py.control.I2PControl()
a.restart_graceful()
