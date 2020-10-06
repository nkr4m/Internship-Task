from rest_framework import serializers 
from .models import Job
import datetime

class JobSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job
        fields = ('id', 'company_name', 'expiry_date_time')