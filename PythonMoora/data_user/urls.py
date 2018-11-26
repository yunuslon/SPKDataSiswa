from django.conf.urls import url
from data_user import views

urlpatterns = [
    url (r'^$', views.ListUserView.as_view(), name='view'),
	url(r'^simpan/$', views.SaveDataUserView.as_view(), name='simpan'),
	# url(r'^edit/(?P<id>\d+)$', views.EditSiswaView.as_view(), name='edit'),
	# url(r'^update/$', views.UpdateSiswaView.as_view(), name='update'),
	# url(r'^hapus/(?P<id>\d+)$', views.HapusSiswaView.as_view(), name='hapus'),
]