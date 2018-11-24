from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas,TesOlimpiade
from soal.tesolimpiade.forms import TesOlimpiadeForm
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from library.view import ManagementAccessView

# Create your views here.


class ListSoalOlimpiadeBioView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/index.html'
        soalbio = TesOlimpiade.objects.all().filter(mata_pelajaran='biologi')
        data = {
            'soalbio' : soalbio,
          
        }
        return render(request, template, data)

class ListSoalOlimpiadeFisView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/fisika.html'
        soalfis = TesOlimpiade.objects.all().filter(mata_pelajaran='fisika')
        data = {
            'soalfis' : soalfis,
          
        }
        return render(request, template, data)

class ListSoalOlimpiadeKimView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/kimia.html'
        soalkim = TesOlimpiade.objects.all().filter(mata_pelajaran='kimia')
        data = {
            'soalkim' : soalkim,
          
        }
        return render(request, template, data)
        
class ListSoalOlimpiadeMatView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/matematika.html'
        soalmat = TesOlimpiade.objects.all().filter(mata_pelajaran='matematika')
        data = {
            'soalmat' : soalmat,
          
        }
        return render(request, template, data)

class HapusBiologiView(ManagementAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('tesolimpiade:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusFisikaView(ManagementAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('tesolimpiade:fisika')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusKimiaView(ManagementAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('tesolimpiade:kimia')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusMatematikaView(ManagementAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('tesolimpiade:matematika')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class DetailBiologiView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/detailbio.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveBiologiView(ManagementAccessView):
    def post(self, request):
        form = TesOlimpiadeForm(request.POST or None, request.FILES)

        if form.is_valid():
            tesolimpiade = TesOlimpiade()
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.gambar = form.cleaned_data['gambar']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            tesolimpiade.save()
            return redirect('tesolimpiade:view')
        else:
            return HttpResponse(form.errors)

class AddSoalBioView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/addbio.html'
        return render(request, template)

class UbahBioView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/ubahbio.html'
        data = {
            'soalbio': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateBioView(ManagementAccessView):
    def post(self, request, id):
        tesolimpiade = TesOlimpiade.objects.get(id=id)
        form = TesOlimpiadeForm(request.POST, request.FILES)
        if form.is_valid():
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            newpic = form.cleaned_data.get('gambar', None)

            if not newpic == None:
                    tesolimpiade.gambar = newpic
                    
            tesolimpiade.save(force_update=True)
            
            return redirect('tesolimpiade:view')
        else:
            return HttpResponse(form.errors)

class DetailFisikaView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/detailfis.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveFisikaView(ManagementAccessView):
    def post(self, request):
        form = TesOlimpiadeForm(request.POST or None, request.FILES)

        if form.is_valid():
            tesolimpiade = TesOlimpiade()
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.gambar = form.cleaned_data['gambar']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            tesolimpiade.save()
            return redirect('tesolimpiade:fisika')
        else:
            return HttpResponse(form.errors)

class AddSoalFisView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/addfis.html'
        return render(request, template)

class UbahFisView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/ubahfis.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateFisView(ManagementAccessView):
    def post(self, request, id):
        tesolimpiade = TesOlimpiade.objects.get(id=id)
        form = TesOlimpiadeForm(request.POST, request.FILES)
        if form.is_valid():
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            newpic = form.cleaned_data.get('gambar', None)

            if not newpic == None:
                    tesolimpiade.gambar = newpic
                    
            tesolimpiade.save(force_update=True)
            
            return redirect('tesolimpiade:fisika')
        else:
            return HttpResponse(form.errors)

class DetailKimiaView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/detailkim.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveKimiaView(ManagementAccessView):
    def post(self, request):
        form = TesOlimpiadeForm(request.POST or None, request.FILES)

        if form.is_valid():
            tesolimpiade = TesOlimpiade()
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.gambar = form.cleaned_data['gambar']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            tesolimpiade.save()
            return redirect('tesolimpiade:kimia')
        else:
            return HttpResponse(form.errors)

class AddSoalKimView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/addkim.html'
        return render(request, template)

class UbahKimView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/ubahkim.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateKimView(ManagementAccessView):
    def post(self, request, id):
        tesolimpiade = TesOlimpiade.objects.get(id=id)
        form = TesOlimpiadeForm(request.POST, request.FILES)
        if form.is_valid():
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            newpic = form.cleaned_data.get('gambar', None)

            if not newpic == None:
                    tesolimpiade.gambar = newpic
                    
            tesolimpiade.save(force_update=True)
            
            return redirect('tesolimpiade:kimia')
        else:
            return HttpResponse(form.errors)

class DetailMatematikaView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/detailmat.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveMatematikaView(ManagementAccessView):
    def post(self, request):
        form = TesOlimpiadeForm(request.POST or None, request.FILES)

        if form.is_valid():
            tesolimpiade = TesOlimpiade()
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.gambar = form.cleaned_data['gambar']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            tesolimpiade.save()
            return redirect('tesolimpiade:matematika')
        else:
            return HttpResponse(form.errors)

class AddSoalMatView(ManagementAccessView):
    def get(self, request):
        template = 'tesolimpiade/addmat.html'
        return render(request, template)

class UbahMatView(ManagementAccessView):
    def get(self, request, id):
        template = 'tesolimpiade/ubahmat.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateMatView(ManagementAccessView):
    def post(self, request, id):
        tesolimpiade = TesOlimpiade.objects.get(id=id)
        form = TesOlimpiadeForm(request.POST, request.FILES)
        if form.is_valid():
            tesolimpiade.mata_pelajaran = form.cleaned_data['mata_pelajaran']
            tesolimpiade.no = form.cleaned_data['no']
            tesolimpiade.pertayaan = form.cleaned_data['pertayaan']
            tesolimpiade.jawabanA = form.cleaned_data['jawabanA']
            tesolimpiade.jawabanB = form.cleaned_data['jawabanB']
            tesolimpiade.jawabanC = form.cleaned_data['jawabanC']
            tesolimpiade.jawabanD = form.cleaned_data['jawabanD']
            tesolimpiade.jawabanE = form.cleaned_data['jawabanE']
            tesolimpiade.kunci = form.cleaned_data['kunci']
            newpic = form.cleaned_data.get('gambar', None)

            if not newpic == None:
                    tesolimpiade.gambar = newpic
                    
            tesolimpiade.save(force_update=True)
            
            return redirect('tesolimpiade:matematika')
        else:
            return HttpResponse(form.errors)


