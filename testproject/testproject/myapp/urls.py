from django.conf.urls import patterns, url

urlpatterns = patterns('testproject.myapp.views',
    url(r'^', 'home')
)