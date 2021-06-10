from django.shortcuts import render, redirect
from .models import Image, GalleryHeader

def index(request):

    headers = GalleryHeader.objects.prefetch_related('galleries').all()

    return render(request, 'gallery/index.html', {'headers':headers})




