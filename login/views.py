
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
        
        logintype = login.objects.all()
        for types in logintype:
            if(types.loginId == username and types.passWord == password):
                print(types.userType)
                #return HttpResponse(""+types.userType)
                return render(request,"dummy/login.html")
            else:
                return HttpResponse("User not found")
        return HttpResponse("")
    except:
        print(Exception)