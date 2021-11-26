from django.db import models

# Create your models here.
class FieldJob(models.Model):
    field_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.field_name