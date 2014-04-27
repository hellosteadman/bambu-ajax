from django.conf.urls import patterns, url
from bambu_ajax import autodiscover
from bambu_ajax.views import utility, endpoint

autodiscover()
urlpatterns = patterns('',
	url(r'^util\.js$', utility, name = 'ajax_utility'),
	url(r'^endpoint\.js$', endpoint, name = 'ajax_endpoint'),
)
