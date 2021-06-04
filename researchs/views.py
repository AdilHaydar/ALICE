from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Research, CategoryResearch
from .forms import ResearchForm, CategoryResearchForm
from main.decorators import authorized_user
from django.core import serializers
# Create your views here.

@authorized_user
def create(request):
    form = ResearchForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()

        return redirect('research:list')

    return render(request, 'research/create.html', {'form':form})

def list(request):
    categories = CategoryResearch.objects.prefetch_related('researchs').all()

    context = {
        'categories':categories,
        'nbar':'research-list',
    }

    return render(request, 'research/list.html',context)

def show(request, slug):
    research = get_object_or_404(Research ,slug=slug)

    return render(request, 'research/show.html',{'research':research})

def create_category(request):
    form = CategoryResearchForm(request.POST or None)

    if form.is_valid():
        form.save()


    return render(request, 'research/create-category.html', {'form':form})

def get_categories(request):
    data = serializers.serialize('json', CategoryResearch.objects.all())

    #return JsonResponse(data=data, status=200, safe=False) 
    # * Bu işlemi JsonResponse ile yapmak istersem safe=False parametresini eklemem gerekiyor ama HttpResponse ile aşağıdaki gibi yaprsam JS tarafından otomatik olarak JS dict yapısına çevrilmiş olarak bana veriyor.
    return HttpResponse(data, content_type="application/json")