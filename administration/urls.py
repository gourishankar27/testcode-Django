from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from administration.views import index,createDoctor,createReceptionist


from django.conf.urls import url
from administration.views import index,createDoctor,createReceptionist



urlpatterns = [
    url(r'^administration/', index),
    url(r'^/createDoctor', createDoctor),
    url(r'^/createReceptionist', createReceptionist),


    
]