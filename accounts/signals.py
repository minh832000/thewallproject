from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from profiles.models import Profile as ProfileModel
from profiles.models import RecruiterProfile as RecruiterProfileModel

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
      if created:
            if instance.is_job_seeker:
                  ProfileModel.objects.create(user=instance)
            if instance.is_recruiter:
                  RecruiterProfileModel.objects.create(user=instance)




# @receiver(post_save, sender=UserModel)
# def save_profile(sender, instance, **kwargs):
#       instance.profile.save()