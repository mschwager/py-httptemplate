#!/usr/bin/env python3

from setuptools import setup

import codecs
import os

PACKAGE_DIRECTORY = 'src'
PACKAGE_NAME = 'httptemplate'

here = os.path.abspath(os.path.dirname(__file__))
about_filename = os.path.join(
    here,
    PACKAGE_DIRECTORY,
    PACKAGE_NAME,
    '__version__.py',
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
    package_dir={'': PACKAGE_DIRECTORY},
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        "aiodns==1.1.1",
        "aiohttp==2.3.7",
        "aiohttp-jinja2==0.14.0",
        "cchardet==2.1.1",
    ],
)
