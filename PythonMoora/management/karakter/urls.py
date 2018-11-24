
from django.conf.urls import url
from management.karakter import views

urlpatterns = [
    url (r'^$', views.ListKarakterView.as_view(), name='view'),
    url(r'^edit/(?P<id>\d+)$', views.EditKarakterView.as_view(), name='edit'),
	url(r'^simpan/$', views.SaveKarakterView.as_view(), name='simpan'),
	url(r'^update/$', views.UpdateKarakterView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusKarakterView.as_view(), name='hapus'),

]