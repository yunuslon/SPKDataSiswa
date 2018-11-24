from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.view import ManagementAccessView
from orm.models import Siswa,SoalBiologi,NilaiAkademik,Kelas,Karakter,Plomba
from management.data_siswa.forms import UserForm, SiswaForm,NilaiAkademikForm,KelasForm,PlombaForm,KarakterForm
from management.data_siswa import helpers
import mimetypes
import os


class ListDataSiswaView(ManagementAccessView):
    def get(self, request):
        template = 'data_siswa/index.html'
       
        return render(request, template)

class ListDataSiswaBiologiView(ManagementAccessView):
    def get(self, request):
        sw = Siswa.objects.all()
        data_siswa = helpers.Data_SiswaBio(sw).as_matrix()
        template = 'data_siswa/biologi.html'
        data = {
            'data_siswa' : data_siswa,
        }
        return render(request, template, data)

class AddDataSiswaBioView(ManagementAccessView):
    def get(self, request):
        template = 'data_siswa/add_siswabio.html'
        user_form = UserForm(request.POST or None)
        siswa_form = SiswaForm(request.POST or None)
       
        data = {
            'user_form' : user_form,
            'siswa_form' : siswa_form,

        }
        return render(request, template, data)

class SaveDataSiswaBioView(ManagementAccessView):
    def post(self, request):
        siswa_form = SiswaForm(request.POST or None, request.FILES)
        nilaiakademik_form = NilaiAkademikForm(request.POST or None)
        kelas_form = KelasForm(request.POST or None)
        plomba_form = PlombaForm(request.POST or None)
        karakter_form = KarakterForm(request.POST or None)

        if siswa_form.is_valid() and nilaiakademik_form.is_valid() and kelas_form.is_valid() and plomba_form.is_valid() and karakter_form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            staff = request.POST.get('staff', None)
            if not staff == None:
                user.is_staff = True
                user.save()

                group = Group.objects.get(name='SoalBio')
                group.user_set.add(user)

                soalbiologi = SoalBiologi()
                soalbiologi.user = user
                soalbiologi.nama = user.username
                soalbiologi.save()

            else:
                 user.save()

            siswa = Siswa()
            siswa.user = user
            siswa.nama = siswa_form.cleaned_data['nama']
            siswa.alamat = siswa_form.cleaned_data['alamat']
            siswa.jenis_kelamin = siswa_form.cleaned_data['jenis_kelamin']
            siswa.save()

            nilaiak = NilaiAkademik()
            nilaiak.siswa = siswa
            nilaiak.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            nilaiak.nilai =nilaiakademik_form.cleaned_data['nilai']
            nilaiak.save()

            kelas = Kelas()
            kelas.siswa = siswa
            kelas.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            kelas.jenjang = kelas_form.cleaned_data['jenjang']
            kelas.nilai = kelas_form.cleaned_data['nilaikl']
            kelas.save() 

            plomba = Plomba()
            plomba.siswa = siswa
            plomba.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            plomba.intensitas = plomba_form.cleaned_data['intensitas']
            plomba.nilai = plomba_form.cleaned_data['nilaipl']
            plomba.save()

            karakter = Karakter()
            karakter.siswa = siswa
            karakter.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            karakter.sikap = karakter_form.cleaned_data['sikap']
            karakter.nilai = karakter_form.cleaned_data['nilaikr']
            karakter.save()

            return redirect('data_siswa:biologi')
        else:
            return HttpResponse(siswa_form.errors)

class HapusDataSiswaBioView(ManagementAccessView):
    
    def get(self, request, id):
        siswa = Siswa.objects.filter(id=id)
        if siswa.exists():
            siswa.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_siswa:biologi')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 