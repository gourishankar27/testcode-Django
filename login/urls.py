from django.conf.urls import url
from django.urls import include,path
from login.views import index

urlpatterns = [
    path('', index, name='index'),
    url(r'^login/' , index),
]
