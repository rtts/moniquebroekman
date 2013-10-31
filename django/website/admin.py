from django.contrib import admin
from adminsortable.admin import SortableAdmin
from website.models import Page

class WebsitePageAdmin(SortableAdmin):
    prepopulated_fields = {"short_name": ("page_title",)}
    list_display = ('visible_in_menu', 'short_name', 'page_title')
    list_display_links = ('page_title',)

admin.site.register(Page, WebsitePageAdmin)

# hide the following from admin:

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
