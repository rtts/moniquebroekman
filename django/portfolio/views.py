from django.http import Http404
from django.shortcuts import render, get_object_or_404
from portfolio.models import Project, Page

def index(request):
    projects = Project.objects.all()
    pages = Page.objects.all()
    return render(request, 'portfolio/index.html', {
            'pages': pages,
            'projects': projects
            })

def project(request, name):
    pages = Page.objects.all()
    project = get_object_or_404(Project, short_name=name)
    return render(request, 'portfolio/project.html', {
            'pages': pages,
            'project': project
            })

def page(request, name):
    pages = Page.objects.all()
    page = get_object_or_404(Page, short_name=name)
    return render(request, 'portfolio/page.html', {
            'pages': pages,
            'page': page
            })
