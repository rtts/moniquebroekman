from django.contrib import admin
from django.utils.html import strip_tags
from adminsortable.admin import SortableAdmin
from portfolio.models import Category, Project

def frontpage_summary(project):
    return strip_tags(project.frontpage_summary)

def projects(category):
    return ', '.join(category.projects.values_list('short_name', flat=True))

def category(project):
    return ', '.join(project.categories.values_list('category_name', flat=True))

class PortfolioCategoryAdmin(SortableAdmin):
    prepopulated_fields = {"short_name": ("category_name",)}
    list_display = ('visible_in_menu', 'short_name', 'category_name', projects)
    list_display_links = ('category_name',)

class PortfolioProjectAdmin(SortableAdmin):
    prepopulated_fields = {"short_name": ("project_title",)}
    list_display = ('created', 'short_name', 'project_title', frontpage_summary, category)
    list_display_links = ('project_title',)
    list_filter = ('categories',)
    ordering = ['-order']

admin.site.register(Category, PortfolioCategoryAdmin)
admin.site.register(Project, PortfolioProjectAdmin)
