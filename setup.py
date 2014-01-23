#!/usr/bin/env python

import os, json, imp
from setuptools import setup, find_packages

PROJ_NAME = 'romkan'
PACKAGE_NAME = 'romkan'
PROJ_METADATA = '%s.json' % PROJ_NAME

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGELOG = open(os.path.join(HERE, 'CHANGELOG.rst')).read()
VERSION = imp.load_source('version', os.path.join(HERE, 'src/%s/version.py' % PACKAGE_NAME)).__version__
SRC = os.path.join(HERE, 'src')


proj_info = json.loads(open(os.path.join(HERE, PROJ_METADATA)).read())
test_requirements = ['ddt>=0.5.0', 'unicodecsv>=0.10.1']


setup(
    name = proj_info['name'],
    version = VERSION,
    
    author = proj_info['author'],
    author_email = proj_info['author_email'],
    url = proj_info['url'],
    license = proj_info['license'],
    
    description = proj_info['description'],
    keywords = proj_info['keywords'],
    
    long_description = README + '\n\n' + CHANGELOG,
    
    packages = find_packages(SRC),
    package_dir = {'' : SRC},
    
    test_suite = 'tests',
    tests_require = test_requirements,
    dependency_links = ['https://github.com/jdunck/python-unicodecsv/zipball/master#egg=unicodecsv-0.10.1'],
    
    platforms = 'any',
    zip_safe = False,
    include_package_data = True,
    
    classifiers = proj_info['classifiers'],
)
