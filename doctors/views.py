from django.http import HttpResponse
from .models import Docs, Case
from django.shortcuts import render

#from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic\
    
#from .forms import UserForm

def index_doctor(request):
    return render(request, "doctors/index_doctors.html")

def AddCaseView(request):

    try:
        CaseName = request.GET.get('case_name')
        CaseInfo = request.GET.get('diagnostic')
        DocUpload = request.GET.get('picture')
        Medicines = request.GET.get('medicines')

        pat = Case()
        pat.CaseName = CaseName
        pat.CaseInfo = CaseInfo
        pat.Medicines = Medicines
        pat.DocUploads = DocUpload
        pat.save()

        read = Case.objects.all()
        context = {
            'read': read
        }

        #return render(request, 'doctors/views_patient.html', context)
        #return render(request, 'doctors/details.html')
        return render(request, 'doctors/index_doctors.html', context)
        #return HttpResponse(
          #  "<h1>Data Encrypted and Stored</h1> "  "\n" + str(CaseName) + "\n" + str(CaseInfo) + "\n" + str(
           #     Medicines) + "<h2>Click the button to return to the homepage :</h2><form action=\"/index_doctor\" method=\"GET\"><input type=\"submit\" value=\"submit\"></form>")

        template = 'doctors/add-patientdetails.html'
        obj = Case.objects.all()
        context = {'casenumber': obj.CaseNumber,'casename': obj.CaseName}

    except:
        Exception
        print(Exception)

        #return HttpResponse("hello")
    #return render(request, 'doctors/details.html', context)
    #return render(request, 'doctors/views_patient.html', context)
    return HttpResponse("<h1>Data Encrypted and Stored</h1> "  "\n" + str(CaseName) + "\n" + str(CaseInfo) + "\n" + str(Medicines) + "<h2>Click the button to return to the homepage :</h2><form action=\"/index_doctor\" method=\"GET\"><input type=\"submit\" value=\"submit\"></form>")


def AddCaseViewButton(request):
    obj=Case.objects.all()
    for case in obj:
        casename = case.CaseName
        caseinfo = case.CaseInfo
        medicine = case.Medicines
    return HttpResponse("<h1>Data Encrypted and Stored</h1> "  "\n" + str(casename) + "\n" + str(caseinfo) + "\n" + str(medicine))


#def AppendCaseView():
    #    model = docs
#  template_name = 'doctors/patient_view.html'



def ViewCaseView(request):
    allcases = Case.objects.all()
    context = {
        'allcases': allcases
    }

'''def ViewCaseView():
    template = 'doctors/add-patientdetails.html'
    obj = Case.objects.all()
    context = {'casenumber': obj.CaseNumber,'casename': obj.CaseName}
    # append button will redirect to append page
    return render(request,template,context)   
'''


    #return render(request, 'doctors/views_patient.html', context)
