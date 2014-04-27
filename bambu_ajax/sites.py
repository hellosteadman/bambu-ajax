from django.utils.datastructures import SortedDict
from django.http import HttpResponseRedirect
from django.utils.decorators import available_attrs
from functools import wraps

class AlreadyRegistered(Exception):
	pass

class NotRegistered(Exception):
	pass

class DoesNotExist(Exception):
	pass

class AjaxSite(object):
	_registry = {}

	def register(self, view):
		mod = []

		if view.__module__.startswith('bambu_ajax.test.'):
			key = 'bambu_ajax.test.%s' % view.__name__
		else:
			for part in view.__module__.split('.'):
				if part == 'ajax':
					break

				mod.append(part)
			key = '%s.%s' % ('.'.join(mod), view.__name__)

		self._registry[key] = view
		return view
