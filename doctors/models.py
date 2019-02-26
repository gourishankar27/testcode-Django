from django.contrib.auth.models import Permission, User
from from django.core.validators import int_list_validator
from django.db import models


class docs(models.Model):
  patient_RID = models.Charfield
  "patient_DID
  "Hospital ID":"",
  "Case Name":"",
  "Case Number":""
  "Realted Doc":""
  "Case Info":"",
            
    def __str__(self):
        return self.doc_name


