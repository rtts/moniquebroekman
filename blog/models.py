from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from numberedmodel.models import NumberedModel

class Blog(models.Model):
    title = models.CharField('titel', max_length=255)
    slug = models.SlugField('URL', unique=True)
    date = models.DateField('datum', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Section(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    text = RichTextField('tekst', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    caption = models.CharField('bijschrift', max_length=255, blank=True)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)
    blog = models.ForeignKey('Blog', related_name='sections')

    def number_with_respect_to(self):
        return self.blog.sections.all()

    def __str__(self):
        return '#' + str(self.position)

    class Meta:
        ordering = ['position']
        verbose_name = 'Sectie'
