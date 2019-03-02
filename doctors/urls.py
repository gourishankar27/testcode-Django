from django.conf.urls import url
#from . import views


app_name = 'doctors'

#urlpatterns = [
    #path(r'^$', views.index, name='doctors_index'),
    #url(r'^$', views.index, name='doctors_index'),
    # url(r'^add_(?P<patient_ID>[0-9]+)/$', views.AddCaseView, name='add_case'),
    #url(r'^view_(?P<patient_ID>[0-9]+)/$', views.ViewCaseView, name='view_case'),
    #url(r'^ad_(?P<patient_ID>[0-9]+)/$', views.det, name='append_case'),
#]

#from django.conf.urls import url
<<<<<<< HEAD
from user.views import index_doctor,AddCaseView,ViewCaseView,AddCaseViewButton
=======
from doctors.views import index,AddCaseView
>>>>>>> 24458e7dae47b88556b0d13c4ced327b7b0d29d5

urlpatterns = [
    url(r'^AddCaseViewButton/', AddCaseViewButton),
    url(r'^index_doctor/', index_doctor),
    url(r'^AddCaseView/', AddCaseView),
    #url(r'^ViewCaseView/', ViewCaseView),


]
