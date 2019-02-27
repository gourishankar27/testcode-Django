from django.shortcuts import render
from .models import patient

from django.http import HttpResponse


def index(request):
    return render(request, "reception/reception.html")

def createPatient(request):
    try:
        firstName = request.GET.get('firstName')
        lastName = request.GET.get('lastName')
        mobile = request.GET.get('mobile')
        caseNumber = request.GET.get('caseNumber')
        doctorID = request.GET.get('doctorID')
        age = request.GET.get('age')
        emailID = request.GET.get('emailID')
        weight = request.GET.get('weight')
        bodyMassIndex = request.GET.get('bodyMassIndex')
        dateOfBirth = request.GET.get('dateOfBirth')
        address = request.GET.get('address')
        getsex = request.GET.get('sex')
        sex='No value set'
        if(getsex=='1'):
            sex = 'Male'
        elif(getsex=='0'):
            sex = 'Female'       
        
    except:
        Exception

    return HttpResponse("" + firstName + "\n"+lastName+"\n"+mobile+"\n"+caseNumber+"\n"+doctorID+"\n"+age+"\n"+emailID+"\n"+weight+"\n"+bodyMassIndex+"\n"+dateOfBirth+" "+address+" "+" "+sex)