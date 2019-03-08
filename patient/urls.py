from django.conf.urls import url
from patient.views import pat_display, index1

urlpatterns = [
<<<<<<< HEAD
    #url(r'^$', views.pat_diplsay, name="patient"),
    url(r'^patient/' , pat_display),
    url(r'^index_patient', index1),
=======
    #url(r'^$', views.pat_diplsay, name="patient1"),
    url(r'^patient1/' , pat_display),
    url(r'^index_patient', index),
>>>>>>> 6d2fb7e5b89dbf801483c37c2a629902d31c4472
]