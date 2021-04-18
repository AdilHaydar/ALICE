from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponse
import mimetypes
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    context = {
        'nbar' : 'main-page'
    }
    return render(request,'base/base.html',context)

def list_articles(request):
    articles = Article.objects.all()

    #page = request.GET.get('page',1)
    p = Paginator(articles,5)
    articles = p.page(1)

    context = {
        'articles':articles,
        'nbar' : 'list-articles',
        'num_pages':p.num_pages,
    }
    return render(request,'Article/list_articles.html',context)

def load_more(request):
    data = {'success':True}

    articles = Article.objects.all()
    p = Paginator(articles,5)
    page = request.GET.get('page',1)

    try:
        articles = p.page(page)
    except PageNotAnInteger:
        articles = p.page(1)
    except EmptyPage:
        articles = p.page(p.num_pages)

    articles_html = render_to_string('Article/partial/partial-list.html',{'articles':articles})
    data.update({
        'articles_html':articles_html,
    })

    return JsonResponse(data=data,status=200)

def detail(request,slug):
    article = Article.objects.get(slug=slug)
    article.view_count = F('view_count') + 1
    article.save()
    article.refresh_from_db()

    return render(request,'Article/detail.html',{'article':article})

@login_required(login_url='user:login')
def add(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.user = request.user
        article.save()

        return redirect('article:detail',article.slug)

    context = {
        'nbar' : 'add-article',
        'form' : form
    }
    return render(request,'Article/add_article.html',context)

def show_pdf(request, slug):
    article = Article.objects.get(slug=slug)
    fl_path = article.file.path
    filename = article.file.name

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response