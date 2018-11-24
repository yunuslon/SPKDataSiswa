
from django.conf.urls import url
from management.bobot import views

urlpatterns = [
	url (r'^$', views.ListBobotView.as_view(), name='view'),
	url(r'^edit/(?P<id>\d+)$', views.EditBobotView.as_view(), name='edit'),
	url(r'^update/$', views.UpdateBobotView.as_view(), name='update'),


	]