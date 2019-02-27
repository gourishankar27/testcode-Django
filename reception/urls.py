from django.conf.urls import url
from reception.views import index

urlpatterns = [
    url(r'^reception/' , index),
]
