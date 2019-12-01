from django.db import models

# Create your models here.

class MedicalRecord(models.Model):
    id_record = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    lastname = models.CharField(max_length=45, null=True)
    gender = models.CharField(max_length=2, null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    bloodtype = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null = True)
    phone = models.CharField(max_length=45, null = True)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.id_record,self.email,self.phone)

class Doctor(models.Model):
    id_doctor = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    department = models.CharField(max_length=45)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.id_doctor,self.title,self.name)


    

class VitalSignsMeasure(models.Model):
    id_vs = models.IntegerField(primary_key=True)
    id_record = models.ForeignKey(MedicalRecord, on_delete = models.CASCADE)
    ecg = models.CharField(max_length=20)
    bloodpressure = models.CharField(max_length=20)
    temperature = models.FloatField()
    datetime = models.DateTimeField()

    def __str__(self):
        return "{0}:{1}:{2}".format(self.id_vs,self.id_record,self.datetime)

class Dose(models.Model):
    id_dose = models.IntegerField(primary_key=True)
    id_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, null=True)
    id_doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now=False)  
    nursename = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=100,null=True)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.id_dose,0,0)


class Record(models.Model):
	capacidad = models.IntegerField(default=0)
	location = models.CharField(max_length=100)
	text = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)
	longitude = models.DecimalField(max_digits=9, decimal_places=6, default=None)



    

