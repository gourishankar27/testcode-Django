from django.contrib import admin
from .models import patient, Docs, Case

# Register your models here.
admin.site.register(Docs)
admin.site.register(Case)