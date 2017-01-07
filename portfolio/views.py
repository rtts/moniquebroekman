from django.http import Http404
from django.shortcuts import render, get_object_or_404
from website.models import Page
from portfolio.models import Category, Project

def homepage(request):
    '''
    Serves the homepage, a list of categories
    '''
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'portfolio/homepage.html', {
            'pages': pages,
            'categories': categories
    })

def index(request, category=''):
    '''
    Serves a list of projects, narrowed down by category if supplied
    '''
    if category:
        current_category = get_object_or_404(Category, short_name=category)
        projects = current_category.projects.all()
    else:
        current_category = None
        projects = Project.objects.all()
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'portfolio/index.html', {
        'current_category': current_category,
        'pages': pages,
        'projects': projects,
        'categories': categories
    })

def project(request, name):
    '''
    Serves a project page
    '''
    project = get_object_or_404(Project, short_name=name)
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'portfolio/project.html', {
            'pages': pages,
            'project': project,
            'categories': categories
            })

def project_backdoor(request, name):
    '''
    Serves a project page in an anonymous template
    '''
    project = get_object_or_404(Project, short_name=name)
    return render(request, 'portfolio/project_backdoor.html', {
            'project': project,
            })
