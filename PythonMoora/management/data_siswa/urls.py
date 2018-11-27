from django.conf.urls import url
from management.data_siswa import views

urlpatterns = [
    # Biologi
    url (r'^view$', views.ListDataSiswaBiologiView.as_view(), name='view'),
    url (r'^save_data_siswabio$', views.SaveDataSiswaBioView.as_view(), name='save_data_siswabio'),
    url (r'^hapus_data_siswabio/(?P<id>\d+)$', views.HapusDataSiswaBioView.as_view(), name='hapus_data_siswabio'),
    url (r'^detailbio/(?P<id>\d+)$', views.DetailDataSiswaBioView.as_view(), name='detailbio'),
    url (r'^editbio/(?P<id>\d+)$', views.UbahBioView.as_view(), name='editbio'),
    url (r'^updatebio/(?P<id>\d+)$', views.UpdateBioView.as_view(), name='updatebio'),
    url (r'^edituserbio/(?P<id>\d+)$', views.UbahUserBioView.as_view(), name='edituserbio'),
    url (r'^updateuserbio/(?P<id>\d+)$', views.UpdateUserBioView.as_view(), name='updateuserbio'),

    # Fisika
    url (r'^fisika$', views.ListDataSiswaFisikaView.as_view(), name='fisika'),
    url (r'^save_data_siswafis$', views.SaveDataSiswaFisView.as_view(), name='save_data_siswafis'),
    url (r'^hapus_data_siswafis/(?P<id>\d+)$', views.HapusDataSiswaFisView.as_view(), name='hapus_data_siswafis'),
    url (r'^detailfis/(?P<id>\d+)$', views.DetailDataSiswaFisView.as_view(), name='detailfis'),
    url (r'^editfis/(?P<id>\d+)$', views.UbahFisView.as_view(), name='editfis'),
    url (r'^updatefis/(?P<id>\d+)$', views.UpdateFisView.as_view(), name='updatefis'),
    url (r'^edituserfis/(?P<id>\d+)$', views.UbahUserFisView.as_view(), name='edituserfis'),
    url (r'^updateuserfis/(?P<id>\d+)$', views.UpdateUserFisView.as_view(), name='updateuserfis'),

    # Kimia
    url (r'^kimia$', views.ListDataSiswaKimiaView.as_view(), name='kimia'),
    url (r'^save_data_siswakim$', views.SaveDataSiswaKimView.as_view(), name='save_data_siswakim'),
    url (r'^hapus_data_siswakim/(?P<id>\d+)$', views.HapusDataSiswaKimView.as_view(), name='hapus_data_siswakim'),
    url (r'^detailkim/(?P<id>\d+)$', views.DetailDataSiswaKimView.as_view(), name='detailkim'),
    url (r'^editkim/(?P<id>\d+)$', views.UbahKimView.as_view(), name='editkim'),
    url (r'^updatekim/(?P<id>\d+)$', views.UpdateKimView.as_view(), name='updatekim'),
    url (r'^edituserkim/(?P<id>\d+)$', views.UbahUserKimView.as_view(), name='edituserkim'),
    url (r'^updateuserkim/(?P<id>\d+)$', views.UpdateUserKimView.as_view(), name='updateuserkim'),

    # Matematika
    url (r'^matematika$', views.ListDataSiswaMatematikaView.as_view(), name='matematika'),
    url (r'^save_data_siswamat$', views.SaveDataSiswaMatView.as_view(), name='save_data_siswamat'),
    url (r'^hapus_data_siswamat/(?P<id>\d+)$', views.HapusDataSiswaMatView.as_view(), name='hapus_data_siswamat'),
    url (r'^detailmat/(?P<id>\d+)$', views.DetailDataSiswaMatView.as_view(), name='detailmat'),
    url (r'^editmat/(?P<id>\d+)$', views.UbahMatView.as_view(), name='editmat'),
    url (r'^updatemat/(?P<id>\d+)$', views.UpdateMatView.as_view(), name='updatemat'),
    url (r'^editusermat/(?P<id>\d+)$', views.UbahUserMatView.as_view(), name='editusermat'),
    url (r'^updateusermat/(?P<id>\d+)$', views.UpdateUserMatView.as_view(), name='updateusermat'),

]