from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from administration.views import index,createDoctor,createReceptionist

urlpatterns = [
    url(r'^administration/', index),
    
]