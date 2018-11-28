from django.conf.urls import url
from soal.soalmatematika import views

urlpatterns = [
	url (r'^$', views.ListSoalMatematikaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesMatView.as_view(), name='simpan'),
url(r'^hasil/$', views.ListHasilView.as_view(), name='hasil'),
    url(r'^hapus_peserta/(?P<id>\d+)$', views.HapusDaftarPesertaMatematikaView.as_view(), name='hapus_peserta'),

	]