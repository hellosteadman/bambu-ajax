#!/usr/bin/env python
from distutils.core import setup
from os import path

setup(
	name = 'bambu-ajax',
	version = '1.0',
	description = 'AJAX utility functions for Django',
	author = 'Steadman',
	author_email = 'mark@steadman.io',
	url = 'https://github.com/iamsteadman/bambu-ajax',
	namespace_packages = ['bambu'],
	long_description = open(path.join(path.dirname(__file__), 'README')).read(),
	packages = [
		'bambu.ajax',
		'bambu.ajax.templatetags',
		'bambu.ajax.test'
	],
	package_data = {
		'bambu.ajax': [
			'templates/ajax/utils.js',
			'templates/blog/*.html',
			'templates/search/indexes/blog/*.txt',
			'static/blog/*.js'
		]
	},
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django'
	]
)
