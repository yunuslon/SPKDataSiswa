from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter, Siswa
from .forms import KarakterForm
from library.view import ManagementAccessView
# Create your views here.

class ListKarakterView(ManagementAccessView):
    def get(self, request):
        template = 'karakter/index.html'
        karakter = Karakter.objects.all()
        form = KarakterForm(request.POST or None)
        data = {
            'form' : form,
            'karakter' : karakter,
            'siswa' : Siswa.objects.all(),
        }
        return render(request, template, data)


class SaveKarakterView(ManagementAccessView):
    def post(self, request):
        template = 'karakter/index.html'
        form = KarakterForm(request.POST or None)
        if form.is_valid():
            
            karakter = Karakter()
            karakter.siswa = form.cleaned_data['siswa']
            karakter.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            karakter.sikap = form.cleaned_data['sikap']
            karakter.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            karakter.save()
            return redirect('karakter:view')
        else:
            karakter = Karakter.objects.all()
            data = {
                'form': form,
                'karakter': karakter,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditKarakterView(ManagementAccessView):
    template = 'karakter/edit.html'

    def get(self, request, id):
        karakter = Karakter.objects.filter(id=id)
        if not karakter.exists():
            return redirect('karakter:view')
        karakter = karakter.first()
        initial = {

            'id': karakter.id,
            'mata_pelajaran': karakter.mata_pelajaran,
            'sikap': karakter.sikap,
            'nilai': karakter.nilai,
            'siswa': karakter.siswa,
        }

        form = KarakterForm(initial=initial)
        karakter = Karakter.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'karakter' : karakter,
        }
        return render(request, self.template, data)


class UpdateKarakterView(ManagementAccessView):

    def post(self, request):
        
        template = "karakter/index.html"
        form = KarakterForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            karater = Karakter.objects.get(pk=id)
            karater.siswa = form.cleaned_data['siswa']
            karater.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            karater.sikap = form.cleaned_data['sikap']
            karater.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            karater.save(force_update=True)
            return redirect('karakter:view')
        else:
            karater = Karakter.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'karakter': karater,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)




class HapusKarakterView(ManagementAccessView):
    
    def get(self, request, id):
        karakter = Karakter.objects.filter(id=id)
        if karakter.exists():
            karakter.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('karakter:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      



