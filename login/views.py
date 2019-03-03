from django.shortcuts import render
from .models import login
from django.http import HttpResponse
from dummy.views import index
from reception.views import index
import hashlib


def index(request):
    return render(request, "login/login.html")

def loginusers(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('pass')
        enc_uname = hashlib.sha256(username.encode("utf-8")).hexdigest()
        enc_passs = hashlib.sha256(password.encode("utf-8")).hexdigest()
        username = enc_uname
        password = enc_passs
        #print(""+username+"\n"+password)
        print(username)
        print(password)
        #print()
        logintype = login.objects.all()        
        for types in logintype:
            if(str(types.loginId) == str(username) and str(types.passWord) == str(password)):
                print(types.userType)
                print(types.loginId)
                #return HttpResponse(""+types.userType)
                if(types.userType == 'reception'):
                    print("Reception")
                    return render(request,"reception/reception.html")
                elif(types.userType == 'patient'):
                    print("Patient")
                    return render(request,"dummy/login.html")
                elif(types.userType == 'doctor'):
                    #return HttpResponse("gotodoctors page")
                    return render(request, "doctors/index_doctors.html")
            #else:
             #   return HttpResponse("User not found")
        return HttpResponse("Username or password is incorrect")
    except:

        print(Exception)


