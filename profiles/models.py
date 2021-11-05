from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

UserModel = get_user_model()

class Profile(models.Model):
      GENDER_MALE       = 1
      GENDER_FEMALE     = 2
      GENDER_CHOICE     = [
            (GENDER_MALE, _('Name')),
            (GENDER_FEMALE, _('Nữ')),
      ]

      user              = models.OneToOneField(UserModel, related_name="profile", on_delete=models.CASCADE)
      date_of_birth     = models.DateField(null=True, blank=True)
      gender            = models.PositiveBigIntegerField(choices=GENDER_CHOICE, null=True, blank=True)
      phone_number      = models.CharField(max_length=32, null=True, blank=True)
      address           = models.CharField(max_length=255, null=True, blank=True)

      created_at        = models.DateTimeField(auto_now_add=True)
      updated_at        = models.DateTimeField(auto_now=True)

      class Meta:
            verbose_name            = _('Profile')
            verbose_name_plural     = _('Profiles')

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
