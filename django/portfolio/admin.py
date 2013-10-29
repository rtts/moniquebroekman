from django.contrib import admin
from adminsortable.admin import SortableAdmin
from portfolio.models import Portfolio, Project, Page

admin.site.register(Portfolio, SortableAdmin)
admin.site.register(Project, SortableAdmin)
admin.site.register(Page, SortableAdmin)
