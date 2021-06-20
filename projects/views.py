from django.core import paginator
from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):

    projects = Project.objects.all()

    page = request.GET.get('page',1)

    paginator = Paginator(projects, 10)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'projects/index.html', {'projects':projects,'nbar':'project-list'})


def detail(request, slug):

    project = Project.objects.get(slug=slug)

    return render(request, 'projects/detail.html', {'project':project})