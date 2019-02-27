from django.shortcuts import render
from .models import Doctor,Receptionist,Admin

from django.http import HttpResponse


def index(request):
    return render(request, "administration/index.html")

def creatDoctor(request):
    try:
        doc_name = request.GET.get('name')
        doc_mob_no  = request.GET.get('mob_no')
        doc_age = request.GET.get('age')
        doc_email = request.GET.get('email')
        doc_address = request.GET.get('address')
        doc_sex = request.GET.get('sex')
        doc_lic_no = request.GET.get('')
        hos_id = request.GET.get('')
        doc_design = request.GET.get('design')
        doc_dep = request.GET.get('')
        doc_exp = request.GET.get('year_exp')


        sex='No value set'
        if(getsex=='1'):
            sex = 'Male'
        elif(getsex=='0'):
            sex = 'Female'    

        doc = Doctor()
        doc.doc_name = name
        doc.doc_id = '1234'
        doc.hos_id = 'pune4321'
        doc.doc_email_id = email
        doc.doc_mob_no = mob_no
        doc.doc_address = address
        doc.doc_age = age
        doc.doc_sex = sex
        doc.doc_dep = dep
        doc.doc_exp = 
        doc.save()   
        
    except:
        Exception 

     return HttpResponse("" + name +  "\n"+ dep + "\n" + mob_no + "\n" + email + "\n" + doc_id + "\n" + year_exp +  "\n"+ address + "\n" + age +  "\n"+  )



