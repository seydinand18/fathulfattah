from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='home_member'),
    url(r'^detail/(?P<id>[0-9]+)', views.detail_member, name="detail_member"),
    url(r'^new', views.new_member, name="new_member"),
    url(r'^edit/(?P<id>[0-9]+)', views.edit_member, name="edit_member"),
    url(r'^delete/(?P<id>[0-9]+)', views.delete_member, name="delete_member"),
]
