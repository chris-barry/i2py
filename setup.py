#!/usr/bin/env python
from setuptools import setup

setup(name = 'i2py',
    version = '0.3',
    description = 'Tools to work with i2p.',
    author = 'See contributors.txt',
    author_email = 'Anonymous',
    classifiers = [
    'Development Status :: 3 - Alpha',
    #'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    ],
    install_requires = [      # If you plan on adding something, make it known why.
                              # Let's try to keep the dependencies minimal, okay?
    'bunch',                  # Needed by i2py.control.pyjsonrpc.
    'python-geoip',           # Needed by i2py.netdb.
    'python-geoip-geolite2',  # Needed by i2py.netdb.
    ],
    tests_require=['pytest'],
    url = 'https://github.com/chris-barry/i2py',
    packages = ['i2py', 'i2py.netdb', 'i2py.control', 'i2py.control.pyjsonrpc'],
)


