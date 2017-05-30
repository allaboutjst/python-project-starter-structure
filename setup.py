# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

from setuptools import setup, find_packages

VERSION = (0, 1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()

f = open(join(dirname(__file__), 'LICENSE'))
license = f.read().strip()
f.close()

install_requires = [
    'pytest>=3.1.0',
]
tests_require = [
    'nose',
    'coverage',
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    install_requires.append('unittest2')

setup(
    name='pystructuresample',
    version='0.1.0',
    description='Python Project Structure Sample',
    long_description=long_description,
    author='dqi 2018',
    author_email='someone@company.com',
    url='https://github.com/dqi2018/python-structure',
    license=license,
    packages=find_packages(
        where='.',
        exclude=('tests', 'docs')
    ),
    # install_requires=install_requires,
    # test_suite='https://github.com/dqi2018/python-structure',
    # tests_require=tests_require
)
