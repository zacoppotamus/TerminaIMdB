#!/usr/bin/env python
# -*- coding: utf-8 -
import os
from setuptools import setup

DIR=os.path.dirname(__file__)

setup(
    name='terminalmdb',
    version='0.0.3',
    description='CLI for IMDB',
    long_description=open(os.path.join(DIR, 'readme.md')).read(),
    author='Zac Ioannidis',
    author_email='me@izac.us',
    license=open(os.path.join(DIR, 'LICENSE')).read(),
    url='https://github.com/zacoppotamus/TerminaIMdB',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'License :: OSI Approved :: MIT License',
    ],
    py_modules=['terminalmdb'],
    entry_points={
        'console_scripts':
        ['imdb=terminalmdb:main'],
    })