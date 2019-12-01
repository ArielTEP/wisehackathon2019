from django.contrib import admin
from . models import Doctor, Dose, VitalSignsMeasure, MedicalRecord, Record
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Dose)
admin.site.register(VitalSignsMeasure)
admin.site.register(MedicalRecord)
admin.site.register(Record)