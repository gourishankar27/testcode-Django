from django.conf.urls import url
from doctors.views import index_doctor,AddCaseView,ViewCaseView,AddCaseViewButton,gotoAddCaseView

#from . import views

app_name = 'doctors'

urlpatterns = [
    url(r'^AddCaseViewButton/', AddCaseViewButton),
    url(r'^index_doctor/', index_doctor),
    url(r'^AddCaseView', AddCaseView),
    url(r'^ViewCaseView/', ViewCaseView),
    url(r'^gotoAddCaseView', gotoAddCaseView),
]
