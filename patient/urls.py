from django.conf.urls import url
from patient.views import pat_display

urlpatterns = [
    #url(r'^$', views.pat_diplsay, name="patient"),
    url(r'^patient/' , pat_display),
]