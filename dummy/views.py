from django.shortcuts import render
from .models import loginDetails
from django.http import HttpResponse
import hashlib
#from passlib.hash import pbkdf2_sha256



temp_uname = ""

def index(request):
    return render(request, "dummy/login.html")

def gotonext(request):
    try:
        uname = request.GET.get('username')
        passs = request.GET.get('password')

        enc_uname = hashlib.sha256(b"uname").hexdigest()
        enc_passs = hashlib.sha256(b"passs").hexdigest()
        #temp_uname = enc_uname
        ld = loginDetails()
        ld.username = uname
        ld.password = enc_passs
        ld.types = "doctor"
        ld.save()


        post = loginDetails.objects.all()
        for po in post:
            print(po)



        return HttpResponse("<input type=\"text\" value="+uname+">")

    except:
        print(Exception)
        return HttpResponse("code is not working as expected please try again "+ str(Exception))
    return render(request,'dummy/loginnew.html')
def gotologinnew(request):
    uname = request.GET.get('username')
    passs = request.GET.get('password')

    post = loginDetails.objects.all()
    for po in post:
        if(po.username == uname):
            var = pbkdf2_sha256.verify(passs, po.password)
            if(var == True):
                return HttpResponse("login successful")
            else:
                return HttpResponse("something is wrong")



