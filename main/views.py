from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Main, MainImage, ContactInformation, Calendar
from .forms import MainImageForm, MainForm, ContactForm
from .decorators import authorized_user
from django.template.loader import render_to_string
from django.forms import inlineformset_factory
from django.core.serializers.json import DjangoJSONEncoder #datetime field json çevirme işleminde hata veriyor bununla çözüyorum.
from announcement.models import Announcement
import json, datetime, pytz
from main.decorators import authorized_user
# Create your views here.

def index(request):
    main_data = Main.objects.first()
    main_pics = MainImage.objects.filter(main=main_data)

    context = {
        'main_data':main_data,
        'main_pics':main_pics,
    }
    return render(request,'base/base.html',context)

def lazy_announcement(request):
    data = {'success':True}
    announcements = Announcement.objects.get_publish_announcement()
    html_data = render_to_string('base/includes/double_page.html',{'announcements':announcements})

    data.update({
        'html_data':html_data
    })

    return JsonResponse(data=data,status=200)

def lazy_main(request):
    data = {'success':True}
    main_data = Main.objects.first()
    main_pics = MainImage.objects.filter(main=main_data)
    html_data = render_to_string('base/includes/double_page.html',{'main_data':main_data,'main_pics':main_pics})

    data.update({
        'html_data':html_data
    })

    return JsonResponse(data=data, status=200)

@authorized_user
def add(request):
    MainImageFormSet = inlineformset_factory(Main, MainImage, fields=('image',), extra=0)
    
    main_instance = Main.objects.first()
    formset = MainImageFormSet(request.POST or None , request.FILES or None, instance=main_instance)
    
    main_form = MainForm(request.POST or None, instance=main_instance)
    main_image_form = MainImageForm(request.FILES or None)

    context = {
        'main_form': main_form,
        'main_image_form': main_image_form,
        'formset':formset,
    }

    if main_form.is_valid():
        created_main_content = main_form.save(commit=False)
        created_main_content.edited_user = request.user
        created_main_content.save()

        #main_image_form.has_changed() güncellemde bunu da kullan değişiklik yapılmadıysa false döndürüyor.
        if formset.is_valid():
            formset.save()

        if main_image_form.is_valid():
             for data in request.FILES.getlist('image'):
                MainImage.objects.create(main=created_main_content, image=data)

        return redirect('index')

    return render(request, 'main/add.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    contact_info = ContactInformation.objects.first()
    context = {'form':form,'contact_info':contact_info}

    if form.is_valid():
        form.save()

        return redirect('index')

    return render(request,'main/contact.html',context)

def calendar(request):
    data = list(Calendar.objects.values())
    data = json.dumps(data,cls=DjangoJSONEncoder)
    is_admin = json.dumps(request.user.is_staff)

    
    return render(request, 'main/calendar.html',{'data':data,'is_admin':is_admin})

@authorized_user
def drag_event(request):
    
    calendar_instance = Calendar.objects.get(id=request.POST.get('id'))
    date_start, time_start = request.POST.get('start').split('T')
    date_start = list(map(int,date_start.split('-')))
    time_start = list(map(int,time_start.split(':')[:2]))

    calendar_instance.start = datetime.datetime(date_start[0], date_start[1], date_start[2], time_start[0], time_start[1], tzinfo=pytz.UTC)

    # ! Zaman dilimiyle mi alakalı bilmiyorum fakat GMT+03:00 diyor fullcalender ve gönderdiği saati 3 saat geriye alarak bana veriyor, datetime içerisinde tzinfo=pytz.UTC dediğimde python bu saati tekrar 3 saat ileri atıyor.

    if request.POST.get('end'):
        date_end, time_end = request.POST.get('end').split('T')
        date_end = list(map(int,date_end.split('-')))
        time_end = list(map(int,time_end.split(':')[:2]))
        calendar_instance.end = datetime.datetime(date_end[0], date_end[1], date_end[2], time_end[0], time_end[1], tzinfo=pytz.UTC)

    calendar_instance.save()

    return JsonResponse({'success':True}, status=200)

@authorized_user
def add_new_event(request):
    if (not request.POST.get('title')) or (not request.POST.get('start_date')):
        error_message = ('Başlık Alanı', 'Başlangıç Tarihi')[bool(request.POST.get('title'))]

        return JsonResponse({'success':False,'message': f'{error_message} Boş Girilemez!' }, status=406)
    
    start_date = list(map(int,request.POST.get('start_date').split('-')))

    calendar = Calendar()
    calendar.title = request.POST.get('title')
    
    if request.POST.get('start_time'):
        start_time = list(map(int,request.POST.get('start_time').split(':')))
        calendar.start = datetime.datetime(start_date[0],start_date[1],start_date[2], start_time[0], start_time[1], tzinfo=pytz.UTC)
    else:
        calendar.start = datetime.datetime(start_date[0],start_date[1],start_date[2],tzinfo=pytz.UTC)

    if request.POST.get('end_date'):
        end_date = list(map(int,request.POST.get('end_date').split('-')))
        
        if request.POST.get('end_time'):
            end_time = list(map(int,request.POST.get('end_time').split(':')))
            calendar.end = datetime.datetime(end_date[0],end_date[1],end_date[2], end_time[0],end_time[1], tzinfo=pytz.UTC)
        else:
            calendar.end = datetime.datetime(end_date[0],end_date[1],end_date[2],tzinfo=pytz.UTC)
    calendar.save()
    
    

    return JsonResponse({'success':True}, status=200)

@authorized_user
def update_event(request):
    if (not request.POST.get('title')) or (not request.POST.get('start_date')):
        error_message = ('Başlık Alanı', 'Başlangıç Tarihi')[bool(request.POST.get('title'))]

        return JsonResponse({'success':False,'message': f'{error_message} Boş Girilemez!' }, status=406)

    start_date = list(map(int,request.POST.get('start_date').split('-')))

    calendar = Calendar.objects.get(id=request.POST.get('id'))

    calendar.title = request.POST.get('title')
    
    if request.POST.get('start_time'):
        start_time = list(map(int,request.POST.get('start_time').split(':')))
        calendar.start = datetime.datetime(start_date[0],start_date[1],start_date[2], start_time[0], start_time[1],tzinfo=pytz.UTC)
    else:
        calendar.start = datetime.datetime(start_date[0],start_date[1],start_date[2],tzinfo=pytz.UTC)

    if request.POST.get('end_date'):
        end_date = list(map(int,request.POST.get('end_date').split('-')))
        
        if request.POST.get('end_time'):
            end_time = list(map(int,request.POST.get('end_time').split(':')))
            calendar.end = datetime.datetime(end_date[0],end_date[1],end_date[2], end_time[0],end_time[1],tzinfo=pytz.UTC)
        else:
            calendar.end = datetime.datetime(end_date[0],end_date[1],end_date[2],tzinfo=pytz.UTC)
    else:
        calendar.end = None

    calendar.save()


    return JsonResponse({'success':True}, status=200)

@authorized_user
def delete_event(request):
    calendar = Calendar.objects.filter(id=request.POST.get('id'))

    if calendar.exists():
        calendar.first().delete()

        return JsonResponse({'success':True}, status=200)

    return JsonResponse({'success':False}, status=404)