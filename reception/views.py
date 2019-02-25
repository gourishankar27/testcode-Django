

# Create your views here.

from django.shortcuts import render
from .models import reception

from django.http import HttpResponse


def index(request):
    xyz = reception.objects.all()
    context = {'xyz':xyz}
    return render(request ,'reception/index.html',context)