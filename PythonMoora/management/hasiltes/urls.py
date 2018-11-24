
from django.conf.urls import url
from management.hasiltes import views

urlpatterns = [
    url (r'^$', views.ListHasilTesView.as_view(), name='view'),
    url(r'^simpan/$', views.SaveHasilTesView.as_view(), name='simpan'),
	url(r'^edit/(?P<id>\d+)$', views.EditHasilTesView.as_view(), name='edit'),
	url(r'^update/$', views.UpdateHasilTesView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusHasilTesView.as_view(), name='hapus'),


]