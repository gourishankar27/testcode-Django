from django.conf.urls import url
from . import views

app_name = 'doctors'

urlpatterns = [
    url(r'^index/signUp/$', views.index, name='index'),
    url(r'^(?P<patient_ID>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_album/$', views.CreatePatient, name='create_patient'),
    url(r'^(?P<patient_ID>[0-9]+)/$', views.UpdatePatient, name='update_patient'),

]
