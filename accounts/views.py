from django.conf.urls import url
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse

from .models import User, JobSeeker, Recruiter
from .forms import JobSeekerSignUpForm, RecruiterSignUpForm

# Create your views here.
def register_ok(request):
      return render(request, 'accounts/register_success.html')
      
class jobseeker_register(CreateView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

      def form_valid(self, form):
            url = reverse_lazy('register_ok')
            return redirect(reverse(url))
