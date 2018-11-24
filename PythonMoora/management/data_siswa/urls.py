from django.conf.urls import url
from management.data_siswa import views

urlpatterns = [
    url (r'^view$', views.ListDataSiswaView.as_view(), name='view'),
    url (r'^add_data_siswabio$', views.AddDataSiswaBioView.as_view(), name='add_data_siswabio'),
    url (r'^save_data_siswabio$', views.SaveDataSiswaBioView.as_view(), name='save_data_siswabio'),
    url(r'^hapus_data_siswabio/(?P<id>\d+)$', views.HapusDataSiswaBioView.as_view(), name='hapus_data_siswabio'),
    url (r'^biologi$', views.ListDataSiswaBiologiView.as_view(), name='biologi'),


]