from django.http import Http404
from django.shortcuts import render, get_object_or_404
from website.models import Page
from portfolio.models import Category, Project

def index(request, category=''):
    '''
    Serves a list of projects, narrowed down by category if supplied
    '''
    if category:
        cat = get_object_or_404(Category, short_name=category)
        projects = cat.projects.all()
    else:
        projects = Project.objects.all()
    pages = Page.objects.filter(visible_in_menu=True)
    categories = Category.objects.filter(visible_in_menu=True)
    return render(request, 'portfolio/index.html', {
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
