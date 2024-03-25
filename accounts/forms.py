from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings



class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget = forms.TextInput(attrs={'class':'form-control input-lg', 'placeholder':'username'}),min_length=3)
    password = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={'class':'form-control input-lg', 'placeholder':'********'}), min_length=6)

