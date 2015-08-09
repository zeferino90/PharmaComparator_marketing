__author__ = 'zeferino'

from django.conf.urls import patterns, url
from product import views

urlpatterns = patterns('',
        url(r'^$', views.hello_world, name='hello_world'),
        url(r'^test2/', views.test2, name='test2'))