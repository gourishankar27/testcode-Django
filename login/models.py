from djongo import models

# Create your models here.
class login(models.Model):
    loginId = models.CharField(max_length = 100)
    passWord = models.CharField(max_length = 100)
    userType = models.CharField(max_length = 30)
