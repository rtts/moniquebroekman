from django.db import models
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel

class Page(NumberedModel):
    position = models.PositiveIntegerField(blank=True)
    page_title = models.CharField(max_length=255)
    short_name = models.SlugField(unique=True)
    visible_in_menu = models.BooleanField(default=True)
    page_content = RichTextField()
    def __str__(self):
        return self.page_title
    class Meta:
        ordering = ['position']
        pass
