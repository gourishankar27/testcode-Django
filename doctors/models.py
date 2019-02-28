from django.db import models




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
  DocUploads = models.FileField()

  def __str__(self):
    return self.CaseNumber+'-'+self.CaseName
