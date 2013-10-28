from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^ckeditor/', include('ckeditor.urls')),
    # url(r'^$', 'mbcms.views.home', name='home'),
    # url(r'^mbcms/', include('mbcms.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
