from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from . import views

app_name = 'administration'

urlpatterns = [
    
    url(r'^$', views.index, name='administrations_index'),
]