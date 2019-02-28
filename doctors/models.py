from django.db import models
from django.urls import reverse

class Docs(models.Model):
  RecepID = models.CharField(max_length=20)
  DocsID = models.CharField(max_length=20)
  HospitalID = models.CharField(max_length=20)

  #def __str__(self):
   # return self.RecepID + '-' + self.DocsID + '-' + self.HospitalID

<<<<<<< HEAD
class Case(models.Model):
  Docs = models.ForeignKey(Docs, on_delete=models.CASCADE)
  CaseNumber = models.CharField(max_length=20)
  CaseName = models.CharField(max_length=20)
  CaseInfo = models.CharField(max_length=250)
  Medicines = models.CharField(max_length=100)
=======

class docs(models.Model):
  RecepID = models.CharField(max_length='20')
  DocsID = models.CharField(max_length='20')
  HospitalID = models.CharField(max_length='20')

  def __str__(self):
    return self.RecepID +'-'+ self.DocsID +'-'+ self.HospitalID

class case(models.Model):
  docs = models.ForeignKey(docs, on_delete=models.CASCADE)
  CaseNumber = models.CharField()
  CaseName = models.CharField(max_length='20')
  CaseInfo = models.CharField(max_length='250')
>>>>>>> 369d2e1463b3486301dd7ba4939c9be324a029ea
  DocUploads = models.FileField()

  #def __str__(self):
    #return self.CaseNumber+'-'+ self.CaseName
