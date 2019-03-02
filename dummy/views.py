from django.shortcuts import render
from .models import loginDetails
from django.http import HttpResponse


def index(request):
    return render(request, "login.html")

def gotonext(request):
    try:
        uname = request.GET.get('username')
        passs = request.GET.get('password')
        
        ld = loginDetails()
        ld.username = uname
        ld.password = passs
        ld.types = "amey"
        ld.save()


        post = loginDetails.objects.all()
        for po in post:
            print(po)


        return HttpResponse("<input type=\"text\" value="+uname+">")
    except:
        
        print(Exception)
        return HttpResponse("code is not working as expected please try again "+ str(Exception))