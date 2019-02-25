
# Create your models here.
from djongo import models

class reception (models.Model):
    Name = models.CharField(max_length = 100)
    ReceptionID = models.CharField(max_length = 30)
    HospitalID = models.CharField(max_length = 30)
    EmailID = models.CharField(max_length = 50)
    MoblieNo = models.CharField(max_length=12)