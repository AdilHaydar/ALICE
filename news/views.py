from django.shortcuts import render
from .models import News
# Create your views here.

def list_news(request):

    news = News.objects.all()

    return render(request, 'news/list_news.html', {'news':news})

def news_detail(request, slug):

    news = News.objects.get(slug=slug)

    return render(request, 'news/news_detail.html', {'news':news})