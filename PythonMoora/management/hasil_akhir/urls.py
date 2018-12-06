from django.conf.urls import url
from management.hasil_akhir import views

urlpatterns = [
    url (r'^$', views.ListMataPelajaranView.as_view(), name='view'),
    url (r'^fisika$', views.ListFisikaView.as_view(), name='fisika'),
    url (r'^biologi$', views.ListBiologiView.as_view(), name='biologi'),
    url (r'^kimia$', views.ListKimiaView.as_view(), name='kimia'),
    url (r'^matematika$', views.ListMatematikaView.as_view(), name='matematika'),
   

    # Report Biologi
    url (r'^reportdata_awal$', views.GeneratePDFnilai_awal.as_view(), name='reportdata_awal'),
    url (r'^report_ternormalisasi$', views.GeneratePDFternormalisasi.as_view(), name='report_ternormalisasi'),
    url (r'^report_pembobotan$', views.GeneratePDFpembobotan.as_view(), name='report_pembobotan'),
    url (r'^report_rangking$', views.GeneratePDFrangking.as_view(), name='report_rangking'),

    # Report Fisika
    url (r'^reportdata_awalfis$', views.GeneratePDFnilai_awalFis.as_view(), name='reportdata_awalfis'),
    url (r'^report_ternormalisasifis$', views.GeneratePDFternormalisasiFis.as_view(), name='report_ternormalisasifis'),
    url (r'^report_pembobotanfis$', views.GeneratePDFpembobotanFis.as_view(), name='report_pembobotanfis'),
    url (r'^report_rangkingfis$', views.GeneratePDFrangkingFis.as_view(), name='report_rangkingfis'),

    # Report Kimia
    url (r'^reportdata_awalkim$', views.GeneratePDFnilai_awalKim.as_view(), name='reportdata_awalkim'),
    url (r'^report_ternormalisasikim$', views.GeneratePDFternormalisasiKim.as_view(), name='report_ternormalisasikim'),
    url (r'^report_pembobotankim$', views.GeneratePDFpembobotanKim.as_view(), name='report_pembobotankim'),
    url (r'^report_rangkingkim$', views.GeneratePDFrangkingKim.as_view(), name='report_rangkingkim'),

    # Report Matematika
    url (r'^reportdata_awalmat$', views.GeneratePDFnilai_awalMat.as_view(), name='reportdata_awalmat'),
    url (r'^report_ternormalisasimat$', views.GeneratePDFternormalisasiMat.as_view(), name='report_ternormalisasimat'),
    url (r'^report_pembobotanmat$', views.GeneratePDFpembobotanMat.as_view(), name='report_pembobotanmat'),
    url (r'^report_rangkingmat$', views.GeneratePDFrangkingMat.as_view(), name='report_rangkingmat'),
]