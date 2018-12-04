from django.conf.urls import url
from guru import views


urlpatterns = [

# Biologi
    url (r'^$', views.ListSoalOlimpiadeBioView.as_view(), name='view'),
    url (r'^addbio$', views.AddSoalBioView.as_view(), name='addbio'),
    url (r'^savebio$', views.SaveBiologiView.as_view(), name='savebio'),
    url (r'^editbio/(?P<id>\d+)$', views.UbahBioView.as_view(), name='editbio'),
    url (r'^updatebio/(?P<id>\d+)$', views.UpdateBioView.as_view(), name='updatebio'),
    url (r'^detailbio/(?P<id>\d+)$', views.DetailBiologiView.as_view(), name='detailbio'),
    url(r'^hapusbio/(?P<id>\d+)$', views.HapusBiologiView.as_view(), name='hapusbio'),

# Fisika
    url (r'^fisika$', views.ListSoalOlimpiadeFisView.as_view(), name='fisika'),
    url (r'^addfis$', views.AddSoalFisView.as_view(), name='addfis'),
    url (r'^savefis$', views.SaveFisikaView.as_view(), name='savefis'),
    url (r'^editfis/(?P<id>\d+)$', views.UbahFisView.as_view(), name='editfis'),
    url (r'^updatefis/(?P<id>\d+)$', views.UpdateFisView.as_view(), name='updatefis'),
    url (r'^detailfis/(?P<id>\d+)$', views.DetailFisikaView.as_view(), name='detailfis'),
    url(r'^hapusfis/(?P<id>\d+)$', views.HapusFisikaView.as_view(), name='hapusfis'),

# Kimia
    url (r'^kimia$', views.ListSoalOlimpiadeKimView.as_view(), name='kimia'),
    url (r'^addkim$', views.AddSoalKimView.as_view(), name='addkim'),
    url (r'^savekim$', views.SaveKimiaView.as_view(), name='savekim'),
    url (r'^editkim/(?P<id>\d+)$', views.UbahKimView.as_view(), name='editkim'),
    url (r'^updatekim/(?P<id>\d+)$', views.UpdateKimView.as_view(), name='updatekim'),
    url (r'^detailkim/(?P<id>\d+)$', views.DetailKimiaView.as_view(), name='detailkim'),
    url (r'^hapuskim/(?P<id>\d+)$', views.HapusKimiaView.as_view(), name='hapuskim'),

# Matematika
    url (r'^matematika$', views.ListSoalOlimpiadeMatView.as_view(), name='matematika'),
    url (r'^addmat$', views.AddSoalMatView.as_view(), name='addmat'),
    url (r'^savemat$', views.SaveMatematikaView.as_view(), name='savemat'),
    url (r'^editmat/(?P<id>\d+)$', views.UbahMatView.as_view(), name='editmat'),
    url (r'^updatemat/(?P<id>\d+)$', views.UpdateMatView.as_view(), name='updatemat'),
    url (r'^detailmat/(?P<id>\d+)$', views.DetailMatematikaView.as_view(), name='detailmat'),
    url(r'^hapusmat/(?P<id>\d+)$', views.HapusMatematikaView.as_view(), name='hapusmat'),
 
]