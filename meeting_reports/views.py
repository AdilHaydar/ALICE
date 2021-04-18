from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import JsonResponse
from .models import MeetingReport, MeetingReportCategory, Meeting
from .forms import MeetingReportForm, MeetingForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    reports = MeetingReport.objects.all()

    #page = request.GET.get('page',1)
    p = Paginator(reports,5)
    reports = p.page(1)

    context = {
        'reports':reports,
        'nbar' : 'list-reports',
        'num_pages':p.num_pages,
    }

    return render(request, 'meeting/meeting_reports.html', context)

@login_required(login_url="user:login")
def add(request):
    categories = MeetingReportCategory.objects.all()
    form = MeetingReportForm(request.POST or None, request.FILES or None)

    nbar = "add-report"
    context = {'categories':categories,'form':form,'nbar':nbar}
    if form.is_valid():

        created_meeting = form.save(commit=False)
        created_meeting.user = request.user
        created_meeting.save()
        created_meeting.category.set(request.POST.getlist('category'))
        created_meeting.save()

    print(form.errors)
    return render(request,'meeting/meeting_reports_add.html', context)

def detail(request, id):
    report = get_object_or_404(MeetingReport, id=id)

    return render(request, 'meeting/meeting_reports_detail.html',{'report':report})


def add_change_delete_category(request):
    categories = MeetingReportCategory.objects.all()
    context = {
        'nbar': 'add-category',
        'categories':categories,
        'delete_category': None,
    }
    if request.method == 'POST':
        if request.is_ajax():
            category_name = request.POST.get('category_name')

            if MeetingReportCategory.objects.filter(category_name=category_name).exists():

                return JsonResponse({'success':False,'message':'Aynı Kategori Zaten Mevcut'}, status=400)

            MeetingReportCategory.objects.create(category_name=category_name)

            return JsonResponse({'success':True,'message':'Kategori Başarıyla Oluşturuldu'}, status=200)

        if request.POST.get('delete'):
            category = MeetingReportCategory.objects.get(id=request.POST.get('category_id'))
            category.delete()
            
            context.update({
                'delete_category':True,
                'deleted_category_name':category.category_name,
            })
            return render(request,'meeting/add_category.html', context)

    return render(request, 'meeting/add_category.html', context)

def update_category(request, pk):
    category = get_object_or_404(MeetingReportCategory, id=pk)

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        if MeetingReportCategory.objects.filter(category_name=category_name).exists():
            return JsonResponse({'success':False,'message':'Aynı Kategori Zaten Mevcut'}, status=400)

        category.category_name = category_name
        category.save()

        return JsonResponse({'success':True,'message':'Kategori Başarıyla Güncellendi.'}, status=200) 

    return render(request, 'meeting/update_category.html',{'category':category})


def meeting_list(request):
    meeting_lists = Meeting.objects.all()
    context = {
        'meeting_lists' : meeting_lists,
    }
    return render(request, 'meeting/meeting_list.html', context)

def add_meeting_list(request):
    form = MeetingForm(request.POST or None, request.FILES or None)

    context = {
        'form' : form,
    }

    if form.is_valid():
        created_meeting = form.save(commit=False)
        created_meeting.user = request.user
        created_meeting.save()

        return redirect('meeting-reports:meeting-list')

    return render(request, 'meeting/add_meeting_list.html',context)

def meeting_detail(request, pk):
    meeting = get_object_or_404(Meeting, id=pk)

    return render(request, 'meeting/meeting_detail.html',{'meeting':meeting})