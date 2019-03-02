from django.shortcuts import render
from django.http import HttpResponse
from login.views import index


def index(request):
    return render(request, "startpage/startpage.html")

def gotologin(request):
    return render(request, "login/login.html")
