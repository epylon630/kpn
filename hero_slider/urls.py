"""URLs for the ``hero_slider`` app."""
from django.conf.urls import url

from .views import GetCTypeDetails

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'ctype/$', GetCTypeDetails.as_view(), name='get_ctype_details'),
]
