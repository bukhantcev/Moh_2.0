from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, ChoiceField, Select, SelectMultiple
from django.forms.widgets import ChoiceWidget
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

from .models import Profile





class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'password1','password2']

class Phone(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=12, min_length=11)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['podrazdelenie'].empty_label = 'Выберите подразделение'
        self.fields['dolgnost'].empty_label = 'Выберите должность'



    class Meta:
        model = Profile
        fields = ['phone', 'podrazdelenie', 'dolgnost',]

    def clean_phone(self):

        phone = self.cleaned_data['phone']
        ALLOWED_CHARS = '+1234567890-'
        phone_digits = ''
        for i in phone:
            if str(i).isdigit():
                phone_digits += i


        if not (set(phone) <= set(ALLOWED_CHARS)):
            raise ValidationError("Номер должен состоять из цифр")
        elif not ("+7" in phone[:2] or "8" == phone[0]):
            raise ValidationError("Номер должен начинаться на '+7' или '8' и состоять из 10 цифр, не считая кода страны")
        elif len(phone_digits) != 11:
            raise ValidationError(
                "Номер должен состоять из 10 цифр, не считая кода страны")
        else:
            return phone



class FormValid(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name' , 'phone', 'podrazdelenie', 'dolgnost',]
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
            }),
            'podrazdelenie': Select(attrs={
                'class': 'form-control',
            }),
            'dolgnost': Select(attrs={
                'class': 'form-control',
            }),
        }