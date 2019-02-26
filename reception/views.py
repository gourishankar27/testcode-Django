

# Create your views here.

from django.shortcuts import render
from .models import reception

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2> This page belongs to receptionist</h2>")