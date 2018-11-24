from django import forms
from orm.models import TesOlimpiade
# from django.contrib.auth.models import User


class TesOlimpiadeForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    mata_pelajaran = forms.CharField( max_length=30)
    no = forms.IntegerField(required=False, initial=0)
    gambar = forms.ImageField(required=False, initial="gambar/icon.png")
    pertayaan = forms.CharField( max_length=500)
    jawabanA = forms.CharField( max_length=300)
    jawabanB = forms.CharField( max_length=300)
    jawabanC = forms.CharField( max_length=300)
    jawabanD = forms.CharField( max_length=300)
    jawabanE = forms.CharField( max_length=300)
    kunci = forms.CharField( max_length=30)

    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = TesOlimpiade


