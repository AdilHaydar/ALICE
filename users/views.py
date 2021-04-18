from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
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

        