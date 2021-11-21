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
      # Form: "Thông tin cơ bản"
      user              = models.OneToOneField(UserModel, related_name="profile", on_delete=models.CASCADE)
      profile_picture   = models.ImageField(blank=True, null=True, upload_to='profile-picture', default="default-profile-picture.jpg")
      full_name         = models.CharField(max_length=128, null=True, blank=True)
      date_of_birth     = models.DateField(null=True, blank=True)
      gender            = models.PositiveBigIntegerField(choices=GENDER_CHOICE, null=True, blank=True)
      phone_number      = models.CharField(max_length=32, null=True, blank=True)
      address           = models.CharField(max_length=255, null=True, blank=True)

      created_at        = models.DateTimeField(auto_now_add=True)
      updated_at        = models.DateTimeField(auto_now=True)
      # Form: "Thông tin chung"
      is_updated_summary = models.BooleanField(default=False)
      summary            = models.TextField(max_length=1000, blank=True, null=True)

      # Form: "Trình độ học vấn"
      is_updated_education     = models.BooleanField(default=False)
      name_of_school           = models.CharField(max_length=255, blank=True, null=True)
      academic_degree          = models.CharField(max_length=128, blank=True, null=True)
      name_of_major            = models.CharField(max_length=255, blank=True, null=True)
      time_admission           = models.DateField(blank=True, null=True)
      time_graduate            = models.DateField(blank=True, null=True)
      is_studying              = models.BooleanField(default=False)
      additional_education     = models.TextField(blank=True, null=True)

      # Form: "Kinh nghiệm làm việc"
      is_updated_previous_job  = models.BooleanField(default=False)
      name_of_previous_company = models.CharField(max_length=128, null=True, blank=True)
      previous_job_title       = models.CharField(max_length=128, null=True, blank=True)
      time_start_previous_job  = models.DateField(null=True, blank=True)
      time_end_previous_job    = models.DateField(null=True, blank=True)

      # Form: "Dự án tham gia"
      is_updated_project_participated  = models.BooleanField(default=False)
      name_of_project_participated     = models.CharField(max_length=256, null=True, blank=True)
      position_in_project_participated = models.CharField(max_length=64, null=True, blank=True)
      link_of_project_participated     = models.CharField(max_length=512, null=True, blank=True)
      description_project_participated = models.TextField(max_length=1000, null=True, blank=True)

      # Form: "Hoạt động xã hội"
      is_updated_volunteering_activity = models.BooleanField(default=False)
      name_of_volunteering_activity    = models.CharField(max_length=128, null=True, blank=True)
      role_in_volunteering_activity    = models.CharField(max_length=64, null=True, blank=True)
      time_start_volunteering_activity = models.DateField(null=True, blank=True)
      time_end_volunteering_activity   = models.DateField(null=True, blank=True)
      is_joining                       = models.BooleanField(default=False)
      class Meta:
            verbose_name            = _('Profile')
            verbose_name_plural     = _('Profiles')
      # show how we want it to be displayed
      def __str__(self):
          return f'{self.user.username} profile'

class RecruiterProfile(models.Model):
      user                                      = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile_recruiter")
      profile_picture_company                           = models.ImageField(blank=True, null=True, upload_to='profile-picture', default="default-profile-picture.jpg")
      is_updated_basic_information_company      = models.BooleanField(default=False)
      name_of_company                           = models.CharField(max_length=128, null=True, blank=True)
      location_of_company                       = models.TextField(max_length=256, null=True, blank=True)
      email_of_company                          = models.EmailField(null=True, blank=True)
      hotline_of_company                        = models.TextField(max_length=20, null=True, blank=True)
      website_of_company                        = models.TextField(max_length=256, null=True, blank=True)
      business_field_of_company                 = models.TextField(max_length=128, null=True, blank=True)

      class Meta:
            verbose_name            = _('Profile Recruiter')
            verbose_name_plural     = _('Profiles Recruiter')
       # show how we want it to be displayed
      def __str__(self):
          return f'Profile Recruiter-{self.user.username}'
