from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/',views.list, name='list'),
    path('show/<str:slug>/',views.show,name='show'),
    path('create-category/',views.create_category, name='create-category'),
    path('get-categories-ajax/',views.get_categories,name='get-categories-ajax'),
]