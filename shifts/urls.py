from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add/',add, name='add'),
    path('<slug:slug>/', show_profile, name='show-profile')
]
