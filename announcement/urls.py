from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.list_announcement,name = "list-announcement"),
    path('add/',views.add_announcement,name='add-announcement')
]