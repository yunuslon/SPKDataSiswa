
from django.conf.urls import url
from management.plomba import views

urlpatterns = [
    url (r'^$', views.ListPlombaView.as_view(), name='view'),
	url(r'^simpan/$', views.SavePlombaView.as_view(), name='simpan'),
	url(r'^edit/(?P<id>\d+)$', views.EditPlombaView.as_view(), name='edit'),
	url(r'^update/$', views.UpdatePlombaView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusPlombaView.as_view(), name='hapus'),

   
]