from django.contrib import admin




# Register your models here.
from .models import Job

admin.site.register(Job)

admin.site.site_header = "My Site"