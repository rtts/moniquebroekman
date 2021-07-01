from django.db import models
from ckeditor.fields import RichTextField
from cms.mixins import Numbered

class Page(Numbered, models.Model):
    position = models.PositiveIntegerField('positie', blank=True)
    page_title = models.CharField('titel', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    visible_in_menu = models.BooleanField('zichtbaar in het menu', default=True)
    page_content = RichTextField('inhoud')
    def __str__(self):
        return self.page_title
    class Meta:
        ordering = ['position']
        verbose_name = 'pagina'
        verbose_name_plural = 'pagina’s'
