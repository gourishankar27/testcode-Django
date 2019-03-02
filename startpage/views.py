from django.shortcuts import render
from django.http import HttpResponse
from login.views import index


def index(request):
    return render(request, "startpage/startpage.html")

def gotologin(request):
    return render(request, "login/login.html")

def gotohome(request):
    return render(request, "startpage/startpage.html")

def gotoabout(request):
    return render(request, "startpage/about.html")

def gotodepartments(request):
    return render(request, "startpage/department-single.html")

def gotocontacts(request):
    return render(request, "startpage/contact.html")
