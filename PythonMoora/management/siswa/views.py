from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Siswa
from library.view import ManagementAccessView
from management.siswa.forms import SiswaForm
from django.contrib.auth.models import  User
# Create your views here.

class ListSiswaView(ManagementAccessView):
    def get(self, request):
        template = 'siswa/index.html'
        form = SiswaForm(request.POST or None)
        siswa = Siswa.objects.all()
        data = {
        'form_mode' : 'add',
        'form' : form,
		'user' : User.objects.all(),
		'siswa' : siswa,
        }
        return render(request, template, data)


class SaveSiswaView(ManagementAccessView):
    def post(self, request):
        template = 'siswa/index.html'
        form = SiswaForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            siswa = Siswa()
            siswa.user = form.cleaned_data['user']
            siswa.nama = form.cleaned_data['nama']
            siswa.jenis_kelamin = form.cleaned_data['jenis_kelamin']
            siswa.alamat = form.cleaned_data['alamat']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            siswa.save()
            return redirect('siswa:view')
        else:
            siswa = Siswa.objects.all()
            data = {

                'form': form,
                'siswa': siswa,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditSiswaView(ManagementAccessView):
    template = 'siswa/edit.html'

    def get(self, request, id):
        siswa = Siswa.objects.filter(id=id)
        if not siswa.exists():
            return redirect('siswa:view')
        siswa = siswa.first()
        initial = {

            'id': siswa.id,
            'nama': siswa.nama,
            'jenis_kelamin': siswa.jenis_kelamin,
            'alamat': siswa.alamat,
            'user': siswa.user,
        }

        form = SiswaForm(initial=initial)
        siswa = Siswa.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'siswa' : siswa,
        }
        return render(request, self.template, data)



class UpdateSiswaView(ManagementAccessView):

    def post(self, request):
        
        template = "siswa/index.html"
        form = SiswaForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            siswa = Siswa.objects.get(pk=id)
            siswa.user = form.cleaned_data['user']
            siswa.nama = form.cleaned_data['nama']
            siswa.jenis_kelamin = form.cleaned_data['jenis_kelamin']
            siswa.alamat = form.cleaned_data['alamat']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            siswa.save(force_update=True)
            return redirect('siswa:view')
        else:
            siswa = Siswa.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'siswa': siswa,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            # return render(request, template, data)
            return HttpResponse(form.errors)

class HapusSiswaView(ManagementAccessView):

    def get(self, request, id):
        siswa = Siswa.objects.filter(id=id)
        if siswa.exists():
            siswa.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('siswa:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      