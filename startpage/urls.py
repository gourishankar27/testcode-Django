from django.conf.urls import url
from django.urls import include,path
from startpage.views import index

urlpatterns = [
    path('', index , name = 'index'),
    url(r'^startpage/' , index),
]

