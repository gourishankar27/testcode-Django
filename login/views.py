<<<<<<< HEAD
from django.shortcuts import render
from .models import login
from django.http import HttpResponse
from dummy.views import index
from reception.views import index


def index(request):
    return render(request, "login/login.html")

def loginusers(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('pass')
        #print(""+username+"\n"+password)
        print(username)
        print(password)
        print()
        logintype = login.objects.all()        
        for types in logintype:
            if(str(types.loginId) == str(username) and str(types.passWord) == str(password)):
                print(types.userType)
                print(types.loginId)
                #return HttpResponse(""+types.userType)
                if(types.userType == 'reception'):
                    return render(request,"reception/reception.html")
                elif(types.userType == 'patient'):
                    return render(request,"dummy/login.html")
                
            #else:
             #   return HttpResponse("User not found")
        return HttpResponse("")
    except:
        print(Exception)

=======

from django.shortcuts import render
from .models import login
from django.http import HttpResponse
from dummy.views import index


def index(request):
    return render(request, "login/login.html")

def loginusers(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('pass')
        #print(""+username+"\n"+password)
        print(username)
        print(password)
        print()
        logintype = login.objects.all()        
        for types in logintype:
            if(str(types.loginId) == str(username) and str(types.passWord) == str(password)):
                print(types.userType)
<<<<<<< HEAD
                print(types.loginId)
                return HttpResponse(""+types.userType)
            #else:
             #   return HttpResponse("User not found")
=======
<<<<<<< HEAD
                #return HttpResponse(""+types.userType)
                return render(request,"dummy/login.html")
            else:
                return HttpResponse("User not found")
=======
                print(types.loginId)
                #return HttpResponse(""+types.userType)
                return render(request,"dummy/login.html")
            #else:
             #   return HttpResponse("User not found")
>>>>>>> 17c62eeca74df5ef3d80699f3756817328981d03
>>>>>>> ee3b27f9a5de7c6c64403d5e25714850e24e1994
        return HttpResponse("")
    except:
        print(Exception)
>>>>>>> 4f504f30a33bf947621d55158be8aebd189df94f
