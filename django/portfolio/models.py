from django.db import models
from ckeditor.fields import RichTextField
from adminsortable.models import Sortable

class Portfolio(Sortable):
    short_name = models.SlugField()
    portfolio_name = models.CharField(max_length=255)
    projects = models.ManyToManyField("Project", related_name="portfolios")
    def __unicode__(self):
        return self.portfolio_name
    class Meta(Sortable.Meta):
        pass

class Project(Sortable):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    short_name = models.SlugField()
    project_title = models.CharField(max_length=255)
    frontpage_summary = RichTextField()
    article_content = RichTextField()
    def __unicode__(self):
        return self.project_title
    class Meta(Sortable.Meta):
        pass

class Page(Sortable):
    short_name = models.SlugField()
    page_title = models.CharField(max_length=255)
    page_content = RichTextField()
    def __unicode__(self):
        return self.page_title
    class Meta(Sortable.Meta):
        pass
