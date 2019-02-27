from django.db import models


class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_id = models.CharField(max_length=50)
    hos_id = models.CharField(max_length = 30)
    doc_mob_no = models.CharField(max_length=12)
    doc_address = models.CharField(max_length=500)
    doc_age = models.CharField(max_length=2)
    doc_email = models.CharField(max_length=40)
    doc_lic_no = models.CharField(max_length=100)
    doc_admin_id = models.CharField(max_length=50)
    doc_patient_id = models.CharField(max_length=100)
    doc_sex = modesl.CharField(max_length=10)
    doc_design = CharField(max_lemngth=50)
    doc_exp = CharField(max_length=4)
    
    def __str__(self):
        return self.doc_name + ' - ' + self.doc_id


class Receptionist(models.Model):
    rec_name = models.CharField(max_length=100)
    rec_id = models.CharField(max_length=100)
    hos_id = models.CharField(max_length = 30)
    rec_email_id = models.CharField(max_length=50)
    rec_mob_no = models.CharField(max_length=12)
    rec_address =  models.CharField(max_length=500)
    rec_age = models.CharField(max_length=2)
    rec_patient_id = models.CharField(max_length=100)

    def __str__(self):
        return self.rec_name + ' - ' + self.rec_id


class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=100)
    hos_id = models.CharField(max_length = 30)
    admin_email_id = models.CharField(max_length=50)
    admin_mob_no = models.CharField(max_length=12)
    admin_address = models.CharField(max_length=500)
    admin_age = models.CharField(max_length=2)
    admin_patient_id = models.CharField(max_length=100)

    def __str__(self):
        return self.admin_name + ' - ' + self.admin_id



