#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
	name = 'bambu-ajax',
	version = '2.0',
	description = 'AJAX utility functions for Django',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-ajax',
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	packages = [
		'bambu_ajax',
		'bambu_ajax.templatetags',
		'bambu_ajax.test'
	],
	package_data = {
		'bambu_ajax': [
			'templates/ajax/utils.js',
			'templates/blog/*.html',
			'templates/search/indexes/blog/*.txt',
			'static/blog/*.js'
		]
	},
	install_requires = [
        'Django>=1.4'
    ],
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)