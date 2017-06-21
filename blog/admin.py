from django.contrib import admin
from .models import *

class InlinePhotoAdmin(admin.TabularInline):
    model = Photo
    extra = 0
    min_num = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {'slug': ('title',), }
    inlines = [InlinePhotoAdmin]
