from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import TesOlimpiade,HasilTes,SoalKimia
from soal.soalkimia import helpers
from soal.soalkimia.forms import HasilTesForm
from library.view import SoalKimAccessView
from django.contrib.auth import authenticate, login, logout




class ListSoalKimiaView(SoalKimAccessView):
    template_name = 'soalkimia/index.html'
      

    def get(self, request):
        tp = TesOlimpiade.objects.all()
        tesolimpiade = helpers.SleksiSoalKim(tp).as_matrix()
       
        data = {
        'tesolimpiade2' : tesolimpiade,
        'tesolimpiade': {
               'total': len(tesolimpiade)
                # 'email':

                },

                }

        return render(request, self.template_name, data)

class SimpanHasilTesKimView(SoalKimAccessView):
    template_name = 'soalkimia/index.html'

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
            return redirect('soalkimia:hasil')

class ListHasilView(SoalKimAccessView):
    template_name = 'soalkimia/hasil.html'
      

    def get(self, request):
        ht = HasilTes.objects.all()
       
        data = {
            'ht' : ht,

                }

        return render(request, self.template_name, data)

class HapusDaftarPesertaKimiaView(SoalKimAccessView):
    
    def get(self, request, id):
        soalkimia = SoalKimia.objects.filter(id=id)
        if soalkimia.exists():
            soalkimia.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            logout(request)
            return redirect('login:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  
