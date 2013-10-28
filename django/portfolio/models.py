from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    position = models.IntegerField()
    shortname = models.SlugField()
    title = models.CharField(max_length=255)
    summary_pic = models.ImageField(upload_to='summary_pics')
    summary_text = RichTextField()
    content = RichTextField()
    def __unicode__(self):
        return self.title

class Page(models.Model):
    position = models.IntegerField()
    shortname = models.SlugField()
    title = models.CharField(max_length=255)
    content = RichTextField()
    def __unicode__(self):
        return self.title
