
from django.shortcuts import render
from .models import login

from django.http import HttpResponse


def index(request):
    return HttpResponse("login page exist here")
    