from django.core import paginator
from django.shortcuts import render
from .models import Document
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):

    documents = Document.objects.all()

    page = request.GET.get('page', 10)

    paginator = Paginator(documents, 10)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)

    return render(request, 'documents/index.html', {'documents':documents,'nbar':'document-list'})


def detail(request, slug):

    document = Document.objects.get(slug=slug)

    return render(request, 'documents/detail.html', {'document':document})
    
