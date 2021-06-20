from main.decorators import authorized_user
from django.shortcuts import render, redirect
from .models import Shift, ShiftProfile, AuthorityTitle, AcademicTitle
from .forms import ShiftForm
from main.decorators import authorized_user
# Create your views here.

def index(request):
    #shifts = Shift.objects.all()
    shifts = Shift.objects.get_shifts_without_authority()
    authority_title = AuthorityTitle.objects.prefetch_related('shifts').all()
    return render(request,'shifts/index.html',{'shifts':shifts,'authority_title':authority_title,'nbar':'shift-list'})

@authorized_user
def add(request):
    form = ShiftForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        print(request.POST)
        form.save()

        return redirect('shift:index')
    
    return render(request, 'shifts/add.html', {'form':form})

def show_profile(request, slug):
    acc = ShiftProfile.objects.get(slug=slug)

    return render(request, 'shifts/profile.html', {'acc':acc})
