from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import RegisterForm
from .decorators import authorized_user
from django.contrib.auth.hashers import check_password
# Create your views here.

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if len(user) == 0:
            return JsonResponse({'success':False,'message':'Kullanıcı Adı Yanlış'}, status=403)
    
        user = authenticate(username=username,password=password)

        if user is None:
            return JsonResponse({'success':False,'message':'Parola Eşleşmiyor'}, status=403)
        
        login(request,user)
        return JsonResponse({'success':True},status=200)
    return render(request,'User/login.html')

def logout_user(request):
    logout(request)
    return redirect('user:login')

@authorized_user
def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form,
    }

    if request.is_ajax():

        if form.is_valid():
            registered_user = form.save(commit=False)
            registered_user.save()
            login(request, registered_user)

            #return redirect('index')
            return JsonResponse({'success':True}, status=200)

        return JsonResponse({'success':False,'message':form.errors}, status=406)

    return render(request,'User/register.html', context)


def check_username(request, username):
    username = User.objects.filter(username=username)

    if username.exists():

        return JsonResponse({'success':False}, status=406)

    return JsonResponse({'success':True}, status=200)