from django import forms
from orm.models import Bobot
# from django.contrib.auth.models import User


class BobotForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    nilai_akademik = forms.IntegerField( required=False, initial=0)
    kelas = forms.IntegerField( required=False, initial=0)
    karakter = forms.IntegerField( required=False, initial=0)
    hasil_tes = forms.IntegerField( required=False, initial=0)
    plomba = forms.IntegerField( required=False, initial=0)
    
    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = Bobot


