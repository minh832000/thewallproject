from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification as NotificationModel
from posts.models import Post_apply as ApplicationModel

@receiver(post_save, sender=ApplicationModel)
def create_application(sender, instance, created, **kwargs):
      application = instance
      applicant = application.user_apply
      post = application.post_apply
      recruiter = post.author
      print(post)
      if created:
            # Creating notification
            notification = NotificationModel(type_of_notification=3, sender=applicant, receiver=recruiter, post=post.id)
            notification.save()