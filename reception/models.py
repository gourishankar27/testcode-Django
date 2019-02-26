
# Create your models here.
from djongo import models

class reception(models.Model):
    Name = models.CharField(max_length = 100)
    ReceptionID = models.CharField(max_length = 30)
    HospitalID = models.CharField(max_length = 30)
    EmailID = models.CharField(max_length = 50)
    MobileNo = models.CharField(max_length=12)
    Address = models.CharField(max_length = 1000)
    Age = models.CharField(max_length = 4)
    PatientIDcount = models.IntegerField(default=0)
        
    def __str__(self):
        return self.Name + ' - ' + self.ReceptionID