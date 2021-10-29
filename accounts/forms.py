from django import forms

from .models import User

class JobSeekerSignUpForm(forms.ModelForm):  
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)
      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']

class RecruiterSignUpForm(forms.ModelForm):
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']