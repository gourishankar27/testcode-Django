from django.conf.urls import url
from django.urls import include,path
from login.views import index,loginusers

urlpatterns = [
    url(r'^loginusers/', loginusers),
    url(r'^login/' , index),
]
