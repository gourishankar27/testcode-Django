
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
                print(types.loginID)
                if(types.userType == 'reception'):
                    return render(request,"reception/reception.html")
                #return HttpResponse(""+types.userType)
                #return render(request,"dummy/login.html")
                elif(types.userType == 'patient'):
                    return render(request,"dummy/login.html")
        return HttpResponse("")
    except:
        print(Exception)