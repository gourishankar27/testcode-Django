from django.shortcuts import render
from .models import Doctor, Receptionist, Admin
import re
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
import csv
from django.utils.encoding import smart_str
from Crypto.Cipher import AES
import base64

MASTER_KEY="0))5i+u9$ec0r9*4!o_k5p8k)y+bule0"

def index(request):
    return render(request, "administration/index.html")

def gotocreatedoctor(request):
    return render(request, "administration/forms_basic_doc.html")

def createDoctor(request):
    try:
        doc_name = request.GET.get('Name1')
        doc_mob_no = request.GET.get('mob_no')
        doc_age = request.GET.get('age')
        doc_email = request.GET.get('email')
        doc_address = request.GET.get('address')
        doc_sex = request.GET.get('sex')
        doc_lic_no = request.GET.get('')
        hos_id = request.GET.get('')
        doc_design = request.GET.get('design')
        doc_dep = request.GET.get('department')
        doc_exp = request.GET.get('year_exp')
        sex='No value set'
        if(doc_sex == '1'):
            sex = 'Male'
        elif(doc_sex == '0'):
            sex = 'Female'       
        try:
            user_exists = False
            posts = login.objects.all()
            for post in posts:
                if(doc_mob_no == post.loginId):
                    print("mobile already exist")
                    user_exists = True
            if(not user_exists):
                        doc = Doctor()
                        doc.doc_name = doc_name
                        doc.doc_id = '1234'
                        doc.hos_id = 'pune4321'
                        doc.doc_email = doc_email
                        doc.doc_mob_no = doc_mob_no
                        doc.doc_address = doc_address
                        doc.doc_age = doc_age
                        doc.doc_sex = doc_sex
                        doc.doc_dep = doc_dep
                        doc.doc_exp = doc_exp
                        doc.save()   


                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(10)) # for a 20-character password

                        print(password)
                        '''
                        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                        [''+emailID], fail_silently=False)
                        '''


                        try:
                            subject = 'Thank you for registering to our site'
                            message = ' The private key is '+password
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [''+doc_email,]
                            send_mail( subject, message, email_from, recipient_list )
                        except Exception as e:
                            print(e)
                        enc_uname1 = hashlib.sha256(doc_mob_no.encode("utf-8")).hexdigest()
                        enc_passs1 = hashlib.sha256(password.encode("utf-8")).hexdigest()

                        log = login()
                        log.loginId = enc_uname1
                        log.passWord = enc_passs1
                        log.userType = 'doctor'
                        log.save()

                        '''
                        posts = patient1.objects.all()
                        for post in posts:
                            print(post.pat_name)
                        '''
                        return render(request,'administration/index.html')
        except Exception as e:
            print(e)               
    except Exception as e:
        print(e)
    return HttpResponse("done with the file")   
    #return HttpResponse("" + doc_name +  "\n"+ doc_dep + "\n" + doc_mob_no + "\n" + doc_email + "\n" + "Doctor Id: 1234567" + "\n" + doc_address + "\n" + doc_age +  "\n")

def gotocreatereceptionist(request):
    return render(request, 'administration/forms_basic_recep.html')

