from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^overzicht/alles/$', views.index, name='all'),
    url(r'^overzicht/([^/]+)/$', views.index, name='category'),
    url(r'^_/(.*)/$', views.project_backdoor),
    url(r'^(.*)/$', views.project, name='project'),
]
