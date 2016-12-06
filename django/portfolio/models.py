from django.db import models
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel

class Category(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    category_name = models.CharField('naam van deze categorie', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    visible_in_menu = models.BooleanField('zichtbaar in het menu', default=True)
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
    project_title = models.CharField('titel van het project', max_length=255)
    short_name = models.SlugField('verkorte naam', help_text='deze naam wordt gebruikt in de URL', unique=True)
    frontpage_summary = RichTextField('samenvatting')
    article_content = RichTextField('inhoud')
    def __str__(self):
        return self.project_title
    class Meta:
        ordering = ['position']
        verbose_name_plural = 'projecten'
