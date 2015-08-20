# -*- coding: utf-8 -*-
"""Installer for the d11.hermes package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='d11.hermes',
    version='0.1',
    description="Um portal onde autores encontram revistas científicas para suas publicações.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.6",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Davi Lima',
    author_email='davilima6@gmail.com',
    url='http://pypi.python.org/pypi/d11.hermes',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['d11'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cs.auth.facebook',
        'collective.cover',
        'collective.favorites',
        'eea.facetednavigation',
        'plone.api',
        'plone.app.contenttypes',
        'plone.app.multilingual',
        'setuptools',
        'z3c.jbot',
        'Products.ATVocabularyManager',
        'Products.PloneFormGen'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
