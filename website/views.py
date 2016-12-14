from django.http import Http404
from django.shortcuts import render, get_object_or_404
from website.models import Page
from portfolio.models import Category, Project

def page(request, name):
    page = get_object_or_404(Page, short_name=name)
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'website/page.html', {
            'pages': pages,
            'page': page,
            'categories': categories
            })
