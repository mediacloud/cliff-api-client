#! /usr/bin/env python

from setuptools import setup
import sys, re, logging

version = ''
with open('mediameter/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

readme = ''
with open('README.md', 'r') as f:
    readme = f.read()

setup(name='mediameter-cliff',
    version=version,
    description='MediaMeter CLIFF API Client Library',
    long_description=readme,
    author='Rahul Bhargava',
    author_email='rahulb@media.mit.edu',
    url='http://cliff.mediameter.org',
    packages={'mediameter'},
    package_data={'':['LICENSE']},
    include_package_data=True,
    install_requires=['requests'],
    license='MIT',
    zip_safe=False
)
