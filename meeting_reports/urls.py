from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('detail/<int:id>',views.detail, name='detail'),
    path('add-category/',views.add_change_delete_category, name="add-category"),
    path('update-category/<int:pk>',views.update_category, name='update-category'),
    path('meeting-list/',views.meeting_list, name='meeting-list'),
    path('meeting-list/add',views.add_meeting_list, name='add-meeting-list'),
    path('meeting-detail/<int:pk>',views.meeting_detail, name='meeting-detail'),
]