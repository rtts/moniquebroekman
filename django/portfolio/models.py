from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    position = models.IntegerField()
    short_name = models.SlugField()
    project_title = models.CharField(max_length=255)
    frontpage_summary = RichTextField()
    article_content = RichTextField()
    def __unicode__(self):
        return self.project_title
    class Meta:
        ordering = ["position"]

class Page(models.Model):
    position = models.IntegerField()
    short_name = models.SlugField()
    page_title = models.CharField(max_length=255)
    page_content = RichTextField()
    def __unicode__(self):
        return self.page_title
    class Meta:
        ordering = ["position"]
