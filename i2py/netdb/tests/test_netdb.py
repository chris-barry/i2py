#!/usr/bin/env python
# coding: utf-8
#
# test_netdb.py - Test i2py.netdb.

import os,random
import i2py.netdb

'''
def test_inspect():
    netdb.inspect()
'''

def test_sha256():
    assert('d2f4e10adac32aeb600c2f57ba2bac1019a5c76baa65042714ed2678844320d0' == i2py.netdb.sha256('i2p is cool', raw=False))

def test_address_valid():
    invalid = i2py.netdb.Address()
    valid = i2py.netdb.Address()
    valid.cost = 10
    valid.transport = 'SSU'
    valid.options = {'host': '0.0.0.0', 'port': '1234', 'key': '', 'caps': ''}
    valid.expire = 0
    assert(valid.valid() and not invalid.valid())

def test_address_repr():
    valid = i2py.netdb.Address()
    valid.cost = 10
    valid.transport = 'SSU'
    valid.options = {'host': '0.0.0.0', 'port': '1234', 'key': '', 'caps': ''}
    valid.expire = 0
    assert(repr(valid) == 'Address: transport=SSU cost=10 expire=0 options={\'host\': \'0.0.0.0\', \'port\': \'1234\', \'key\': \'\', \'caps\': \'\'} location=None firewalled=False')

# TODO: test_entry*

def test_entry_read_short():
    assert(True)
def test_entry_read_mapping():
    assert(True)
def test_entry_read():
    assert(True)
def test_entry_read_short():
    assert(True)
def test_entry_read_byte():
    assert(True)
def test_entry_read_string():
    assert(True)
def test_entry_init():
    assert(True)
def test_entry_load():
    assert(True)
def test_entry_verify():
    assert(True)
def test_entry_repr():
    assert(True)
def test_entry_dict():
    assert(True)

# Make some garbage files and hope they break things.
def test_inspect_fuzz(tmpdir):
    sub = tmpdir.mkdir('fuzzdb')
    # Write 100 entries.
    for i in range(1,100):
        sub.join('entry{}.dat'.format(i)).write_binary(os.urandom(random.randint(2,400)))
    # Now let's inspect the garbage.
    i2py.netdb.inspect(netdb_dir='fuzzdb')
