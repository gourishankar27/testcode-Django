from django.http import HttpResponse
from .models import Docs, Case
from django.shortcuts import render

#from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
#from .forms import UserForm


def index(request):
    template = 'doctors/add-patientdetails.html'
    context ={}

<<<<<<< HEAD
    return render(request,template,context) 
=======
    return render(request,template,context)
>>>>>>> 826c51a6be3a7dee041ca047542e8b00c7f19800

#   context_object_name = 'all_patients'\

#
#   def get_queryset(self):
 #       return docs.objects.all()

def AddCaseView():
    template = 'doctors/add-patientdetails.html'
    try:
        CaseName = request.GET.get('casename')
        CaseInfo = request.GET.get('caseinfo')
        DocUpload = request.GET.get('doc')
        Medicines = request.GET.get('medicines')

        pat = Case()
        pat.CaseName = CaseName
        pat.CaseInfo = CaseInfo
        pat.Medicines = Medicines
        pat.DocUploads = DocUpload
        pat.save()

    except:
        Exception

    return HttpResponse("<h1>Data Encrypted and Stored<> "  "\n" + CaseName + "\n" + CaseInfo + "\n" + Medicines )


#def AppendCaseView():
    #    model = docs
#  template_name = 'doctors/patient_view.html'


#def ViewCaseView():
    template = 'doctors/add-patientdetails.html'
    obj = Case.objects.all()
    context = {'casenumber': obj.CaseNumber,'casename': obj.CaseName}
# Every case number will have append button, thus will direct to ameyas append page

    return render(request,template,context)