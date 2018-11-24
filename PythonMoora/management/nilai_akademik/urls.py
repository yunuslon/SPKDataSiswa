from django.conf.urls import url
from management.nilai_akademik import views

urlpatterns = [
    url (r'^$', views.ListNilaiAkademikView.as_view(), name='view'),
    url(r'^edit/(?P<id>\d+)$', views.EditNilaiAkademikView.as_view(), name='edit'),
	url(r'^simpan/$', views.SaveNilaiAkademikView.as_view(), name='simpan'),
	url(r'^update/$', views.UpdateNilaiAkademikView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusNilaiAkademikView.as_view(), name='hapus'),
    
]
