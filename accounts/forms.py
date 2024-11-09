from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

class Phone(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'phone', 'dolgnost']