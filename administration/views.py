from django.shortcuts import render
from .models import Doctor, Receptionist, Admin
from login.models import login
from django.http import HttpResponse
import secrets
import string
from login.models import login
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage


def index(request):
    return render(request, "administration/index.html")

def gotocreatedoctor(request):
    return render(request, "administration/forms_basic_doc.html")

def createDoctor(request):
    try:
        doc_name = request.GET.get('Name1')
        doc_mob_no = request.GET.get('mob_no')
        doc_age = request.GET.get('age')
        doc_email = request.GET.get('email')
        doc_address = request.GET.get('address')
        doc_sex = request.GET.get('sex')
        doc_lic_no = request.GET.get('')
        hos_id = request.GET.get('')
        doc_design = request.GET.get('design')
        doc_dep = request.GET.get('department')
        doc_exp = request.GET.get('year_exp')
        sex='No value set'
        if(doc_sex == '1'):
            sex = 'Male'
        elif(doc_sex == '0'):
            sex = 'Female'       
        try:
            user_exists = False
            posts = login.objects.all()
            for post in posts:
                if(doc_mob_no == post.loginId):
                    print("mobile already exist")
                    user_exists = True
            if(not user_exists):
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


                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(10)) # for a 20-character password

                        print(password)
                        '''
                        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                        [''+emailID], fail_silently=False)
                        '''


                        try:
                            subject = 'Thank you for registering to our site'
                            message = ' The private key is '+password
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [''+doc_email,]
                            send_mail( subject, message, email_from, recipient_list )
                        except Exception as e:
                            print(e)

                        log = login()
                        log.loginId = doc_mob_no
                        log.passWord = password
                        log.userType = 'doctor'
                        log.save()

                        '''
                        posts = patient.objects.all()
                        for post in posts:
                            print(post.pat_name)
                        '''
                        return render(request,'administration/index.html')
        except Exception as e:
            print(e)               
    except Exception as e:
        print(e)
        
    #return HttpResponse("" + doc_name +  "\n"+ doc_dep + "\n" + doc_mob_no + "\n" + doc_email + "\n" + "Doctor Id: 1234567" + "\n" + doc_address + "\n" + doc_age +  "\n")

def gotocreatereceptionist(request):
    return render(request, 'administration/forms_basic_recep.html')

def createReceptionist(request):
     try:
        rec_name = request.GET.get('Name1')
        rec_mob_no = request.GET.get('mob_no')
        rec_age = request.GET.get('age')
        rec_email = request.GET.get('email')
        rec_address = request.GET.get('address')
        rec_exp = request.GET.get('year_exp')
        rec_id = request.GET.get('rec_id')
        sex = 'No value set'
        if(rec_sex == '1'):
            sex = 'Male'
        elif(rec_sex == '0'):
            sex = 'Female' 
        
        try:
            user_exists = False
            posts = login.objects.all()
            for post in posts:
                if(rec_mob_no ==post.loginId):
                    print("mobile already exist")
                    user_exists = True
            if(not user_exists):
                        recp = Receptionist()
                        recp.rec_name = rec_name
                        recp.rec_mob_no = rec_mob_no
                        recp.rec_age = rec_age
                        recp.rec_email = rec_email
                        recp.rec_address = rec_address
                        '''recp.rec_sex = rec_sex'''

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(10)) # for a 20-character password

                        print(password)
                        '''
                        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                        [''+emailID], fail_silently=False)
                        '''


                        try:
                            subject = 'Thank you for registering to our site'
                            message = ' The private key is '+password
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [''+rec_email,]
                            send_mail( subject, message, email_from, recipient_list )
                        except Exception as e:
                            print(e)

                        log = login()
                        log.loginId = rec_mob_no
                        log.passWord = password
                        log.userType = 'reception'
                        log.save()

                        '''
                        posts = patient.objects.all()
                        for post in posts:
                            print(post.pat_name)
                        '''
                        return render(request,'administration/forms_basic_recep.html')
        except Exception as e:
            print(e)               
     except Exception as e:
        print(e)
     return HttpResponse("" + rec_name + "\n"+ rec_mob_no +"\n" + rec_age +"\n" + rec_email +"\n" + rec_address +"\n" + '''rec_sex +''' "\n" + rec_id)

        
def sample(request):
    return render(request, 'administration/forms_basic_doc.html')
    #return HttpResponse("Hey!")

def email(request):
    return render(request,'administration/email.html')