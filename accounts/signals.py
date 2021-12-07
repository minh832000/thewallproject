from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from profiles.models import Profile as ProfileModel
from profiles.models import RecruiterProfile as RecruiterProfileModel
from notifications.models import Notification as NotificationModel
UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
      account = instance
      username = account.username
      if created:
            # Creating notification object to inform that account is createds
            notification = NotificationModel(type_of_notification=1, sender=username, receiver=username)
            # Creating profile object
            try:
                  user = UserModel.objects.get(username=instance)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist.')
            if user.is_job_seeker:
                  print('Is job seeker')
                  ProfileModel.objects.create(user=instance)
            if user.is_recruiter:
                  print('Is recruiter')
                  RecruiterProfileModel.objects.create(user=instance)
