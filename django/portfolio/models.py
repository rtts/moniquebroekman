from django.db import models
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel

class Category(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    category_name = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    visible_in_menu = models.BooleanField(default=True)
    projects = models.ManyToManyField("Project", blank=True, related_name="categories")
    def __str__(self):
        return self.category_name
    class Meta:
        #ordering = ['position']
        verbose_name = 'categorie'
        verbose_name_plural = 'categorieën'

class Project(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    project_title = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    frontpage_summary = RichTextField()
    article_content = RichTextField()
    def __str__(self):
        return self.project_title
    class Meta:
        ordering = ['-position']
        verbose_name_plural = 'projecten'
