
from django.shortcuts import render
from .models import login
from django.http import HttpResponse


def index(request):
    return render(request, "login/login.html")

def loginusers(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('pass')
        #print(""+username+"\n"+password)
        
        logintype = login.objects.all()
        for types in logintype:
            print(types.userType)

        return HttpResponse("")
    except:
        print(Exception)