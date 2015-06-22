#!/usr/bin/env python
# coding: utf-8
#
# test_control.py - Test i2py.control.
#
# ***** BEGIN NOTE *****
#
# This does not test the live server right now,
# the call rpc method is overwritten to return static data.
#
# Monkeypatch overwites the pyjsonrpc call and returns the raw json,
# it's usually not a full response since it won't help test, and is
# is annoying to write.
#
# ***** END NOTE *****

import i2py.control
import pytest

# Extend the main class, and make it so that the init does not rely on a real server.
class FakeI2PController(i2py.control.I2PController):
    def __init__(self):
        self._password = ''
        self._token = ''
        self._http_client = i2py.control.pyjsonrpc.HttpClient(url='http://example.com')

@pytest.fixture(autouse=True)
def no_real_auth(monkeypatch):
    monkeypatch.setattr('i2py.control.I2PController', FakeI2PController)

# TODO: Test bad token/api
def test_authenticate_good(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'API':1, 'Token':'123123'})
    a = i2py.control.I2PController()
    a.authenticate() # It's already called in .control's __init__, but it's be explicit.
    assert(a)

def test_authenticate_bad_api(monkeypatch):
    assert(True)

def test_authenticate_bad_pass(monkeypatch):
    assert(True)

def test_echo(monkeypatch):
    val = 'itoopie'
    a = i2py.control.I2PController()
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'Result':val})
    print a.echo(val)
    assert(a.echo(val) == val)
    
def test_get_rate(monkeypatch):
    val = 100
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'Result':val})
    a = i2py.control.I2PController()
    assert(a.get_rate(stat='i2p.test.value') == val)

# TODO: Waiting on http://trac.i2p2.i2p/ticket/1607
def test_set_settings(monkeypatch):
    assert(True)
    '''
    a = i2py.control.I2PController()
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'SettingsSaved': False, 'i2pcontrol.address': '127.0.0.1', 'RestartNeeded': False})
    ret = a.set_settings(address='6.6.6.6', port=666, password='666pass')
    assert(a['i2pcontrol.address'] == '6.6.6.6' and a['i2pcontrol.port'] == '666' and a['i2pcontrol.password'] == '666pass')
    '''

def test_get_router_info(monkeypatch):
    val = 100
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'i2p.router.net.bw.inbound.15s':val})
    a = i2py.control.I2PController()
    assert(a.get_router_info()['i2p.router.net.bw.inbound.15s'] == val)

def test_reseed(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'Reseed':None})
    a = i2py.control.I2PController()
    assert(not a.reseed()['Reseed'])

def test_restart(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'Restart':None})
    a = i2py.control.I2PController()
    assert(not a.reseed()['Restart'])

def test_restart_graceful(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'RestartGraceful':None})
    a = i2py.control.I2PController()
    assert(not a.reseed()['RestartGraceful'])

def test_shutdown(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'Shutdown':None})
    a = i2py.control.I2PController()
    assert(not a.reseed()['Shutdown'])

def test_shutdown_graceful(monkeypatch):
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'ShutdownGraceful':None})
    a = i2py.control.I2PController()
    assert(not a.reseed()['ShutdownGraceful'])

def test_set_network_settings(monkeypatch):
    val = 100
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'i2p.router.net.bw.share':val})
    a = i2py.control.I2PController()
    assert(a.set_network_settings()['i2p.router.net.bw.share'] == val)

def test_get_network_settings(monkeypatch):
    val = 100
    monkeypatch.setattr('i2py.control.pyjsonrpc.HttpClient.call', lambda a,b,c: {'i2p.router.net.bw.share':val})
    a = i2py.control.I2PController()
    assert(a.get_network_settings()['i2p.router.net.bw.share'] == val)

