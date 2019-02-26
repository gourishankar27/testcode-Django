

# Create your views here.

from django.shortcuts import render
from .models import patient

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2> This page belongs to receptionist . Receptionist will add patient</h2>")