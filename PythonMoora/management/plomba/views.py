from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Plomba,Siswa
from management.plomba import helpers
from .forms import PlombaForm
from library.view import ManagementAccessView
# Create your views here.

class ListPlombaView(ManagementAccessView):
	def get(self, request):
		template = 'plomba/index.html'
		form = PlombaForm(request.POST or None)
		plomba = Plomba.objects.all()
		data = {
		'form_mode' : 'add',
		'form' : form,
		'siswa' : Siswa.objects.all(),
		'plomba' : plomba,
		}
		return render(request, template, data)


class SavePlombaView(ManagementAccessView):
    def post(self, request):
        template = 'plomba/index.html'
        form = PlombaForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            plomba = Plomba()
            plomba.siswa = form.cleaned_data['siswa']
            plomba.intensitas = form.cleaned_data['intensitas']
            plomba.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            plomba.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            plomba.save()
            return redirect('plomba:view')
        else:
            plomba = Plomba.objects.all()
            data = {

                'form': form,
                'plomba': plomba,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditPlombaView(ManagementAccessView):
    template = 'plomba/edit.html'

    def get(self, request, id):
        plomba = Plomba.objects.filter(id=id)
        if not plomba.exists():
            return redirect('plomba:view')
        plomba = plomba.first()
        initial = {

            'id': plomba.id,
            'intensitas': plomba.intensitas,
            'mata_pelajaran': plomba.mata_pelajaran,
            'nilai': plomba.nilai,
            'siswa': plomba.siswa,
        }

        form = PlombaForm(initial=initial)
        plomba = Plomba.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'plomba' : plomba,
        }
        return render(request, self.template, data)



class UpdatePlombaView(ManagementAccessView):

    def post(self, request):
        
        template = "plomba/index.html"
        form = PlombaForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            plomba = Plomba.objects.get(pk=id)
            plomba.intensitas = form.cleaned_data['intensitas']
            plomba.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            plomba.nilai = form.cleaned_data['nilai']
            plomba.siswa = form.cleaned_data['siswa']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            plomba.save(force_update=True)
            return redirect('plomba:view')
        else:
            plomba = Plomba.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'plomba': plomba,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            # return render(request, template, data)
            return HttpResponse(form.errors)

class HapusPlombaView(ManagementAccessView):

    def get(self, request, id):
        plomba = Plomba.objects.filter(id=id)
        if plomba.exists():
            plomba.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('plomba:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      
