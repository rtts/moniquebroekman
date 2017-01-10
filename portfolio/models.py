from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from numberedmodel.models import NumberedModel

class Category(NumberedModel):
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

class Project(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    created = models.DateTimeField('aangemaakt', auto_now_add=True)
    modified = models.DateTimeField('gewijzigd', auto_now=True)
    project_title = models.CharField('titel', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    image = models.ImageField('afbeelding', blank=True)
    summary = models.TextField('samenvatting', blank=True)
    frontpage_summary = RichTextField('samenvatting (oude stijl)')
    article_content = RichTextField('inhoud (oude stijl)')
    def __str__(self):
        return self.project_title
    class Meta:
        ordering = ['position']
        verbose_name_plural = 'projecten'

class Element(NumberedModel):
    project = models.ForeignKey('Project')
    TYPES = (
        ('text', 'Tekst element (geeft alleen tekst weer)'),
        ('photo', 'Foto element (geeft de afbeelding en evt. tekst weer)'),
        ('video', 'Video element (geeft een video weer)'),
    )
    position = models.PositiveIntegerField('positie', blank=True)
    type = models.CharField(max_length=16, choices=TYPES)
    image = models.ImageField('afbeelding', blank=True)
    video = EmbedVideoField(help_text="Plak hier een YouTube of Vimeo link", blank=True)
    text = RichTextField('tekst', blank=True)

    def __str__(self):
        return '{} element'.format(self.get_type_display())

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'elementen'
