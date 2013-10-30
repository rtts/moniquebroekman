from django.contrib import admin
from adminsortable.admin import SortableAdmin
from portfolio.models import Category, Project

class PortfolioCategoryAdmin(SortableAdmin):
    prepopulated_fields = {"short_name": ("category_name",)}

class PortfolioProjectAdmin(SortableAdmin):
    prepopulated_fields = {"short_name": ("project_title",)}

admin.site.register(Category, PortfolioCategoryAdmin)
admin.site.register(Project, PortfolioProjectAdmin)
