from django import forms
from orm.models import NilaiAkademik,Siswa
# from django.contrib.auth.models import User


class NilaiAkdemikForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    mata_pelajaran = forms.CharField(max_length=30)
    nilai = forms.IntegerField( required=False, initial=0)
    siswa_all = Siswa.objects.all()
    siswa = forms.ModelChoiceField(queryset=siswa_all, initial=0) 
    
    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = NilaiAkademik


