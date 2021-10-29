from datetime import date
from django import forms
from django.http.response import HttpResponse
from django.views.generic import CreateView
import pprint
import socket

from .models import User
from .forms import JobSeekerSignUpForm



class RegisterJobSeeker(CreateView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

      def post(self, request, *args, **kwargs):
            form = JobSeekerSignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.save()
                  return HttpResponse('Đăng ký thành công')

            

