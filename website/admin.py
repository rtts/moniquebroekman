from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from website.models import Page

@admin.register(Page)
class WebsitePageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {'short_name': ['page_title']}
    list_display = ['position', 'visible_in_menu', 'short_name', 'page_title']
    list_display_links = ['page_title']
