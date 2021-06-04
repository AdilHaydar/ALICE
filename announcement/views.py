from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required
from main.decorators import authorized_user
# Create your views here.
from datetime import datetime
import pytz

@authorized_user
def add_announcement(request):

    if request.is_ajax():
        
        date = list(map(int,request.POST.get('date').split('-')))
        time = list(map(int,request.POST.get('time').split(':')))

        deadline_at = datetime(date[0],date[1],date[2],time[0],time[1], tzinf=pytz.UTC)

        Announcement.objects.create(user=request.user,title=request.POST.get('title'),announcement=request.POST.get('announcement'),deadline_at=deadline_at)

        return JsonResponse({'success':True},status=200)
    
    return JsonResponse({'success':False}, status=406)

def list_announcement(request):
    form = AnnouncementForm()
    announcements = Announcement.objects.get_publish_announcement()
    nbar = 'announcement'

    context = {
        'announcements':announcements,
        'nbar':nbar,
        'form':form,
    }

    return render(request,'announcement/list_announcement.html',context)
