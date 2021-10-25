from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
      is_job_seeker = models.BooleanField(default=False)
      is_recruiter = models.BooleanField(default=False)
      first_name = models.CharField(max_length=100)
      last_name = models.CharField(max_length=100)

class JobSeeker(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
      phone_number = models.CharField(max_length=20)     
      address = models.CharField(max_length=256, null=True) 
      email = models.EmailField(max_length=256, null=True)

class Recruiter(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
      phone_number = models.CharField(max_length=20)
      company_name = models.CharField(max_length=256, null=True)
      email = models.EmailField(max_length=256, null=True)

    