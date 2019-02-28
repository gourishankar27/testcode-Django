from django.conf.urls import url
from administration.views import index

urlpatterns = [
    url(r'^administration/' , index),
]
