from django import forms
from django.contrib.auth import authenticate
from django.db import transaction
import re

from .models import User

class SignUpForm(forms.ModelForm):  
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)
      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']
      
      @transaction.atomic
      def clean_re_password(self):
            if 'password' in self.cleaned_data:
                  password = self.cleaned_data['password']
                  re_password = self.cleaned_data['re_password']
                  if password != re_password and password:
                       raise forms.ValidationError('Mật khẩu và xác nhận mật khẩu không trùng nhau')
                  return password
            raise forms.ValidationError('Mật khẩu không hợp lệ')
            
      def clean_username(self):
            username = self.cleaned_data['username']
            if not re.search(r'^\w+$', username):
                  raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
            try:
                  User.objects.get(username=username)
            except User.DoesNotExist:
                  return username
            raise forms.ValidationError("Tài khoản đã tồn tại")
                 
      
      def clean_email(self):
            email = self.cleaned_data['email']
            try:
                  User.objects.get(email=email)
            except User.DoesNotExist:
                  return email
            raise forms.ValidationError('Email đã được sử dụng')

class LoginForm(forms.Form):
      username = forms.CharField(max_length=30, required=True)
      password = forms.CharField(required=True, widget=forms.PasswordInput)
      
class RecruiterSignUpForm(forms.ModelForm):
      re_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

      class Meta():
            model = User
            fields = ['username', 'email', 'password', 'first_name', 'last_name']
