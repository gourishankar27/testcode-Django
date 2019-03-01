from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from administration.views import createDoctor,createReceptionist

urlpatterns = [
    url(r'^administration/', createDoctor),
    url(r'^creatreceptionist/', createReceptionist),
    
]