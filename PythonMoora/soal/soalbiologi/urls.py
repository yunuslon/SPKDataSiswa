from django.conf.urls import url
from soal.soalbiologi import views

urlpatterns = [
	url (r'^$', views.ListSoalBiologiView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesBioView.as_view(), name='simpan'),


	]