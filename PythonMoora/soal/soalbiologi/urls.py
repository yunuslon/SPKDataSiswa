from django.conf.urls import url
from soal.soalbiologi import views

urlpatterns = [
	url (r'^$', views.ListSoalBiologiView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesBioView.as_view(), name='simpan'),
    url(r'^hasil/$', views.ListHasilView.as_view(), name='hasil'),
    url(r'^hapus_peserta/(?P<id>\d+)$', views.HapusDaftarPesertaBiologiView.as_view(), name='hapus_peserta'),




	]