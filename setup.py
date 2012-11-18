#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    description='PyPanel is a web hosting control panel.',	 
    install_requires=['cuisine', 'django', 'django-celery', 'fabric',
                      'MySQL-pytho', 'psycopg2'],
    license='MIT',
    name='pypanel',
    packages=['pypanel'],
    platforms=['linux', 'linux2'],
    scripts=['scripts/install.py'],
    tests_require=['nose'],
    test_suite='nose.collector',
    url='http://pypanel.org/',
    version='0.0.1',
    include_package_data=True,
    zip_safe=False,
)
