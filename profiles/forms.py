# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction


# class JobSeekerSignUpForm(UserCreationForm):
#       class Meta(UserCreationForm.Meta):
#             model = UserCreationForm
      
#       @transaction.atomic
#       def save(self):
#             user = super().save(commit=False)
#             user.is_job_seeker = True
#             user.save()
#             return user
