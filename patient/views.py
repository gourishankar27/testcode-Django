from django.shortcuts import render
from django.http import HttpResponse
from reception.models import patient
from doctors import views

def index1(request):
    return render(request, 'patient/index.html')

def pat_display(request):
    pat_data = patient.objects.all()
    context = {
        'pat_data': pat_data
    }
    x=0
    for obj in pat_data:
        x=x+1
    
    return render(request, "patient/sample.html", context)

    #pat_data = patient()
    #pat_name = pat_data.pat_name
    #pat_id = pat_data.pat_id
    #pat_hos_id = pat_data.hos_id
    #pat_email_id = pat_data.pat_email_id
    #pat_mon_no = pat_data.pat_mon_no
    #pat_address = pat_data.pat_address
    #pat_age = pat_data.pat_age
    #pat_data.save()

    #template = 'index.html'
    #return render(request, template)
    #return HttpResponse("Hello")


