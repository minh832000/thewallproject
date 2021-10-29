from django import forms
from django.forms import fields

from .models import User

class SignUpForm(forms.ModelForm):  
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)
      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']
      
      def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['re_password']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password']

class LoginForm(forms.Form):
      username = forms.CharField(required=True, max_length=30)
      password = forms.CharField(required=True, widget=forms.PasswordInput)

      def __init__(self, *args, **kwargs):
            self.username = 'Unknown'
            self.password = 'Password'
            super(LoginForm, self).__init__(*args, **kwargs)     
      
class RecruiterSignUpForm(forms.ModelForm):
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']
