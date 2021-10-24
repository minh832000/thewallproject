from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
      is_job_seeker = models.BooleanField(default=False)
      is_recruiter = models.BooleanField(default=False)

class JobSeekerProfile(models.Model):
      username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Recruiter(models.Model):
      username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)