from django.shortcuts import render
from .models import Doctor, Receptionist, Admin

from django.http import HttpResponse

def index(request):
    return render(request, "administration/index.html")

def gotocreatedoctor(request):
    return render(request, "administration/forms_basic_doc.html")

def createDoctor(request):
    print('fakkk')
    try:
        doc_name = request.GET.get('Name1')
        doc_mob_no  = request.GET.get('mob_no')
        doc_age = request.GET.get('age')
        doc_email = request.GET.get('email')
        doc_address = request.GET.get('address')
        doc_sex = request.GET.get('sex')
        doc_lic_no = request.GET.get('')
        hos_id = request.GET.get('')
        doc_design = request.GET.get('design')
        doc_dep = request.GET.get('department')
        doc_exp = request.GET.get('year_exp')
        
        '''sex='No value set'
        if(doc_sex == '1'):
            sex = 'Male'
        elif(doc_sex == '0'):
            sex = 'Female' '''

        doc = Doctor()
        doc.doc_name = doc_name
        doc.doc_id = '1234'
        doc.hos_id = 'pune4321'
        doc.doc_email = doc_email
        doc.doc_mob_no = doc_mob_no
        doc.doc_address = doc_address
        doc.doc_age = doc_age
        doc.doc_sex = doc_sex
        doc.doc_dep = doc_dep
        doc.doc_exp = doc_exp
        doc.save() 

        print(doc.name)
        return HttpResponse("CreateDoctor success")
        #return render(request, 'administration/forms_basic_doc.html')

    except:
        Exception
        return HttpResponse("CreateDoctor success1")
        #return HttpResponse("" + doc_name +  "\n"+ doc_dep + "\n" + doc_mob_no + "\n" + doc_email + "\n" + "Doctor Id: 1234567" + "\n" + doc_address + "\n" + doc_age +  "\n")

def gotocreatereceptionist(request):
    return render(request, "administration/forms_basic_recep.html")

def createReceptionist(request):
     try:
        rec_name = request.GET.get('Name1')
        rec_mob_no = request.GET.get('mob_no')
        rec_age = request.GET.get('age')
        rec_email = request.GET.get('email')
        rec_address = request.GET.get('address')
        rec_exp = request.GET.get('year_exp')
        '''sex = 'No value set'
        if(rec_sex == '1'):
            sex = 'Male'
        elif(rec_sex == '0'):
            sex = 'Female' '''

        rec_id = request.GET.get('rec_id')

        recp = Receptionist()
        recp.rec_name = rec_name
        recp.rec_mob_no = rec_mob_no
        recp.rec_age = rec_age
        recp.rec_email = rec_email
        recp.rec_address = rec_address
        '''recp.rec_sex = rec_sex'''

        return HttpResponse("CreateReceptionist success")

     except:
        Exception
        return HttpResponse("" + rec_name + "\n"+ rec_mob_no +"\n" + rec_age +"\n" + rec_email +"\n" + rec_address +"\n" + '''rec_sex +''' "\n" + rec_id)
    

def sample(request):
    return render(request, 'administration/forms_basic_doc.html')
    #return HttpResponse("Hey!")
