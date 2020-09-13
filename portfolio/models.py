from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from cms.models import Numbered

class Category(Numbered, models.Model):
    position = models.PositiveIntegerField('positie', blank=True)
    category_name = models.CharField('naam van deze categorie', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    visible_in_menu = models.BooleanField('zichtbaar in het menu', default=True)
    visible_on_homepage = models.BooleanField('zichtbaar op de homepage', default=True)
    image = models.ImageField('afbeelding', blank=True)
    projects = models.ManyToManyField("Project", verbose_name='projecten', blank=True, related_name="categories")
    def __str__(self):
        return self.category_name
    class Meta:
        ordering = ['position']
        verbose_name = 'categorie'
        verbose_name_plural = 'categorieën'

class Project(Numbered, models.Model):
    position = models.PositiveIntegerField('positie', blank=True)
    created = models.DateTimeField('aangemaakt', auto_now_add=True)
    modified = models.DateTimeField('gewijzigd', auto_now=True)
    project_title = models.CharField('titel', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    image = models.ImageField('afbeelding', blank=True)
    summary = models.TextField('samenvatting', blank=True)
    frontpage_summary = RichTextField('samenvatting (oude stijl)', blank=True)
    article_content = RichTextField('inhoud (oude stijl)', help_text='Probeer deze editor niet meer te gebruiken! Voeg in plaats daarvan foto-, video- of tekstelementen hieronder toe.', blank=True)
    def __str__(self):
        return self.project_title
    class Meta:
        ordering = ['position']
        verbose_name_plural = 'projecten'

class Element(Numbered, models.Model):
    TYPES = (
        ('text', 'Tekst element (geeft alleen tekst weer)'),
        ('photo', 'Foto element (geeft foto’s weer)'),
        ('video', 'Video element (geeft een video weer)'),
    )
    project = models.ForeignKey('Project', related_name='elements', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('positie', blank=True)
    type = models.CharField(max_length=16, choices=TYPES)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)
    text = RichTextField('tekst', blank=True)

    def __str__(self):
        return self.get_type_display().split('(')[0]

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'elementen'

class Photo(Numbered, models.Model):
    element = models.ForeignKey('Element', related_name='photos', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('positie', blank=True)
    image = models.ImageField('afbeelding', blank=True)

    class Meta:
        ordering = ['position']
        verbose_name = 'afbeelding'
        verbose_name_plural = 'afbeeldingen'
