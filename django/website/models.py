from django.db import models
from ckeditor.fields import RichTextField
from adminsortable.models import Sortable

class Page(Sortable):
    page_title = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    visible_in_menu = models.BooleanField(default=True)
    page_content = RichTextField()
    def __unicode__(self):
        return self.page_title
    class Meta(Sortable.Meta):
        pass
