from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render


def unauthenticate(view_func):
    def wrapper_fun(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            view_func(request, *args, **kwargs)
    return wrapper_fun