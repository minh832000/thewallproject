from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, JobSeeker, Recruiter

class JobSeekerSignUpForm(UserCreationForm):
      first_name = forms.CharField(label='First Name', required=True)
      last_name = forms.CharField(required=True)
      phone_number = forms.CharField(required=True)
      email = forms.EmailField(required=True)
      address = forms.CharField(required=True)

      class Meta(UserCreationForm):
            model = User
            fields = ['first_name', 'last_name', 'username']

      @transaction.atomic
      def save(self):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.save()
            jobseeker = JobSeeker.objects.create(user=user)
            jobseeker.phone_number = self.cleaned_data.get('phone_number')
            jobseeker.email = self.cleaned_data.get('email')
            jobseeker.address = self.cleaned_data.get('address')
            jobseeker.save()
            return user

class RecruiterSignUpForm(UserCreationForm):
      first_name = forms.CharField(required=True)
      last_name = forms.CharField(required=True)
      phone_number = forms.CharField(required=True)
      email = forms.EmailField(required=True)
      company_name = forms.CharField(required=True)

      class Meta(UserCreationForm):
            model = User
            fields = ['first_name', 'last_name', 'username']

      @transaction.atomic
      def save(self):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.save()
            recruiter = Recruiter.objects.create(user=user)
            recruiter.phone_number = self.cleaned_data.get('phone_number')
            recruiter.email = self.cleaned_data.get('email')
            recruiter.address = self.cleaned_data.get('company_name')
            recruiter.save()
            return user
