from django.shortcuts import render
from .models import patient
from login.models import login
from django.http import HttpResponse
import secrets
import string
from login.models import login
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
import hashlib

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
        try:      
            user_exists = False
            posts = login.objects.all()
            for post in posts:
                if(mobile ==post.loginId):
                    print("mobile already exist")
                    user_exists = True
            if(not user_exists):
                        pat = patient()
                        pat.pat_name = firstName+" "+lastName
                        pat.pat_id = '1234'
                        pat.hos_id = 'pune4321'
                        pat.pat_email_id = emailID
                        pat.pat_mon_no = mobile
                        pat.pat_address = address
                        pat.pat_age = age
                        pat.save()


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
                            recipient_list = [''+emailID, ]
                            send_mail(subject, message, email_from, recipient_list)
                        except Exception as e:
                            print(e)
                        enc_uname = hashlib.sha256(mobile.encode("utf-8")).hexdigest()
                        enc_passs = hashlib.sha256(password.encode("utf-8")).hexdigest()

                        log = login()
                        log.loginId = enc_uname
                        log.passWord = enc_passs
                        log.userType = 'patient1'
                        log.save()

                        '''
                        posts = patient1.objects.all()
                        for post in posts:
                            print(post.pat_name)
                        '''
        except Exception as e:
            print(e)               
    except Exception as e:
        print(e)
    return HttpResponse("" + firstName + "\n"+lastName+"\n"+mobile+"\n"+caseNumber+"\n"+doctorID+"\n"+age+"\n"+emailID+"\n"+weight+"\n"+bodyMassIndex+"\n"+dateOfBirth+" "+address+" "+" "+sex)

