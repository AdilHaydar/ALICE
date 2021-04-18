from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login')
def add_announcement(request):

    if request.is_ajax():
        print(request.POST.get('announcement'))
        Announcement.objects.create(user=request.user,title=request.POST.get('title'),announcement=request.POST.get('announcement'),deadline_at=request.POST.get('deadline_at'))

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
