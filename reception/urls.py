from django.conf.urls import url
from reception.views import index,createPatient

urlpatterns = [
    url(r'^reception/' , index),
    url(r'^createPatient/', createPatient)
]
