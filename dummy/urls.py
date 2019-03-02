from django.conf.urls import url
from dummy.views import index,gotonext, gotologinnew

urlpatterns = [
    url(r'^dummy/', index),
    url(r'^gotonext/', gotonext),
    url(r'^gotologinnew/', gotologinnew),

]
