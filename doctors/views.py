from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import PatientData

class IndexView(generic.listView)
    template_name = 'doctors/index.html'
    context_object_name = 'all_patients'

    def get_queryset(self):
        return docs.objects.all()

class AddCase(request):
    context = {'PatientData'}
    template_name = 'doctors/patient_view.html'

class UpadtePatient(generic.UpdateView):
    model = PatientData
    fields = ['patient_caseName','patient_caseInfo','patient_relatedDoc']
    template_name = 'doctors/addPatient.html'
    