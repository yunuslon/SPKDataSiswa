from django import forms
from orm.models import SoalBiologi,SoalFisika,SoalKimia,SoalMatematika
from django.contrib.auth.models import  User

class SoalForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    nama = forms.CharField(max_length=30)
    user_all = User.objects.all()
    user = forms.ModelChoiceField(queryset=user_all, initial=0) 
    class Meta:
        model = SoalBiologi

