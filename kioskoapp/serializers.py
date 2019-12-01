from rest_framework import serializers
from . models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    def create(self, response):
        instance = MedicalRecord()
        instance.id_record = response.get('id_record')
        instance.name = response.get('name')
        instance.lastname = response.get('lastname')
        instance.gender = response.get('gender')
        instance.weight = response.get('weight')
        instance.height = response.get('height')
        instance.bloodtype = response.get('bloodtype')
        instance.email = response.get('email')
        instance.phone = response.get('phone')
        instance.save()
        return instance

    class Meta:
        model = MedicalRecord
        fields = '__all__'