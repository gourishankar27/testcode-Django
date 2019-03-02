from django.shortcuts import render
from django.http import HttpResponse
from reception.models import patient
from reception import views

# Create your models here.

#pat_data = patient()

def pat_diplsay(request):
    pat_data = patient.objects.all()
    context = {
        'pat_data': pat_data
    }
    return render(request, 'index.html', context)

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


