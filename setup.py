#!/usr/bin/env python

PROJ_NAME = 'romkan'
PACKAGE_NAME = 'romkan'

PROJ_METADATA = '%s.json' % PROJ_NAME

import os, json, imp, sys

here = os.path.abspath(os.path.dirname(__file__))
proj_info = json.loads(open(os.path.join(here, PROJ_METADATA)).read())
README = open(os.path.join(here, 'README.rst')).read()
CHANGELOG = open(os.path.join(here, 'CHANGELOG.rst')).read()
VERSION = imp.load_source('version', os.path.join(here, 'src/%s/version.py' % PACKAGE_NAME)).__version__

PY2 = sys.version_info[0] <= 2
deps = ['unicodecsv'] if PY2 else []

from setuptools import setup, find_packages
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
    
    packages = find_packages('src'),
    package_dir = {'' : 'src'},
    
    test_suite = 'tests',
    install_requires = deps,
    
    platforms = 'any',
    zip_safe = False,
    include_package_data = True,
    
    classifiers = proj_info['classifiers'],
)
