from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.pat_diplsay, name="patient"),
]