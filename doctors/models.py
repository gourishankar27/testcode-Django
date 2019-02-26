from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models


class PatientData(models.Model):
    user = models.ForeignKey(User, default=1)
    patient_ID = models.CharField(max_length=15)
    patient_RID = models.CharField(max_length=15)
    patient_DID = models.CharField(max_length=100)
    patient_HID = models.CharField(max_length=20)
    patient_caseName = models.CharField(max_length=5)
    patient_caseID = models.CharField(max_length=20)
    patient_caseInfo = models.CharField(max_length=20)
    patient_relatedDoc = models.FileField()

    def get_absolute_url(self):
        return reverse('doctors',kwargs=('pk': self.pk))

    def __str__(self):
        return self.patient_ID


