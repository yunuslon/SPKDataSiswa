from django import forms
from orm.models import Plomba,Siswa


class PlombaForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    intensitas = forms.CharField(max_length=30)
    mata_pelajaran = forms.CharField(max_length=30)
    nilai = forms.IntegerField( required=False, initial=0)
    siswa_all = Siswa.objects.all()
    siswa = forms.ModelChoiceField(queryset=siswa_all, initial=0) 
    
    
    class Meta:
        model = Plomba


