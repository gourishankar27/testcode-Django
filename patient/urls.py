from django.conf.urls import url
from patient.views import pat_display, index_patient

urlpatterns = [
    url(r'^index_patient/', index_patient),
    url(r'^display/', pat_display),
]