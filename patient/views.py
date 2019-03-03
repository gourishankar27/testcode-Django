from django.shortcuts import render
from django.http import HttpResponse
from reception.models import patient
from doctors import views

def index(request):
    return render(request, 'patient/index.html')

def pat_display(request):
    pat_data = patient.objects.all()
    context = {
        'pat_data': pat_data
    }
    count_male = 0
    count_female = 0
    patient_id = '81'
    '''for pt in pat_data:
       # if(pt.pat_gender == 'Male'):
        if(pt.id == patient_id ):
            #count_male += 1
            print (pt.pat_name)  
        else:
            count_female += 1 
    print(count_male)
    print(count_female) '''

    '''for pt in pat_data:
        if(pt.pat_gender == 'Male'):
            count_male+=1
            print("Males: "+count_male)
            print("Females: "+count_female)
        else:
            count_female+=1
            print("Males: "+count_male)
            print("Females: "+count_female) '''

    return render(request, 'patient/sample.html', context)

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