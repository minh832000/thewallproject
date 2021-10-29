from datetime import date
from django import forms
from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .models import User
from .forms import JobSeekerSignUpForm

class RegisterJobSeeker(CreateView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'
      success_url = ''

      def post(self, request, *args, **kwargs):
            form = JobSeekerSignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.save()
                  return HttpResponse('Đăng ký thành công')

            return HttpResponse('Đăng ký không thành công')


class Login(TemplateView):
      # model = User 
      template_name = 'accounts/sign-in.html'

