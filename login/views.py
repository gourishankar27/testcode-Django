
from django.shortcuts import render
from .models import login
from django.http import HttpResponse


def index(request):
    return render(request, "login/login.html")
    