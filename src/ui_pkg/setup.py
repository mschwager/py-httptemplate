#!/usr/bin/env python3

from setuptools import setup

import codecs
import os

PACKAGE_NAME = 'uitemplate'

here = os.path.abspath(os.path.dirname(__file__))
about_filename = os.path.join(
    here,
    PACKAGE_NAME,
    'about.py',
)
about = {}

with codecs.open(about_filename, 'r', 'utf-8') as fd:
    exec(fd.read(), about)

setup(
    name=about['__name__'],
    version=about['__version__'],
    description=about['__description__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=[PACKAGE_NAME],
    package_data={
        PACKAGE_NAME: [
            'templates/*',
            'static/*',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        "aiodns==1.1.1",
        "aiohttp==2.3.8",
        "aiohttp-jinja2==0.14.0",
        "cchardet==2.1.1",
    ],
)
