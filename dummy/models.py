from djongo import models
# Create your models here.
class loginDetails(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 30)
    types = models.CharField(max_length = 30)