from django.http import Http404
from django.shortcuts import render
from portfolio.models import Project, Page

def index(request):
    projects = Project.objects.order_by('position')
    pages = Page.objects.order_by('position')
    return render(request, 'portfolio/index.html', {
            'pages': pages,
            'projects': projects
            })

def project(request, name):
    pages = Page.objects.order_by('position')
    try:
        project = Project.objects.get(short_name=name)
    except project.DoesNotExist:
        raise Http404
    return render(request, 'portfolio/project.html', {
            'pages': pages,
            'project': project
            })

def page(request, name):
    pages = Page.objects.order_by('position')
    try:
        page = Page.objects.get(short_name=name)
    except page.DoesNotExist:
        raise Http404
    return render(request, 'portfolio/page.html', {
            'pages': pages,
            'page': page
            })
