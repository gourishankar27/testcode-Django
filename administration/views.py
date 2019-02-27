from django.shortcuts import render
from .models import Doctor,Receptionist,Admin

from django.http import HttpResponse


def index(request):
    return render(request, "administration/index.html")

def creatDoctor(request):
    try:
        doc_name = request.GET.get('name')
        mobile = request.GET.get('mob_no')
        age = request.GET.get('age')
        emailID = request.GET.get('email')
        address = request.GET.get('address')
        getsex = request.GET.get('sex')
        sex='No value set'
        if(getsex=='1'):
            sex = 'Male'
        elif(getsex=='0'):
            sex = 'Female'       
        
    except:
        Exception
