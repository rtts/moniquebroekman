from datetime import datetime
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from cms.models import Numbered

class Blog(models.Model):
    title = models.CharField('titel', max_length=255)
    slug = models.SlugField('URL', unique=True)
    date = models.DateField('datum', default=datetime.now)

    def get_absolute_url(self):
        return reverse('blog_post', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Section(Numbered, models.Model):
    position = models.PositiveIntegerField('positie', blank=True)
    text = RichTextField('tekst', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    caption = models.CharField('bijschrift', max_length=255, blank=True)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)
    blog = models.ForeignKey('Blog', related_name='sections', on_delete=models.CASCADE)
    html = models.TextField('HTML', help_text='Plak hier de broncode van een volledig HTML document.', blank=True)

    def number_with_respect_to(self):
        return self.blog.sections.all()

    def __str__(self):
        return '#' + str(self.position)

    class Meta:
        ordering = ['position']
        verbose_name = 'Sectie'
