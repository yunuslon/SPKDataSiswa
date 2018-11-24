from django.conf.urls import url
from management.hasil_akhir import views

urlpatterns = [
    url (r'^$', views.ListMataPelajaranView.as_view(), name='view'),
    url (r'^fisika$', views.ListFisikaView.as_view(), name='fisika'),
    url (r'^biologi$', views.ListBiologiView.as_view(), name='biologi'),
    url (r'^kimia$', views.ListKimiaView.as_view(), name='kimia'),
    url (r'^matematika$', views.ListMatematikaView.as_view(), name='matematika'),
   

    # Report
    url (r'^reporttbl$', views.GeneratePDFtbl.as_view(), name='reporttbl'),
    url (r'^reportnilai_awal$', views.GeneratePDFnilai_awal.as_view(), name='reportnilai_awal'),
    url (r'^report_pembobotan$', views.GeneratePDFpembobotan.as_view(), name='report_pembobotan'),
    url (r'^report_rangking$', views.GeneratePDFrangking.as_view(), name='report_rangking'),

]