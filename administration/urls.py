from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include
from django.conf.urls import url
from administration.views import index,createDoctor,createReceptionist, gotocreatedoctor ,gotocreatereceptionist,email, sendmail,download_csv_data,upload_csv



urlpatterns = [
    #url(r'^$', sample),
    url(r'^administration/$', index),
    url(r'^createDoctor/', createDoctor),
    url(r'^createReceptionist/', createReceptionist),
    url(r'^gotocreatedoctor/', gotocreatedoctor),
    url(r'^gotocreatereceptionist/',gotocreatereceptionist),
    url(r'^email/',email),
    url(r'^sendmail/',sendmail),
    url(r'^downloadCSV/',download_csv_data),
    url(r'^upload/', upload_csv),

]