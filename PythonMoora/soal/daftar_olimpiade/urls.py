
from django.conf.urls import url
from soal.daftar_olimpiade import views

urlpatterns = [
	url (r'^$', views.ListDaftarView.as_view(), name='view'),
	url(r'^simpanbio/$', views.SaveDaftarBiologiView.as_view(), name='simpanbio'),
	url(r'^simpanfis/$', views.SaveDaftarFisikaView.as_view(), name='simpanfis'),
	url(r'^simpankim/$', views.SaveDaftarKimiaView.as_view(), name='simpankim'),
	url(r'^simpanmat/$', views.SaveDaftarMatematikaView.as_view(), name='simpanmat'),
	
	url(r'^hapusbio/(?P<id>\d+)$', views.HapusBiologiView.as_view(), name='hapusbio'),
	url(r'^hapuskim/(?P<id>\d+)$', views.HapusKimiaView.as_view(), name='hapuskim'),
	url(r'^hapusfis/(?P<id>\d+)$', views.HapusFisikaView.as_view(), name='hapusfis'),
	url(r'^hapusmat/(?P<id>\d+)$', views.HapusMatematikaView.as_view(), name='hapusmat'),


	]