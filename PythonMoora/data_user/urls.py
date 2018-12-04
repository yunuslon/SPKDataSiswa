from django.conf.urls import url
from data_user import views

urlpatterns = [
    url (r'^$', views.ListUserView.as_view(), name='view'),
	url(r'^simpan/$', views.SaveDataUserView.as_view(), name='simpan'),
	url(r'^edit/(?P<id>\d+)$', views.EditDataUserView.as_view(), name='edit'),
	url(r'^update/$', views.UpdateDataUserView.as_view(), name='update'),
	url(r'^hapus/(?P<id>\d+)$', views.HapusDataUserView.as_view(), name='hapus'),

	# ########################################### Guru ##########################################################
 	url (r'^guru/$', views.ListUserGuruView.as_view(), name='guru'),
	url(r'^simpan_guru/$', views.SaveDataUserGuruView.as_view(), name='simpan_guru'),
	url(r'^edit_guru/(?P<id>\d+)$', views.EditDataUserGuruView.as_view(), name='edit_guru'),
	url(r'^update_guru/$', views.UpdateDataUserGuruView.as_view(), name='update_guru'),
	url(r'^hapus_guru/(?P<id>\d+)$', views.HapusDataUserGuruView.as_view(), name='hapus_guru'),


]