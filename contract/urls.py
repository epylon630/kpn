from django.conf.urls import url

from . import views

r'^polls/(?P<string>[\w\-]+)/$'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<category>[\w\-]+)/category/$', views.category , name='category'),
    url(r'^(?P<offer_id>[0-9]+)/$', views.detail , name='detail'),
	url(r'^(?P<offer_id>[0-9]+)/items/$', views.item_list , name='item_list'),
    url(r'^(?P<item_id>[0-9]+)/item_detail/$', views.item_detail , name='item_detail'),
]
