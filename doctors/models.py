from djongo import models
from django.urls import reverse

class Docs(models.Model):
  RecepID = models.CharField(max_length=20)
  DocsID = models.CharField(max_length=20)
  HospitalID = models.CharField(max_length=20)

  def __str__(self):
    return self.RecepID + '-' + self.DocsID + '-' + self.HospitalID


class Case(models.Model):
  #Docs = models.ForeignKey(Docs, on_delete=models.CASCADE)
  CaseNumber = models.CharField(max_length=20)
  CaseName = models.CharField(max_length=20)
  CaseInfo = models.CharField(max_length=250)
  Medicines = models.CharField(max_length=100)
  DocUploads = models.FileField()