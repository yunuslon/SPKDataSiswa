from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import TesOlimpiade,HasilTes
from soal.soalmatematika import helpers
from soal.soalmatematika.forms import HasilTesForm
from library.view import SoalMatAccessView



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
        return redirect('/soalkimia/')
