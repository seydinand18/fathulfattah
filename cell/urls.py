from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name="home_cell"),
    url(r'^detail/(?P<id>[0-9]+)', views.detail_cell, name="detail_cell"),
    url(r'^new', views.new_cell, name="new_cell"),
    url(r'^edit/(?P<id>[0-9]+)', views.edit_cell, name="edit_cell"),
    url(r'^delete/(?P<id>[0-9]+)', views.delete_cell, name="delete_cell"),
]
