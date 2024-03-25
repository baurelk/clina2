from urllib import request
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout

from accounts.forms import LoginForm
from clina import settings

# Create your views here.

class loginView(View):

    def get(self, request, *args, **kwargs):
        
        login_form = LoginForm()
        
        if request.method == 'POST':

            login_form = LoginForm(request.POST)
            
            if login_form.is_valid():
                cleaned_data = login_form.cleaned_data
                user = auth.authenticate(request, username=cleaned_data.get('username'),password=cleaned_data.get('password'))
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, "Logged in Successfully!")
                    print("Logged in Successfully!")
                    return redirect("app:home")
                else:
                    messages.error(request, "Invalid credentials, wrong username or password")
                    print("Invalid credentials, wrong username or password")
            else:
                messages.error(request, "form invalid")
                print("form invalid")
        
        return render(request, 'accounts/login.html', {'form': login_form})


class logoutView(View):
    @login_required
    def logaout(args):
        logout(request)
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        