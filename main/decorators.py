from django.http import HttpResponse
from django.shortcuts import redirect


def authorized_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('<h3>You are not authorized to view this page</h3>')

    return wrapper_func

