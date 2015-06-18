#! /usr/bin/env python

from setuptools import setup

setup(name='mediameter-cliff',
  version='1.0',
  description='MediaMeter CLIFF API Client Library',
  author='Rahul Bhargava',
  author_email='rahulb@media.mit.edu',
  url='http://cliff.mediameter.org',
  packages={'mediameter': 'mediameter',
            'mediameter.test': 'mediameter/test'},
  package_data={'mediameter.test':['fixtures/*.json']},
  install_requires=['requests']
)
