#! /usr/bin/python
from setuptools import setup, find_packages

import os

_HERE = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

#try:
#    import pypandoc
#    long_description = pypandoc.convert('README.md', 'rst')
    
#except(IOError, ImportError):
#    long_description = open('README.md').read()




with open(os.path.join(_HERE, 'README.rst'),'r+') as fh:
    long_description = fh.read()

setup(
    name = "statcamp",
    version = "0.0.2",
    description = "stat funcs from datacamp stat thinking",
    long_description = long_description,
    author = "Shichao(Richard) Ji",
    author_email = "jshichao@vt.edu",
    url = "https://github.com/shichaoji/statcamp",
    download_url = "https://github.com/shichaoji/statcamp/archive/0.1.tar.gz",
    keywords = ['data science','data mining','text mining','statistics'],
    license = 'MIT', 
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        ],
    packages = find_packages(),
    install_requires=[
        'numpy',
      ],
   # entry_points={
   #     'console_scripts': ['dsutils=dsutils:main'],
   #   },
#    cmdclass={'install': Install},
)

#import sys
#if 'install' in sys.argv:
#    print 'download nltk stopwords'
#    import nltk
#    nltk.download("stopwords")
