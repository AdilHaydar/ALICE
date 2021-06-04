  
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login_user,name = "login"),
    path('logout/',views.logout_user,name = "logout"),
    path('register/', views.register, name="register"),
    path('check-username/<str:username>/', views.check_username,name='check-username'),
]