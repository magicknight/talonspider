#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='talonspider',
    version='0.0.7',
    author='Howie Hu',
    description="A simple,lightweight scraping micro-framework",
    author_email='xiaozizayang@gmail.com',
    install_requires=['lxml', 'requests', 'cchardet', 'cssselect'],
    url="https://github.com/howie6879/talonspider/blob/master/README.md",
    packages=find_packages(),
    package_data={'talonspider': ['utils/*.txt']})
