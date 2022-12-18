from django import forms
from . import models
from django.contrib.auth.models import User

CHOICES= [
    ('male', 'male'),
    ('female', 'female'),
    ]

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class Form(forms.ModelForm):

    class Meta:
        model= models.Student
        fields=['address','mobile','profile_pic','gender']
        widgets = {
            'gender': forms.RadioSelect()
        }


class Medform(forms.ModelForm):

    class Meta:
        model= models.med
        fields=['m','mobile']