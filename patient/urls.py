from django.conf.urls import url
from patient.views import pat_display, index

urlpatterns = [
    #url(r'^$', views.pat_diplsay, name="patient1"),
    url(r'^patient1/' , pat_display),
    url(r'^index_patient', index),
]