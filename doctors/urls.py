from django.conf.urls import url
from . import views


app_name = 'doctors'

urlpatterns = [
    #path(r'^$', views.index, name='doctors_index'),
    url(r'^$', views.index, name='doctors_index'),
    # url(r'^add_(?P<patient_ID>[0-9]+)/$', views.AddCaseView, name='add_case'),
    #url(r'^view_(?P<patient_ID>[0-9]+)/$', views.ViewCaseView, name='view_case'),
    #url(r'^ad_(?P<patient_ID>[0-9]+)/$', views.det, name='append_case'),
]
