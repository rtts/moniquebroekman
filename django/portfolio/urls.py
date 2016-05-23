from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^overzicht/([^/]+)/$', views.index, name='category'),
    url(r'^_/(.*)/$', views.project_backdoor),
    url(r'^(.*)/$', views.project, name='project'),
)
