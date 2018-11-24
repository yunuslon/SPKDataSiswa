from django import forms
from orm.models import Siswa,NilaiAkademik,Kelas,Plomba,Karakter
from django.contrib.auth.models import User


class UserForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User

class SiswaForm(forms.Form):
    nama = forms.CharField(max_length=30)
    jenis_kelamin = forms.CharField(max_length=30)
    alamat = forms.CharField(max_length=70)

    class Meta:
        model = Siswa

class NilaiAkademikForm(forms.Form):
    mata_pelajaran = forms.CharField(max_length=50)
    nilai = forms.IntegerField(initial=0)
    
    class Meta:
        model = NilaiAkademik

class KelasForm(forms.Form):
    jenjang = forms.CharField(max_length=30)
    nilaikl = forms.IntegerField(initial=0)
    
    class Meta:
        model = Kelas

class PlombaForm(forms.Form):
    intensitas = forms.CharField(max_length=30)
    nilaipl = forms.IntegerField(initial=0)
    
    class Meta:
        model = Plomba

class KarakterForm(forms.Form):
    sikap = forms.CharField(max_length=30)
    nilaikr = forms.IntegerField(initial=0)
    
    class Meta:
        model = Karakter