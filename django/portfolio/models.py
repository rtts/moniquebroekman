from django.db import models
from ckeditor.fields import RichTextField
from adminsortable.models import Sortable

class Category(Sortable):
    category_name = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    visible_in_menu = models.BooleanField(default=True)
    projects = models.ManyToManyField("Project", related_name="categories")
    def __unicode__(self):
        return self.category_name
    class Meta(Sortable.Meta):
        verbose_name_plural = "categories"
        pass

class Project(Sortable):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    project_title = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    frontpage_summary = RichTextField()
    article_content = RichTextField()
    def __unicode__(self):
        return self.project_title
    class Meta(Sortable.Meta):
        pass
