from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
import datetime

# Create your views here.


class JOBS(generics.ListAPIView): 
    queryset = Job.objects.all().filter( expiry_date_time = '2020-10-06T09:09:01Z')
    serializer_class = JobSerializer
