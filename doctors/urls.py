from django.conf.urls import url
from .import views

app_name = 'doctors'

urlpatterns = [
    path(r'^doctorSearch/$', views.index, name='doctors_index'),
    path(r'^add_(?P<patient_ID>[0-9]+)/$', views.detail, name='add_case'),
    path(r'^view_(?P<patient_ID>[0-9]+)/$', views.UpdatePatient, name='append_case'),
    path(r'^add_(?P<patient_ID>[0-9]+)/$', views.detail, name='view_case'),
]
