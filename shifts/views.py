from django.shortcuts import render, redirect
from .models import Shift
from .forms import ShiftForm
# Create your views here.

def index(request):
    shifts = Shift.objects.all()
    return render(request,'shifts/index.html',{'shifts':shifts,'nbar':'shift-list'})

def add(request):
    form = ShiftForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        print(request.POST)
        form.save()

        return redirect('shift:index')
    
    return render(request, 'shifts/add.html', {'form':form})
