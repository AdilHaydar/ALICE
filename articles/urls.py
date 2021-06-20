
from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:slug>',views.detail,name = "detail"),
    path('add',views.add,name='add'),
    path('show-pdf/<slug:slug>',views.show_pdf,name='show-pdf'),
    path('list-articles/',views.list_articles,name='list'),
    path('load-more/',views.load_more,name='load-more'),
]