from django.shortcuts import render
from django.http import HttpResponse
from reception.models import patient
from doctors import views

<<<<<<< HEAD
def index1(request):
    return render(request, 'patient/index.html')
=======
def index(request):
    return render(request, 'patient1/index.html')
>>>>>>> 6d2fb7e5b89dbf801483c37c2a629902d31c4472

def pat_display(request):
    pat_data = patient.objects.all()
    context = {
        'pat_data': pat_data
    }
    return render(request, 'patient1/sample.html', context)
    #count_male = 0
    #count_female = 0
    #patient_id = '81'
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


    #pat_data = patient1()
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