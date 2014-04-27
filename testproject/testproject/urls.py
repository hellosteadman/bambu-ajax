from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^ajax/', include('bambu_ajax.urls')),
    url(r'^', include('testproject.myapp.urls')),
)