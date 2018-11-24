from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import SoalBiologi,SoalFisika,SoalKimia,SoalMatematika
from soal.daftar_olimpiade.forms import SoalForm
from library.view import ManagementAccessView
from django.contrib.auth.models import User


# Create your views here.



class ListDaftarView(ManagementAccessView):
	def get(self, request):

		template = 'daftar_olimpiade/index.html'

		form = SoalForm(request.POST or None)
		soalbiologi = SoalBiologi.objects.all()
		data = {
        'form_mode' : 'add',
        'form' : form,
		'soalbiologi' :soalbiologi,
        'soalfisika' :SoalFisika.objects.all(),
        'soalkimia' :SoalKimia.objects.all(),
        'soalmatematika' :SoalMatematika.objects.all(),
        'user' : User.objects.all(),
		}
		return render(request, template, data)


class SaveDaftarBiologiView(ManagementAccessView):
    def post(self, request):
        template = 'daftar_olimpiade/index.html'
        form = SoalForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            soalbiologi = SoalBiologi()
            soalbiologi.user = form.cleaned_data['user']
            soalbiologi.nama = form.cleaned_data['nama']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            soalbiologi.save()
            return redirect('daftar_olimpiade:view')
        else:
            soalbiologi = SoalBiologi.objects.all()
            data = {

                'form': form,
                'soalbiologi': soalbiologi,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class SaveDaftarFisikaView(ManagementAccessView):
    def post(self, request):
        template = 'daftar_olimpiade/index.html'
        form = SoalForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            soalfisika = SoalFisika()
            soalfisika.user = form.cleaned_data['user']
            soalfisika.nama = form.cleaned_data['nama']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            soalfisika.save()
            return redirect('daftar_olimpiade:view')
        else:
            soalfisika = SoalFisika.objects.all()
            data = {

                'form': form,
                'soalfisika': soalfisika,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class SaveDaftarKimiaView(ManagementAccessView):
    def post(self, request):
        template = 'daftar_olimpiade/index.html'
        form = SoalForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            soalkimia = SoalKimia()
            soalkimia.user = form.cleaned_data['user']
            soalkimia.nama = form.cleaned_data['nama']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            soalkimia.save()
            return redirect('daftar_olimpiade:view')
        else:
            soalkimia = SoalKimia.objects.all()
            data = {

                'form': form,
                'soalkimia': soalkimia,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class SaveDaftarMatematikaView(ManagementAccessView):
    def post(self, request):
        template = 'daftar_olimpiade/index.html'
        form = SoalForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            soalmatematika = SoalMatematika()
            soalmatematika.user = form.cleaned_data['user']
            soalmatematika.nama = form.cleaned_data['nama']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            soalmatematika.save()
            return redirect('daftar_olimpiade:view')
        else:
            soalmatematika = SoalMatematika.objects.all()
            data = {

                'form': form,
                'soalmatematika': soalmatematika,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class HapusBiologiView(ManagementAccessView):

    def get(self, request, id):
        soalbiologi = SoalBiologi.objects.filter(id=id)
        if soalbiologi.exists():
            soalbiologi.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('daftar_olimpiade:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  

class HapusFisikaView(ManagementAccessView):

    def get(self, request, id):
        soalfisika = SoalFisika.objects.filter(id=id)
        if soalfisika.exists():
            soalfisika.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('daftar_olimpiade:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  

class HapusKimiaView(ManagementAccessView):

    def get(self, request, id):
        soalkimia = SoalKimia.objects.filter(id=id)
        if soalkimia.exists():
            soalkimia.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('daftar_olimpiade:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  

class HapusMatematikaView(ManagementAccessView):

    def get(self, request, id):
        soalmatematika = SoalMatematika.objects.filter(id=id)
        if soalmatematika.exists():
            soalmatematika.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('daftar_olimpiade:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  