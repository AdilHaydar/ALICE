from django.shortcuts import render
from .models import SSS
# Create your views here.


def index(request):

    sss = SSS.objects.all()

    return render(request, 'sss/index.html', {'sss':sss,'nbar':'sss'})