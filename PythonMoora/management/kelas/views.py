from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Kelas,Siswa,User
from management.kelas.forms import KelasForm
from library.view import ManagementAccessView
# from django.contrib.auth.models import User


# Create your views here.



class ListKelasView(ManagementAccessView):
	def get(self, request):

		template = 'kelas/index.html'

		form = KelasForm(request.POST or None)
		kelas = Kelas.objects.all()
		data = {
        'form_mode' : 'add',
        'form' : form,
		'siswa' : Siswa.objects.all(),
		'kelas' : kelas,
		}
		return render(request, template, data)


class SaveKelasView(ManagementAccessView):
    def post(self, request):
        template = 'kelas/index.html'
        form = KelasForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            kelas = Kelas()
            kelas.siswa = form.cleaned_data['siswa']
            kelas.jenjang = form.cleaned_data['jenjang']
            kelas.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            kelas.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            kelas.save()
            return redirect('kelas:view')
        else:
            kelas = Kelas.objects.all()
            data = {

                'form': form,
                'kelas': kelas,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditKelasView(ManagementAccessView):
    template = 'kelas/edit.html'

    def get(self, request, id):
        kelas = Kelas.objects.filter(id=id)
        if not kelas.exists():
            return redirect('kelas:view')
        kelas = kelas.first()
        initial = {

            'id': kelas.id,
            'jenjang': kelas.jenjang,
            'mata_pelajaran': kelas.mata_pelajaran,
            'nilai': kelas.nilai,
            'siswa': kelas.siswa,
        }

        form = KelasForm(initial=initial)
        kelas = Kelas.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'kelas' : kelas,
        }
        return render(request, self.template, data)



class UpdateKelasView(ManagementAccessView):

    def post(self, request):
        
        template = "kelas/index.html"
        form = KelasForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            kelas = Kelas.objects.get(pk=id)
            kelas.jenjang = form.cleaned_data['jenjang']
            kelas.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            kelas.nilai = form.cleaned_data['nilai']
            kelas.siswa = form.cleaned_data['siswa']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            kelas.save(force_update=True)
            return redirect('kelas:view')
        else:
            kelas = Kelas.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'kelas': kelas,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            # return render(request, template, data)
            return HttpResponse(form.errors)

class HapusKelasView(ManagementAccessView):

    def get(self, request, id):
        kelas = Kelas.objects.filter(id=id)
        if kelas.exists():
            kelas.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('kelas:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      