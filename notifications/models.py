from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from posts.models import Post as PostModel

UserModel = get_user_model()

class Notification(models.Model):
      creating_account = 1
      updating_profile = 2
      applying_company = 3
      
      NOTIFICATION_TYPE = [
            (creating_account, _('Account is created')),
            (updating_profile, _('Profile is updated')),
            (applying_company, _('Post is applied'))
      ]

      type_of_notification          = models.PositiveSmallIntegerField(null=True, blank=True, choices=NOTIFICATION_TYPE)
      sender                        = models.ForeignKey(UserModel, related_name='creater_notification', on_delete=models.CASCADE) 
      receiver                      = models.ForeignKey(UserModel, related_name='consumer_notification', on_delete=models.CASCADE)
      recruitment_post              = models.ForeignKey(PostModel, related_name='recruitment_post', on_delete=models.CASCADE, null=True, blank=True)
      created_at                    = models.DateTimeField(auto_now_add=True)
      is_seen                       = models.BooleanField(default=False)

      class Meta:
            verbose_name            = _('Notification')
            verbose_name_plural     = _('Notifications')

      def __str__(self):
          return f'Notification from {self.sender.username}'