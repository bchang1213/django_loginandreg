from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^gosignin$', views.gosignin),
	url(r'^login$', views.login, name = "login"),
	url(r'^goregister$', views.goregister),
	url(r'^register$', views.register),
	url(r'^dashboard$', views.dashboard),
	url(r'^addnewuser$', views.addnewuser),
	url(r'^(?P<user_id>\d+)/messages$', views.messages),
	url(r'^(?P<user_id>\d+)$', views.show, name = 'users'),
	# url(r'^(?P<user_id>\d+)/success$', views.success, name = 'success'),
  ]