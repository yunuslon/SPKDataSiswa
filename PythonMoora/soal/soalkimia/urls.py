from django.conf.urls import url
from soal.soalkimia import views

urlpatterns = [
	url (r'^$', views.ListSoalKimiaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesKimView.as_view(), name='simpan'),
	url(r'^hasil/$', views.ListHasilView.as_view(), name='hasil'),
    url(r'^hapus_peserta/(?P<id>\d+)$', views.HapusDaftarPesertaKimiaView.as_view(), name='hapus_peserta'),

	]