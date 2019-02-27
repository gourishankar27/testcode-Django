from django.shortcuts import render
from .models import patient

from django.http import HttpResponse


def index(request):
    return render(request, "reception/reception.html")