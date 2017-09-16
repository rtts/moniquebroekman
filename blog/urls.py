from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^([^/]+)/$', views.post, name='blog_post'),
#    url(r'^(.*)/$', views.archive, name='blog_archive'),
]
