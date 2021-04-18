"""CERN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user/',include(("users.urls",'users'),namespace='user')),
    path('article/',include(('articles.urls','articles'), namespace='article')),
    path('announcement/',include(('announcement.urls','announcement'),namespace='announcement')),
    path('meeting/',include(('meeting_reports.urls','meeting_reports'), namespace='meeting-reports')),
    path('shift/',include(('shifts.urls','shifts'), namespace='shift'))
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)