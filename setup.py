#!/usr/bin/env python

from setuptools import setup

setup(name='git rewrite author',
      version='1.0',
      description='Rewrite author/committer history of a git repository',
      author='David Fokkema',
      author_email='davidfokkema@icloud.com',
      url='https://github.com/davidfokkema/git-rewrite-author',
      classifiers=['Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Version Control',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      scripts=['git-rewrite-author'])
