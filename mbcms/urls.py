from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import website.views
import portfolio.views

urlpatterns = staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('info/', include('website.urls')),
    path('project/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('', portfolio.views.homepage),
]

admin.site.site_title = 'Monique Broekman Beheer'
admin.site.site_header = 'Monique Broekman Beheer'
admin.site.site_url = None
admin.site.index_title = 'Overzicht'
admin.site.enable_nav_sidebar = False
#admin.site.unregister(User)
admin.site.unregister(Group)
