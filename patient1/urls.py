from django.conf.urls import url
from patient1.views import index_patient, ShowPatient, gotoOnePatient, OnePatient, pat_display, gotopatient1

urlpatterns = [
    url(r'^index_patient', index_patient),
    url(r'^patient1/', ShowPatient),
    url(r'^gotoOnePatient', gotoOnePatient),
    url(r'^OnePatient/', OnePatient),
    url(r'^/pat_display', pat_display),
    url(r'^gotopatient1', gotopatient1),
]