from django import forms
from orm.models import  Siswa
from django.contrib.auth.models import  User


class SiswaForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    user_all = User.objects.all()
    user = forms.ModelChoiceField(queryset=user_all, initial=0)
    nama = forms.CharField(max_length=30)
    jenis_kelamin = forms.CharField(max_length=30)
    alamat = forms.CharField(max_length=70)
    
        
    class Meta:
        model = Siswa


