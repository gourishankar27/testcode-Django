
# Create your models here.
from djongo import models
#from django.db import models

class patient(models.Model):
    pat_name = models.CharField(max_length = 100)
    pat_id = models.CharField(max_length = 30)
    hos_id = models.CharField(max_length = 30)
    pat_email_id = models.CharField(max_length = 50)
    pat_mon_no = models.CharField(max_length=12)
    pat_address = models.CharField(max_length = 1000)
    pat_age = models.CharField(max_length = 4)
    
    def __str__(self):
        return self.pat_name + ' - ' + self.pat_id