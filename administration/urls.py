from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from django.conf.urls import url
from administration.views import index,createDoctor,createReceptionist,gotocreatedoctor, gotocreatereceptionist



urlpatterns = [
    #url(r'^$', sample),
    url(r'^administration/$', index),
    url(r'^createDoctor/$', createDoctor),
    url(r'^administration/createReceptionist/', createReceptionist),
    url(r'^gotocreatedoctor/',gotocreatedoctor),
    url(r'^gotocreatereceptionist/',gotocreatereceptionist),
]