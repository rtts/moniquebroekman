from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import website.views
import portfolio.views

urlpatterns = [
    url(r'^$', portfolio.views.index),
    url(r'^info/', include('website.urls')),
    url(r'^project/', include('portfolio.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Monique Broekman Beheer'
admin.site.site_header = 'Monique Broekman Beheer'
admin.site.site_url = None
admin.site.index_title = 'Overzicht'
admin.site.unregister(User)
admin.site.unregister(Group)
