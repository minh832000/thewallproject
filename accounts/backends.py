from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomBackend(ModelBackend):
      def authenticate(self, request, username=None, password=None, **kwargs):
            try:
                  user = UserModel.objects.get(username=username)
                  if user:
                        if user.check_password(password):
                              return user
            except UserModel.DoesNotExist:
                  UserModel().set_password(password)
                  return None

      def get_user(self, user_id):
            try:
                  return UserModel.objects.get(pk=user_id)
            except UserModel.DoesNotExist:
                  return None
