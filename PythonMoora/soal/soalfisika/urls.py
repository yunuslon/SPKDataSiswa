from django.conf.urls import url
from soal.soalfisika import views

urlpatterns = [
	url (r'^$', views.ListSoalFisikaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesFisView.as_view(), name='simpan'),
	url(r'^hasil/$', views.ListHasilView.as_view(), name='hasil'),
    url(r'^hapus_peserta/(?P<id>\d+)$', views.HapusDaftarPesertaFisikaView.as_view(), name='hapus_peserta'),
	]