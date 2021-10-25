from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(AbstractUser):
#       is_job_seeker = models.BooleanField(default=False)
#       is_recruiter = models.BooleanField(default=False)

# class Skills (models.Model):
#       id_skill = models.IntegerField()
#       name_skill = models.CharField(max_length=128)
#       describe_skill = models.TextField()
      
# class JobSeekerProfile(models.Model):
#       user_name = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#       # id_profile = models.CharField(primary_key=True, null=False)
#       # basic information fields 
#       profile_picture = models.ImageField()
#       phone_number = models.CharField(max_length=11)
#       address = models.CharField(max_length=255)
#       general_information = models.TextField()
#       # work experiences
#       previous_position = models.CharField(max_length=100)
#       previous_company = models.CharField(max_length=255)
#       previous_job_start_time = models.DateField()
#       previous_job_end_time = models.DateField()
#       # academic level
#       university_name = models.CharField(max_length=255)
#       major = models.CharField(max_length=255)
#       study_status = models.CharField() # 2 choices: graduated and un-graduated
#       enrollment_time = models.DateField()
#       graduation_time = models.DateField()
#       additional_information_education = models.TextField()
#       # previous projects
#       link_project = models.TextField()
#       describe_project = models.TextField()
#       additional_information_project = models.TextField()
#       # skills
#       id_skill = models.ManyToManyField(Skills, through='JobSeekerSkill')
      
# class RecruiterProfile(models.Model):
#       username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
