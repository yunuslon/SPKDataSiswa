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
        na = NilaiAkademik.objects.all()
        template = 'data_siswa/biologi.html'
        data = {
            'siswa' : na.filter(mata_pelajaran='biologi'),
        }
        return render(request, template, data)

class DetailDataSiswaBioView(ManagementAccessView):
    def get(self, request, id):
        template = 'data_siswa/detail_siswabio.html'
        data = {
            'siswa' : Siswa.objects.get(id=id)
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
            siswa.tanggal_lahir= siswa_form.cleaned_data['tanggal_lahir']
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
        user = User.objects.filter(id=id)
        if user.exists():
            user.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_siswa:biologi')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class UbahBioView(ManagementAccessView):
    def get(self, request, id):
        template = 'data_siswa/edit_siswabio.html'
        data = {
            'siswa': Siswa.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateBioView(ManagementAccessView):
    def post(self, request, id):
        user = User.objects.get(id=id)
        soalbiologi = SoalBiologi.objects.get(id=id)
        siswa = Siswa.objects.get(id=id)
        nilaiak = NilaiAkademik.objects.get(id=id)
        kelas = Kelas.objects.get(id=id)
        plomba = Plomba.objects.get(id=id)
        karakter = Karakter.objects.get(id=id)

        siswa_form = SiswaForm(request.POST or None, request.FILES)
        nilaiakademik_form = NilaiAkademikForm(request.POST or None)
        kelas_form = KelasForm(request.POST or None)
        plomba_form = PlombaForm(request.POST or None)
        karakter_form = KarakterForm(request.POST or None)
        user_form = UserForm(request.POST, request.FILES)

        if siswa_form.is_valid() and nilaiakademik_form.is_valid() and kelas_form.is_valid() and plomba_form.is_valid() and karakter_form.is_valid():
            if user_form.is_valid():
                user = siswa.user
                user.username = user_form.cleaned_data['user']
                user.set_password(user_form.cleaned_data['password']) 
                user.save()
                siswa.user = user
            
        
            siswa.user = user
            siswa.nama = siswa_form.cleaned_data['nama']
            siswa.tanggal_lahir= siswa_form.cleaned_data['tanggal_lahir']
            siswa.alamat = siswa_form.cleaned_data['alamat']
            siswa.jenis_kelamin = siswa_form.cleaned_data['jenis_kelamin']
            siswa.save(force_update=True)

           
            nilaiak.siswa = siswa
            nilaiak.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            nilaiak.nilai =nilaiakademik_form.cleaned_data['nilai']
            nilaiak.save(force_update=True)

           
            kelas.siswa = siswa
            kelas.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            kelas.jenjang = kelas_form.cleaned_data['jenjang']
            kelas.nilai = kelas_form.cleaned_data['nilaikl']
            kelas.save(force_update=True) 


            plomba.siswa = siswa
            plomba.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            plomba.intensitas = plomba_form.cleaned_data['intensitas']
            plomba.nilai = plomba_form.cleaned_data['nilaipl']
            plomba.save(force_update=True)


            karakter.siswa = siswa
            karakter.mata_pelajaran = nilaiakademik_form.cleaned_data['mata_pelajaran']
            karakter.sikap = karakter_form.cleaned_data['sikap']
            karakter.nilai = karakter_form.cleaned_data['nilaikr']
            karakter.save(force_update=True)

            return redirect('data_siswa:biologi', id=id)
        else:
            return HttpResponse(siswa_form.errors)