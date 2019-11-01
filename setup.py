#! /usr/bin/env python
from setuptools import setup
import re
from os import path

version = ''
with open('cliff/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='mediacloud-cliff',
      version=version,
      description='Media Cloud CLIFF API Client Library',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Rahul Bhargava',
      author_email='rahulb@media.mit.edu',
      url='http://cliff.mediacloud.org',
      packages={'cliff'},
      package_data={'': ['LICENSE']},
      include_package_data=True,
      install_requires=['requests'],
      license='MIT',
      zip_safe=False
)
