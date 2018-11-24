from django.conf.urls import url
from soal.soalfisika import views

urlpatterns = [
	url (r'^$', views.ListSoalFisikaView.as_view(), name='view'),
    url(r'^simpan/$', views.SimpanHasilTesFisView.as_view(), name='simpan'),


	]