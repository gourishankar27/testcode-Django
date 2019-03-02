from django.conf.urls import url
from django.urls import include,path
from startpage.views import index,gotologin
#from login.views import index

urlpatterns = [
    path('', index, name='index'),
    url(r'^startpage/' , index),
    url(r'^gotologin/' , gotologin),
    #url(r'^login/$', 'views.login', name='login'),
]
