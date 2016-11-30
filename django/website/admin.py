from django.contrib import admin
from website.models import Page

@admin.register(Page)
class WebsitePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"short_name": ("page_title",)}
    list_display = ('visible_in_menu', 'short_name', 'page_title')
    list_display_links = ('page_title',)
