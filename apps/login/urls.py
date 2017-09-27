from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^gosignin$', views.gosignin),
	url(r'^login$', views.login, name = "login"),
	url(r'^goregister$', views.goregister),
	url(r'^register$', views.register),
	url(r'^(?P<user_id>\d+)/success$', views.success, name = 'success'),
  ]