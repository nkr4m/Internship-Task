from django.db import models

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    expiry_date_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.company_name
    
