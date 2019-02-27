from django.conf.urls import url
from login.views import index

urlpatterns = [
    url(r'^login/' , index),
]
