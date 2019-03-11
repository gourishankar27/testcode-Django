from django.shortcuts import render
from reception.models import patient
from django.http import HttpResponse
from doctors.models import Case
from doctors import views
from login.models import login
from login.views import loginusers
# Create your views here.

def index_patient(request):
    return render(request, 'patient1/index_patient.html')

def gotopatient1(request):
    return render(request, 'patient1/sample.html')

def ShowPatient(request):
    pat_data = patient.objects.all()
    context = {
      'pat_data': pat_data
    }

    return render(request, 'patient1/sample.html', context)

def gotoOnePatient(request):
    return render(request, 'patient1/demo.html')

def OnePatient(request):
    '''id = request.GET.get('id')
    obj = patient.objects.all()
    for object in obj:
        if (id == object.pat_id):
            context = {'object': object}
    #pat = patient.objects.get(pk="82")
    return render(request, 'patient1/demo.html', context)'''

    id = patient.objects.get(pk="82")
    obj = patient.objects.all()
    for object in obj:
        if (id == object.pat_id):
            context = {'object': object}
            return render(request, 'patient1/demo.html', context)

    return render(request, 'patient1/demo.html')


def pat_display(request):
    pat = Case.objects.all()
    context = {
        'pat': pat
    }

    patient1 = 9762985808
    patient2 = 7744868511

    if (username == patient1):
        pat1 = Case.objects.get(pk="82")
        return HttpResponse("<h1>Cases for {{username}} :</h1><ul>{{Case.Name}}</ul>")

    elif (username == patient2):
        pat2 = Case.objects.get(pk="83")
        return HttpResponse("<h1>Cases for {{username}} :</h1><ul>{{Case.Name}}</ul>")