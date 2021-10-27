from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse

from .models import User, JobSeeker, Recruiter
from .forms import JobSeekerSignUpForm, RecruiterSignUpForm

# Create your views here.
class jobseeker_register(CreateView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

      def form_valid(self, form):
            return redirect(reverse('index'))
