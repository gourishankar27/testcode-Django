from django.conf.urls import url
from dummy.views import index,gotonext

urlpatterns = [
    url(r'^dummy/' , index),
    url(r'^gotonext/', gotonext),
]
