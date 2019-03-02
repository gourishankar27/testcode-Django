from djongo import models
from django.db import models
from passlib.hash import pbkdf2_sha256

class loginDetails(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)


