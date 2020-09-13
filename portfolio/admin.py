from django.db import models
from django.contrib import admin
from django.utils.html import strip_tags
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.forms import CheckboxSelectMultiple
from portfolio.models import *

def frontpage_summary(project):
    return strip_tags(project.frontpage_summary)

def projects(category):
    return ', '.join(category.projects.values_list('short_name', flat=True))

def category(project):
    return ', '.join(project.categories.values_list('category_name', flat=True))
category.short_description = 'categoriën'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {"short_name": ["category_name"]}
    list_display = ['visible_in_menu', 'visible_on_homepage', 'short_name', 'category_name', projects]
    list_display_links = ['category_name']

class InlineElementAdmin(admin.StackedInline):
    model = Element
    extra = 0
    min_num = 1
    fields = ['position', 'type', 'edit_link', 'video', 'text']
    readonly_fields = ['edit_link']

    def edit_link(self, instance):
        url = reverse('admin:{}_{}_change'.format(instance._meta.app_label, instance._meta.model_name), args=[instance.pk])

        if instance.pk:
            html = ''.join(['&bull; {}<br>'.format(p.image) for p in instance.photos.all()] + \
                           ['<a href="{}">Voeg foto’s toe</a>'.format(url)])
            return mark_safe(html)
        else:
            return '(sla dit element eerst op)'
    edit_link.short_description = 'Foto’s'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    prepopulated_fields = {"short_name": ["project_title"]}
    exclude = ['frontpage_summary']
    list_display = ['project_title', 'created', 'show_url', category]
    list_display_links = ['project_title']
    list_filter = ['categories']
    inlines = [InlineElementAdmin]

    def show_url(self, obj):
        return mark_safe('<a href="/project/{}" target="_blank">{}</a>'.format(obj.short_name, obj.short_name))
    show_url.short_description = 'verkorte naam'

class InlinePhotoAdmin(admin.TabularInline):
    model = Photo
    extra = 0
    min_num = 1

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if '_save' in request.POST:
            return redirect('admin:portfolio_project_change', obj.project.pk)
        else:
            return super(ElementAdmin, self).response_change(request, obj)

    # Hide this admin from the admin index
    def get_model_perms(self, request):
        return {}
    def has_add_permission(self, request):
        return False

    exclude = ['project', 'position', 'type', 'video', 'text']
    inlines = [InlinePhotoAdmin]
