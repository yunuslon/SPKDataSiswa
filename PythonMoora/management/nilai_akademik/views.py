from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import NilaiAkademik,Siswa
from .forms import NilaiAkdemikForm
from library.view import ManagementAccessView
# Create your views here.

class ListNilaiAkademikView(ManagementAccessView):
    def get(self, request):
        template = 'nilai_akademik/index.html'

        form = NilaiAkdemikForm(request.POST or None)
        nilai_akademik = NilaiAkademik.objects.all()
        data = {
            'form'  : form,
            'siswa' : Siswa.objects.all(),
            'nilai_akademik' : nilai_akademik,
        }
        return render(request, template, data)


class SaveNilaiAkademikView(ManagementAccessView):
    def post(self, request):
        template = 'nilai_akademik/index.html'
        form = NilaiAkdemikForm(request.POST or None)
        if form.is_valid():
            
            nilaiakademik = NilaiAkademik()
            nilaiakademik.siswa = form.cleaned_data['siswa']
            nilaiakademik.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            nilaiakademik.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            nilaiakademik.save()
            return redirect('nilai_akademik:view')
        else:
            nilaiakademik = NilaiAkademik.objects.all()
            data = {
                'form': form,
                'nilaiakademik': nilaiakademik,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)


class EditNilaiAkademikView(ManagementAccessView):
    template = 'nilai_akademik/edit.html'

    def get(self, request, id):
        nilai_akademik = NilaiAkademik.objects.filter(id=id)
        if not nilai_akademik.exists():
            return redirect('nilai_akademik:view')
        nilai_akademik = nilai_akademik.first()
        initial = {

            'id': nilai_akademik.id,
            'mata_pelajaran': nilai_akademik.mata_pelajaran,
            'nilai': nilai_akademik.nilai,
            'siswa': nilai_akademik.siswa,
        }

        form = NilaiAkdemikForm(initial=initial)
        nilai_akademik = NilaiAkademik.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'nilaiakademik' : nilai_akademik,
        }
        return render(request, self.template, data)


class UpdateNilaiAkademikView(ManagementAccessView):

    def post(self, request):
        
        template = "nilai_akademik/index.html"
        form = NilaiAkdemikForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            nilai_akademik = NilaiAkademik.objects.get(pk=id)
            nilai_akademik.siswa = form.cleaned_data['siswa']
            nilai_akademik.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            nilai_akademik.nilai = form.cleaned_data['nilai']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            nilai_akademik.save(force_update=True)
            return redirect('nilai_akademik:view')
        else:
            nilai_akademik = NilaiAkademik.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'nilai_akademik': nilai_akademik,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)




class HapusNilaiAkademikView(ManagementAccessView):
    
    def get(self, request, id):
        nilaiakademik = NilaiAkademik.objects.filter(id=id)
        if nilaiakademik.exists():
            nilaiakademik.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('nilai_akademik:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

