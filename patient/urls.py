from django.conf.urls import url
from patient.views import pat_display, index

urlpatterns = [
    #url(r'^$', views.pat_diplsay, name="patient"),
    url(r'^patient/' , pat_display),
    url(r'^index_patient', index),
]