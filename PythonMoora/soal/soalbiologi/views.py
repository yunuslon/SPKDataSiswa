from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import SoalBiologi,TesOlimpiade,HasilTes
from soal.soalbiologi import helpers
from soal.soalbiologi.forms import HasilTesForm
from library.view import SoalBioAccessView
from django.contrib.auth import authenticate, login, logout




class ListSoalBiologiView(SoalBioAccessView):
    template_name = 'soalbiologi/index.html'
      

    def get(self, request):
        tp = TesOlimpiade.objects.all()
        tesolimpiade = helpers.SleksiSoalBio(tp).as_matrix()
       
        data = {
        'tesolimpiade2' : tesolimpiade,
        'tesolimpiade': {
               'total': len(tesolimpiade)
                # 'email':

                },

                }

        return render(request, self.template_name, data)

class SimpanHasilTesBioView(SoalBioAccessView):
    template_name = 'soalbiologi/index.html'

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
            return redirect('soalbiologi:hasil')

class ListHasilView(SoalBioAccessView):
    template_name = 'soalbiologi/hasil.html'
      

    def get(self, request):
        ht = HasilTes.objects.all()
       
        data = {
            'ht' : ht,

                }

        return render(request, self.template_name, data)

class HapusDaftarPesertaBiologiView(SoalBioAccessView):
    
    def get(self, request, id):
        soalbiologi = SoalBiologi.objects.filter(id=id)
        if soalbiologi.exists():
            soalbiologi.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            logout(request)
            return redirect('login:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')  

