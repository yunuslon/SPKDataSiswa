from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import HasilTes,Siswa
from .forms import HasilTesForm
from library.view import ManagementAccessView
# Create your views here.

class ListHasilTesView(ManagementAccessView):
	def get(self, request):
		template = 'hasiltes/index.html'
		form = HasilTesForm(request.POST or None)
		hasiltes = HasilTes.objects.all()
		data = {
		'form_mode' : 'add',
		'form' : form,
		'siswa' : Siswa.objects.all(),
		'hasiltes' : hasiltes,
		}
		return render(request, template, data)


class SaveHasilTesView(ManagementAccessView):
    def post(self, request):
        template = 'hasiltes/index.html'
        form = HasilTesForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            hasiltes = HasilTes()
            hasiltes.siswa = form.cleaned_data['siswa']
            hasiltes.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            hasiltes.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            hasiltes.save()
            return redirect('hasiltes:view')
        else:
            hasiltes = HasilTes.objects.all()
            data = {

                'form': form,
                'hasiltes': hasiltes,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditHasilTesView(ManagementAccessView):
    template = 'hasiltes/edit.html'

    def get(self, request, id):
        hasiltes = HasilTes.objects.filter(id=id)
        if not hasiltes.exists():
            return redirect('hasiltes:view')
        hasiltes = hasiltes.first()
        initial = {

            'id': hasiltes.id,
            'mata_pelajaran': hasiltes.mata_pelajaran,
            'nilai': hasiltes.nilai,
            'siswa': hasiltes.siswa,
        }

        form = HasilTesForm(initial=initial)
        hasiltes = HasilTes.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'hasiltes' : hasiltes,
        }
        return render(request, self.template, data)



class UpdateHasilTesView(ManagementAccessView):

    def post(self, request):
        
        template = "hasiltes/index.html"
        form = HasilTesForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            hasiltes = HasilTes.objects.get(pk=id)
            hasiltes.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            hasiltes.nilai = form.cleaned_data['nilai']
            hasiltes.siswa = form.cleaned_data['siswa']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            hasiltes.save(force_update=True)
            return redirect('hasiltes:view')
        else:
            hasiltes = HasilTes.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'hasiltes': hasiltes,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            # return render(request, template, data)
            return HttpResponse(form.errors)

class HapusHasilTesView(ManagementAccessView):

    def get(self, request, id):
        hasiltes = HasilTes.objects.filter(id=id)
        if hasiltes.exists():
            hasiltes.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('hasiltes:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      
