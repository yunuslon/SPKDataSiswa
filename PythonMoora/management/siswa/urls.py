
from django.conf.urls import url
from management.siswa import views

urlpatterns = [
    url (r'^$', views.ListSiswaView.as_view(), name='view'),
	url(r'^simpan/$', views.SaveSiswaView.as_view(), name='simpan'),
	url(r'^edit/(?P<id>\d+)$', views.EditSiswaView.as_view(), name='edit'),
	url(r'^update/$', views.UpdateSiswaView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusSiswaView.as_view(), name='hapus'),
]