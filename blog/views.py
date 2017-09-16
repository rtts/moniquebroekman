from django.shortcuts import render, get_object_or_404
from .models import *
from portfolio.models import Category
from website.models import Page

def index(request):
    try:
        oldblog = Page.objects.get(short_name='blog')
    except Page.DoesNotExist:
        oldblog = None
    blogs = Blog.objects.all()
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'blog.html', {
        'oldblog': oldblog,
        'blogs': blogs,
        'pages': pages,
        'categories': categories,
    })

def post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'blogpost.html', {
        'blog': blog,
        'pages': pages,
        'categories': categories,
    })
