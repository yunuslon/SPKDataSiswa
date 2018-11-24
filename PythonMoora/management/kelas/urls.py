
from django.conf.urls import url
from management.kelas import views

urlpatterns = [
	url (r'^$', views.ListKelasView.as_view(), name='view'),
	url(r'^simpan/$', views.SaveKelasView.as_view(), name='simpan'),
	url(r'^edit/(?P<id>\d+)$', views.EditKelasView.as_view(), name='edit'),
	url(r'^update/$', views.UpdateKelasView.as_view(), name='update'),
	# url (r'^update/(?P<pk>\d+)$', views.UpdateKelasView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusKelasView.as_view(), name='hapus'),


	]