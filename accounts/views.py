from django.shortcuts import render
from django.views.generic import CreateView

from .models import User, JobSeeker, Recruiter
from .forms import JobSeekerSignUpForm, RecruiterSignUpForm

# Create your views here.
class jobseeker_register(CreateView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

def successView(request):
      return render(request, 'accounts/register_success.html')