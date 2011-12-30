#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pypanel',
    version='0.1',
    packages=['pypanel'],
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    url='http://www.pypanel.org/',
    description='PyPanel is a web hosting control panel written entirely in Python.',	 
    platforms=['linux', 'linux2'],
    license='MIT',
    scripts=[]
)
