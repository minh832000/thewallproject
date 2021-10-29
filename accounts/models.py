from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
      is_job_seeker                = models.BooleanField(default=False)
      is_recruiter                 = models.BooleanField(default=False)
      email                        = models.EmailField(unique=True)

    