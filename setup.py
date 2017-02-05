"""A Python module for reading data from Tektronix oscilloscopes.

Website:
https://github.com/henne-s/tek-tools
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tek-tools',
    version='1.0.0',
    description='Read data from Tektronix oscilloscopes',
    long_description=long_description,
    url='https://github.com/henne-s/tek-tools',
    author='Hendrik Soehnholz',
    author_email='henne-s@gmx.de',
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='tektronix oscilloscope data',

    packages=[
        'tek_tools',
        ],

    install_requires=[
        'numpy',
        ],

    # $ pip install -e .[test]
    extras_require={
        'test': ['matplotlib'],
    },

)
