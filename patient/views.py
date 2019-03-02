from django.shortcuts import render
from django.http import HttpResponse
from doctors.models import Case
from doctors import views

# Create your models here.

#pat_data = patient()

<<<<<<< HEAD
def index_patient(request):
    return render(request, 'patient/total-report.html')

def pat_display(request):

=======
def pat_display(request):
>>>>>>> dd067ab97bb35df4132889c1e40ee5f78ace446d
    pat_data = patient.objects.all()
    context = {
        'pat_data': pat_data
    }
<<<<<<< HEAD
    #for id in pat_data:
        #if pat_data.id == "":
            #print "Correct!"
    #return HttpResponse("<h1>Hiii</h1>")       
    return render(request, 'patient/sample.html', context)
=======
    return render(request, "patient/index.html")
>>>>>>> dd067ab97bb35df4132889c1e40ee5f78ace446d

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


