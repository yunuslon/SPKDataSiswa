from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas,TesOlimpiade
from guru.forms import TesOlimpiadeForm,UserForm
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from library.view import  GuruAccessView
from django.contrib.auth.models import User, Group


# Create your views here.
class UpdateAkunView(GuruAccessView):
    def post(self, request, id):
        user_form = UserForm(request.POST, request.FILES)

        if user_form.is_valid():
            user = User.objects.get(id=id)
            user.username = user_form.cleaned_data['username']
            user.last_name = user_form.cleaned_data['last_name']
            user.set_password(user_form.cleaned_data['password']) 
            user.save()
           
            messages.add_message(request, messages.INFO, 'Data Akun Berhasil Diupdate')  

            return redirect('guru:user')
        else:
            return HttpResponse(user_form.errors)

class DataAkunView(GuruAccessView):
    def get(self, request):
        template = 'guru/user.html'
       
        return render(request, template)

class ListSoalOlimpiadeBioView(GuruAccessView):
    def get(self, request):
        template = 'guru/index.html'
        soalbio = TesOlimpiade.objects.all().filter(mata_pelajaran='biologi')
        data = {
            'soalbio' : soalbio,
          
        }
        return render(request, template, data)

class ListSoalOlimpiadeFisView(GuruAccessView):
    def get(self, request):
        template = 'guru/fisika.html'
        soalfis = TesOlimpiade.objects.all().filter(mata_pelajaran='fisika')
        data = {
            'soalfis' : soalfis,
          
        }
        return render(request, template, data)

class ListSoalOlimpiadeKimView(GuruAccessView):
    def get(self, request):
        template = 'guru/kimia.html'
        soalkim = TesOlimpiade.objects.all().filter(mata_pelajaran='kimia')
        data = {
            'soalkim' : soalkim,
          
        }
        return render(request, template, data)
        
class ListSoalOlimpiadeMatView(GuruAccessView):
    def get(self, request):
        template = 'guru/matematika.html'
        soalmat = TesOlimpiade.objects.all().filter(mata_pelajaran='matematika')
        data = {
            'soalmat' : soalmat,
          
        }
        return render(request, template, data)

class HapusBiologiView(GuruAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('guru:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusFisikaView(GuruAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('guru:fisika')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusKimiaView(GuruAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('guru:kimia')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')      

class HapusMatematikaView(GuruAccessView):
    
    def get(self, request, id):
        tesolimpiade = TesOlimpiade.objects.filter(id=id)

        if tesolimpiade.exists():
            tesolimpiade.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('guru:matematika')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class DetailBiologiView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/detailbio.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveBiologiView(GuruAccessView):
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
            return redirect('guru:view')
        else:
            return HttpResponse(form.errors)

class AddSoalBioView(GuruAccessView):
    def get(self, request):
        template = 'guru/addbio.html'
        return render(request, template)

class UbahBioView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/ubahbio.html'
        data = {
            'soalbio': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateBioView(GuruAccessView):
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
            
            return redirect('guru:view')
        else:
            return HttpResponse(form.errors)

class DetailFisikaView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/detailfis.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveFisikaView(GuruAccessView):
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
            return redirect('guru:fisika')
        else:
            return HttpResponse(form.errors)

class AddSoalFisView(GuruAccessView):
    def get(self, request):
        template = 'guru/addfis.html'
        return render(request, template)

class UbahFisView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/ubahfis.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateFisView(GuruAccessView):
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
            
            return redirect('guru:fisika')
        else:
            return HttpResponse(form.errors)

class DetailKimiaView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/detailkim.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveKimiaView(GuruAccessView):
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
            return redirect('guru:kimia')
        else:
            return HttpResponse(form.errors)

class AddSoalKimView(GuruAccessView):
    def get(self, request):
        template = 'guru/addkim.html'
        return render(request, template)

class UbahKimView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/ubahkim.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateKimView(GuruAccessView):
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
            
            return redirect('guru:kimia')
        else:
            return HttpResponse(form.errors)

class DetailMatematikaView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/detailmat.html'
        data = {
            'detailsoal' : TesOlimpiade.objects.get(id=id)
        }
        return render(request, template, data)


class SaveMatematikaView(GuruAccessView):
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
            return redirect('guru:matematika')
        else:
            return HttpResponse(form.errors)

class AddSoalMatView(GuruAccessView):
    def get(self, request):
        template = 'guru/addmat.html'
        return render(request, template)

class UbahMatView(GuruAccessView):
    def get(self, request, id):
        template = 'guru/ubahmat.html'
        data = {
            'soal': TesOlimpiade.objects.get(id=id),
        }
        return render(request, template, data)

class UpdateMatView(GuruAccessView):
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
            
            return redirect('guru:matematika')
        else:
            return HttpResponse(form.errors)


