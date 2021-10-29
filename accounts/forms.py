from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
import re

from .models import User

class JobSeekerSignUpForm(forms.ModelForm):  
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']

   
