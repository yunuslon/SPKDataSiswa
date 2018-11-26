from django import forms
from django.contrib.auth.models import  User


class UserForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    last_name = forms.CharField( max_length=150, required=False)    
        
    class Meta:
        model = User

