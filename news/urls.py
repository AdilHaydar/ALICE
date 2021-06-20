from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_news, name='list-news'),
    path('<slug:slug>', views.news_detail, name='news-detail'),
]
