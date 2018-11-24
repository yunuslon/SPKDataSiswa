from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas
from management.hasil_akhir import helpers
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from library.view import ManagementAccessView

# Create your views here.


class ListMataPelajaranView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/index.html'
     
        return render(request, template)

class ListBiologiView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/biologi.html'
        sw = Siswa.objects.all()
        nl = helpers.Matrix_DataAwalBio(sw).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpers.Matrix_TernormalisasiBio(sw).as_matrix(),
            'pembobotan': helpers.Matrix_PembobotanBio(sw).as_matrix(),
            'akhir': helpers.Hasil_AkhirBio(sw).as_matrix(),

        }
        return render(request, template, data)

class ListFisikaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/fisika.html'
        sw = Siswa.objects.all()
        nl = helpers.Matrix_DataAwalFis(sw).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpers.Matrix_TernormalisasiFis(sw).as_matrix(),
            'pembobotan': helpers.Matrix_PembobotanFis(sw).as_matrix(),
            'akhir': helpers.Hasil_AkhirFis(sw).as_matrix(),

        }
        return render(request, template, data)

class ListKimiaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/kimia.html'
        sw = Siswa.objects.all()
        nl = helpers.Matrix_DataAwalKim(sw).as_matrix(),
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpers.Matrix_TernormalisasiKim(sw).as_matrix(),
            'pembobotan': helpers.Matrix_PembobotanKim(sw).as_matrix(),
            'akhir': helpers.Hasil_AkhirKim(sw).as_matrix(),

        }
        return render(request, template, data)

class ListMatematikaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/matematika.html'
        sw = Siswa.objects.all()
        nl = helpers.Matrix_DataAwalMat(sw).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpers.Matrix_TernormalisasiMat(sw).as_matrix(),
            'pembobotan': helpers.Matrix_PembobotanMat(sw).as_matrix(),
            'akhir': helpers.Hasil_AkhirMat(sw).as_matrix(),

        }
        return render(request, template, data)



        # view untuk Report
        
class GeneratePDFtbl(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/reporttbl.html')
        sw = Siswa.objects.all()
        nl = helpers.Matrix_TernormalisasiBio(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/reporttbl.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFnilai_awal(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/reportnilai_awal.html')
        sw = Siswa.objects.all()
        nl = helpers.Matrix_DataAwalBio(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFpembobotan(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/report_pembobotan.html')
        sw = Siswa.objects.all()
        nl = helpers.Matrix_PembobotanBio(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangking(View):
    def get(self, request, *args, **kwargs):
        template = get_template('hasil_akhir/report_rangking.html')
        sw = Siswa.objects.all()
        nl = helpers.Hasil_AkhirBio(sw).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('hasil_akhir/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')