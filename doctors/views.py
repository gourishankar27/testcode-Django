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

    return render(request,template,context) cvdf

#   context_object_name = 'all_patients'\

#
#   def get_queryset(self):
 #       return docs.objects.all()

#def AddCaseView():
    #model = docs
    #    template_name = 'doctors/patient_view.html'

#def AppendCaseView():
    #    model = docs
#  template_name = 'doctors/patient_view.html'


#def ViewCaseView():
    #   model = docs
    #fields = ['patient_caseName','patient_caseInfo','patient_relatedDoc']
    #template_name = 'doctors/addPatient'
