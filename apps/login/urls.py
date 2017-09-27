from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^gosignin$', views.gosignin),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^goregister$', views.goregister),
	url(r'^register$', views.register),
	url(r'^dashboard$', views.dashboard),
	url(r'^addnewuser$', views.addnewuser),
	url(r'^(?P<user_id>\d+)/posts$', views.posts),
	url(r'^(?P<user_id>\d+)$', views.show, name = 'users'),
	url(r'^(?P<user_id>\d+)/comments$', views.comments),
	# url(r'^(?P<user_id>\d+)/success$', views.success, name = 'success'),
  ]