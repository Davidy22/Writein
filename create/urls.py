from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<ID>[0-9]+)$',views.polling, name = 'poll'),
	url(r'^create/$',views.create, name = 'create'),
]
