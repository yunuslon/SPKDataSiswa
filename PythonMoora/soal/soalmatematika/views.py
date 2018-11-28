from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import TesOlimpiade,HasilTes,SoalMatematika
from soal.soalmatematika import helpers
from soal.soalmatematika.forms import HasilTesForm
from library.view import SoalMatAccessView
from django.contrib.auth import authenticate, login, logout




class ListSoalMatematikaView(SoalMatAccessView):
    template_name = 'soalmatematika/index.html'
      

    def get(self, request):
        tp = TesOlimpiade.objects.all()
        tesolimpiade = helpers.SleksiSoalMat(tp).as_matrix()
       
        data = {
        'tesolimpiade2' : tesolimpiade,
        'tesolimpiade': {
               'total': len(tesolimpiade)
                # 'email':

                },

                }

        return render(request, self.template_name, data)

class SimpanHasilTesMatView(SoalMatAccessView):
    template_name = 'soalmatematika/index.html'

    def post(self, request):
        form = HasilTesForm(request.POST or None)
        if form.is_valid():
            hasiltes = HasilTes()
            # hasiltes.user = request.user
            hasiltes.siswa_id = request.user.siswa.id
            hasiltes.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            hasiltes.nilai = form.cleaned_data['nilai']
            hasiltes.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Simpan  nilai berhasil')
            return redirect('soalmatematika:hasil')

class ListHasilView(SoalMatAccessView):
    template_name = 'soalmatematika/hasil.html'
      

    def get(self, request):
        ht = HasilTes.objects.all()
       
        data = {
            'ht' : ht,

                }

        return render(request, self.template_name, data)

class HapusDaftarPesertaMatematikaView(SoalMatAccessView):
    
    def get(self, request, id):
        soalmatematika = SoalMatematika.objects.filter(id=id)
        if soalmatematika.exists():
            soalmatematika.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            logout(request)
            return redirect('login:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  
