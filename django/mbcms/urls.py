from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
import portfolio.views

urlpatterns = patterns('',
    url(r'^$', portfolio.views.index),
    url(r'^projects/', include('portfolio.urls')),
    url(r'^editor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(.*)/', portfolio.views.page),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
