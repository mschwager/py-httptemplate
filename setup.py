#!/usr/bin/env python3

from setuptools import setup

import sys

PACKAGE_DIRECTORY = 'src'

sys.path.append(PACKAGE_DIRECTORY)

import httptemplate

setup(
    name=httptemplate.__name__,
    version=httptemplate.__version__,
    description='',
    url='',
    packages=['httptemplate'],
    package_dir={'': PACKAGE_DIRECTORY},
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
