from django.core import paginator
from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def list_news(request):

    news = News.objects.all()

    page = request.GET.get('page',1)

    paginator = Paginator(news, 10)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/list_news.html', {'news':news})

def news_detail(request, slug):

    news = News.objects.get(slug=slug)

    return render(request, 'news/news_detail.html', {'news':news})