from django.db import models


class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_id = models.CharField(max_length=50)
    doc_mob_no = models.CharField(max_length=12)
    doc_address = models.CharField(max_length=500)
    doc_age = models.CharField(max_length=2)
    doc_lic_no = models.CharField(max_length=100)
    doc_admin_id = models.CharField(max_length=50)
    doc_patient_id = models.CharField(max_length=100)

class Receptionist(models.Model):
    rec_name = models.CharField(max_length=100)
    rec_id = models.CharField(max_length=100)
    rec_email_id = models.CharField(max_length=50)
    rec_mob_no = models.CharField(max_length=12)
    rec_address =  models.CharField(max_length=500)
    rec_age = models.CharField(max_length=2)
    rec_patient_id = models.CharField(max_length=100)

class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_id = models.CharField(max_length=100)
    admin_email_id = models.CharField(max_length=50)
    admin_mob_no = models.CharField(max_length=12)
    admin_address = models.CharField(max_length=500)
    admin_age = models.CharField(max_length=2)
    admin_patient_id = models.CharField(max_length=100)


