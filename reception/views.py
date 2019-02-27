from django.shortcuts import render
from .models import patient
from django.http import HttpResponse


def index(request):
    return render(request, "reception/reception.html")

def createPatient(request):
    try:
        var = request.GET.get('firstname')
        print(var)
        
    except:
        Exception

|
    return HttpResponse("HI " + var)