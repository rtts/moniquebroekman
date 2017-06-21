from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from numberedmodel.models import NumberedModel

class Blog(models.Model):
    title = models.CharField('titel', max_length=255)
    slug = models.SlugField('URL', unique=True)
    date = models.DateField('datum', default=datetime.now)
    text = RichTextField('tekst', blank=True)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)

class Photo(NumberedModel):
    element = models.ForeignKey('Blog', related_name='photos')
    position = models.PositiveIntegerField('positie', blank=True)
    image = models.ImageField('afbeelding', blank=True)

    class Meta:
        ordering = ['position']
        verbose_name = 'afbeelding'
        verbose_name_plural = 'afbeeldingen'
