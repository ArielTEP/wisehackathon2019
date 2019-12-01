from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from kioskoapp.models import MedicalRecord
from . serializers import MedicalRecordSerializer
from .models import Record
#add for DRF API to work
from rest_framework import generics
from .serializers import RecordSerializer
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
        uid = request.data['uid']
        if uid == '478':
            #aumentar Record capacidad de Hospital1 
            hospital = Record.objects.get(id=1)
            
        elif uid == '693':
            #aumentar Record capacidad de Hospital2
            hospital = Record.objects.get(id=2)
        else:
            print("no encontre el tag")
        hospital.capacidad += 1
        hospital.save()
        return redirect("home")


def home(request):
    return render(request,"kioskoapp/home.html")

#API to get all records
class RecordAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Record.objects.all()
    serializer_class = RecordSerializer