def createReceptionist(request):
     try:
        rec_name = request.GET.get('Name1')
        rec_mob_no = request.GET.get('mob_no')
        rec_age = request.GET.get('age')
        rec_email = request.GET.get('email')
        rec_address = request.GET.get('address')
        rec_exp = request.GET.get('year_exp')
        rec_id = request.GET.get('rec_id')
        sex = 'No value set'
        if(rec_sex == '1'):
            sex = 'Male'
        elif(rec_sex == '0'):
            sex = 'Female' 
        
        try:
            user_exists = False
            posts = login.objects.all()
            for post in posts:
                if(rec_mob_no ==post.loginId):
                    print("mobile already exist")
                    user_exists = True
            if(not user_exists):
                        recp = Receptionist()
                        recp.rec_name = rec_name
                        recp.rec_mob_no = rec_mob_no
                        recp.rec_age = rec_age
                        recp.rec_email = rec_email
                        recp.rec_address = rec_address
                        '''recp.rec_sex = rec_sex'''

                        alphabet = string.ascii_letters + string.digits
                        password = ''.join(secrets.choice(alphabet) for i in range(10)) # for a 20-character password

                        print(password)
                        '''
                        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
                        [''+emailID], fail_silently=False)
                        '''


                        try:
                            subject = 'Thank you for registering to our site'
                            message = ' The private key is '+password
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [''+rec_email,]
                            send_mail( subject, message, email_from, recipient_list )
                        except Exception as e:
                            print(e)

                        enc_uname2 = hashlib.sha256(rec_doc_mob.encode("utf-8")).hexdigest()
                        enc_passs2 = hashlib.sha256(password.encode("utf-8")).hexdigest()

                        log = login()
                        log.loginId = enc_uname2
                        log.passWord = enc_passs2
                        log.userType = 'reception'
                        log.save()

                        '''
                        posts = patient1.objects.all()
                        for post in posts:
                            print(post.pat_name)
                        '''
                        return render(request,'administration/forms_basic_recep.html')
        except Exception as e:
            print(e)               
     except Exception as e:
        print(e)
     return HttpResponse("" + rec_name + "\n"+ rec_mob_no +"\n" + rec_age +"\n" + rec_email +"\n" + rec_address +"\n" + '''rec_sex +''' "\n" + rec_id)

        
def sample(request):
    return render(request, 'administration/forms_basic_doc.html')
    #return HttpResponse("Hey!")

def email(request):
    return render(request,'administration/email.html')

def sendmail(request):
    email = request.GET.get('emailID')
    subject = request.GET.get('subject')
    body = request.GET.get('body')
    if(email != ""):
        print("send mail")
        domain = email.split('@')[1]
        if domain == "gmail.com":
            print("Verified requester")
            download_csv_data(request)
            try:
                subject = 'Mail within the domain '+subject
                message = ' The email can be only sent to users within domain '+body
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [''+email, ]
                send_mail(subject, message, email_from, recipient_list)
                return HttpResponse("mail sent successfully")
            except Exception as e:
                print(e)
        else:
            print("un-Verified user")
            return HttpResponse("unverified user")
    else:
        return HttpResponse("please enter email and try again")
def download_csv_data(request):
    # response content type
    try:
        print("inside download csv")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        writer.writerow([encrypt_val("First row"), encrypt_val('Foo'), encrypt_val('Bar'), encrypt_val('Baz')])
        writer.writerow([encrypt_val("Second row"), encrypt_val('A'), encrypt_val('B'), encrypt_val('C'), encrypt_val("Testing"),encrypt_val( "Here's a quote")])
        print("response here")
        return response

    except Exception as e:
        print(e)


def encrypt_val(clear_text):
    '''
    enc_secret = AES.new(MASTER_KEY[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text
    '''
    '''
    obj = AES.new(MASTER_KEY, AES.MODE_CFB, 'This is an IV456')
    message = clear_text
    ciphertext = obj.encrypt(message)
    return ciphertext
    '''
    encryption_suite = AES.new(MASTER_KEY, AES.MODE_CFB, 'This is an IV456')
    cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")
    return cipher_text


def decrypt_val(cipher_text):
    '''
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.decode().rstrip("\0")
    return clear_val
    '''
    '''
    obj = AES.new(MASTER_KEY, AES.MODE_CFB, 'This is an IV456')
    stt = obj.decrypt(cipher_text)
    return stt
    '''
    decryption_suite = AES.new(MASTER_KEY, AES.MODE_CFB, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher_text)
    return plain_text
    
def upload_csv(request):
    data = {}
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect("file selected was not csv")
        
        file_data = csv_file.read().decode("utf-8")		
        temp=""
        cnt = 0
        #loop over the lines and save them in db. If error , store as string and then display
        #temp = file_data.split(',')
        for line in file_data:	
            #while(line != ','):
            if(line == ','):
                print(temp)
                print(cnt)
                print(decrypt_val(temp))
                temp = ""
                cnt = 0
            else:
                temp += line
                cnt += 1
        return HttpResponse("data read is at the end and the data is ")
    except Exception as e:
        print(e)

    return HttpResponseRedirect("")