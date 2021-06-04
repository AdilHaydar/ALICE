from django.shortcuts import redirect

def authorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_anonymous:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')
        
    return wrapper_func