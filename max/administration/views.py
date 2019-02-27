from django.shortcuts import render
from django.shortcuts import render
from .models import Doctor,Receptionist,Admin

from django.http import HttpResponse


def index(request):
    return render(request, "administration/index.html")

