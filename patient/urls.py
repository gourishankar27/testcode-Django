from django.conf.urls import url
<<<<<<< HEAD
from patient.views import pat_display, index_patient

urlpatterns = [
    url(r'^index_patient/', index_patient),
    url(r'^display/', pat_display),
=======
from patient.views import pat_display

urlpatterns = [
    #url(r'^$', views.pat_diplsay, name="patient"),
    url(r'^patient/' , pat_display),
>>>>>>> dd067ab97bb35df4132889c1e40ee5f78ace446d
]