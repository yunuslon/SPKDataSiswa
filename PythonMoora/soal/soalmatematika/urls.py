from django.conf.urls import url
from soal.soalmatematika import views

urlpatterns = [
	url (r'^$', views.ListSoalMatematikaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesMatView.as_view(), name='simpan'),


	]