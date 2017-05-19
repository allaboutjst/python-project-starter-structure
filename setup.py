# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

VERSION = (5, 4, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    'urllib3>=1.8, <2.0',
]
tests_require = [
    'nose',
    'coverage',
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    install_requires.append('unittest2')

setup(
    name = 'elasticsearch',
    description = "Python Project Structure Demo",
    license="Apache License, Version 2.0",
    long_description = long_description,
    version = __versionstr__,
    author = "John Doe",
    author_email = "john.doe@gmail.com",
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch*', )
    ),
    install_requires=install_requires,

    test_suite='test_elasticsearch.run_tests.run_all',
    tests_require=tests_require,
)
