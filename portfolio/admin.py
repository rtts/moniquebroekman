from django.db import models
from django.contrib import admin
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.forms import CheckboxSelectMultiple
from portfolio.models import Category, Project

def frontpage_summary(project):
    return strip_tags(project.frontpage_summary)

def projects(category):
    return ', '.join(category.projects.values_list('short_name', flat=True))

def category(project):
    return ', '.join(project.categories.values_list('category_name', flat=True))

class PortfolioCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {"short_name": ["category_name"]}
    list_display = ['position', 'visible_in_menu', 'visible_on_homepage', 'short_name', 'category_name', projects]
    list_display_links = ['category_name']

class PortfolioProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {"short_name": ["project_title"]}
    list_display = ['position', 'created', 'show_url', 'project_title', frontpage_summary, category]
    list_display_links = ['project_title']
    list_filter = ['categories']

    def show_url(self, obj):
        return mark_safe('<a href="/project/{}" target="_blank">{}</a>'.format(obj.short_name, obj.short_name))
    show_url.short_description = 'verkorte naam'

admin.site.register(Category, PortfolioCategoryAdmin)
admin.site.register(Project, PortfolioProjectAdmin)
