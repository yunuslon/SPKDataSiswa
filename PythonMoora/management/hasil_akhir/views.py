from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Karakter,NilaiAkademik,HasilTes,Siswa,Plomba,Kelas
from management.hasil_akhir import helpers,helpersbio,helpersfis,helperskim,helpersmat
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
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="biologi")
        nl = helpersbio.Matrix_DataAwalBio(na).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpersbio.Matrix_TernormalisasiBio(na).as_matrix(),
            'pembobotan': helpersbio.Matrix_PembobotanBio(na).as_matrix(),
            'akhir': helpersbio.Hasil_AkhirBio(na).as_matrix(),

        }
        return render(request, template, data)

class ListFisikaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/fisika.html'
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="fisika")
        nl = helpersfis.Matrix_DataAwalFis(na).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpersfis.Matrix_TernormalisasiFis(na).as_matrix(),
            'pembobotan': helpersfis.Matrix_PembobotanFis(na).as_matrix(),
            'akhir': helpersfis.Hasil_AkhirFis(na).as_matrix(),

        }
        return render(request, template, data)

class ListKimiaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/kimia.html'
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="kimia")
        nl = helperskim.Matrix_DataAwalKim(na).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helperskim.Matrix_TernormalisasiKim(na).as_matrix(),
            'pembobotan': helperskim.Matrix_PembobotanKim(na).as_matrix(),
            'akhir': helperskim.Hasil_AkhirKim(na).as_matrix(),

        }
        return render(request, template, data)

class ListMatematikaView(ManagementAccessView):
    def get(self, request):
        template = 'hasil_akhir/matematika.html'
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="matematika")
        nl = helpersmat.Matrix_DataAwalMat(na).as_matrix()
        data = {
            'data_awal' : nl,
            'ternormalisasi': helpersmat.Matrix_TernormalisasiMat(na).as_matrix(),
            'pembobotan': helpersmat.Matrix_PembobotanMat(na).as_matrix(),
            'akhir': helpersmat.Hasil_AkhirMat(na).as_matrix(),

        }
        return render(request, template, data)



############################################ view untuk Report Biologi ###################################################
############################################ view untuk Report Biologi ###################################################
############################################ view untuk Report Biologi ###################################################
        
class GeneratePDFnilai_awal(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/biologi/reportnilai_awal.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="biologi")
        nl = helpersbio.Matrix_DataAwalBio(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/biologi/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFternormalisasi(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/biologi/report_ternormalisasi.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="biologi")
        nl = helpersbio.Matrix_TernormalisasiBio(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/biologi/report_ternormalisasi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDFpembobotan(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/biologi/report_pembobotan.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="biologi")
        nl = helpersbio.Matrix_PembobotanBio(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/biologi/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangking(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/biologi/report_rangking.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="biologi")
        nl = helpersbio.Hasil_AkhirBio(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/biologi/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

############################################ view untuk Report fisika ###################################################
############################################ view untuk Report fisika ###################################################
############################################ view untuk Report fisika ###################################################
        
class GeneratePDFnilai_awalFis(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/fisika/reportnilai_awal.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="fisika")
        nl = helpersfis.Matrix_DataAwalFis(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/fisika/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFternormalisasiFis(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/fisika/report_ternormalisasi.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="fisika")
        nl = helpersfis.Matrix_TernormalisasiFis(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/fisika/report_ternormalisasi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDFpembobotanFis(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/fisika/report_pembobotan.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="fisika")
        nl = helpersfis.Matrix_PembobotanFis(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/fisika/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangkingFis(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/fisika/report_rangking.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="fisika")
        nl = helpersfis.Hasil_AkhirFis(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/fisika/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

############################################ view untuk Report kimia ###################################################
############################################ view untuk Report kimia ###################################################
############################################ view untuk Report kimia ###################################################
        
class GeneratePDFnilai_awalKim(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/kimia/reportnilai_awal.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="kimia")
        nl = helperskim.Matrix_DataAwalKim(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/kimia/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFternormalisasiKim(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/kimia/report_ternormalisasi.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="kimia")
        nl = helperskim.Matrix_TernormalisasiKim(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/kimia/report_ternormalisasi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDFpembobotanKim(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/kimia/report_pembobotan.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="kimia")
        nl = helperskim.Matrix_PembobotanKim(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/kimia/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangkingKim(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/kimia/report_rangking.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="kimia")
        nl = helperskim.Hasil_AkhirKim(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/kimia/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

############################################ view untuk Report matematika ###################################################
############################################ view untuk Report matematika ###################################################
############################################ view untuk Report matematika ###################################################
        
class GeneratePDFnilai_awalMat(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/matematika/reportnilai_awal.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="matematika")
        nl = helpersmat.Matrix_DataAwalMat(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/matematika/reportnilai_awal.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFternormalisasiMat(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/matematika/report_ternormalisasi.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="matematika")
        nl = helpersmat.Matrix_TernormalisasiMat(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/matematika/report_ternormalisasi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDFpembobotanMat(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/matematika/report_pembobotan.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="matematika")
        nl = helpersmat.Matrix_PembobotanMat(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/matematika/report_pembobotan.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDFrangkingMat(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report/matematika/report_rangking.html')
        na = NilaiAkademik.objects.all().filter(mata_pelajaran="matematika")
        nl = helpersmat.Hasil_AkhirMat(na).as_matrix()
        data = {
            'nl' : nl,
        }
        html = template.render(data)
        pdf = helpers.render_to_pdf('report/matematika/report_rangking.html', data)
        return HttpResponse(pdf, content_type='application/pdf')