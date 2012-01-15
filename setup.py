#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    description='PyPanel is a web hosting control panel.',	 
    install_requires=['fabric', 'cuisine'],
    license='MIT',
    name='pypanel',
    packages=['pypanel'],
    platforms=['linux', 'linux2'],
    scripts=['scripts/install.py'],
    test_requires=['nose'],
    test_suite='nose.collector',
    url='http://www.pypanel.org/',
    version='0.1',
)
