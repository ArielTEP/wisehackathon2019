from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kioskoapp.models import MedicalRecord
from . serializers import MedicalRecordSerializer
# Create your views here

class MedicalRecordAPI(APIView):

    def get(self, request):
        user_list = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(user_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicalRecordSerializer(data = request.data)
        if serializer.is_valid():
            record = serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=400)

        #print("POST method")
        #data = JSONParser().parse(request)
        #print(data)
        #return Response(str(request.data))

class BandAPI(APIView):
    def post(self, request):
        print(request.data)
        return Response(str(request.data))