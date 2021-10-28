from django.conf.urls import url
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.urls import reverse
from django.views.generic.edit import FormView

from .models import User
from .forms import JobSeekerSignUpForm

# Create your views here.
def register_ok(request):
      return render(request, 'accounts/register_success.html')
      # template_name = 'accounts/register_success.html'
      
class jobseeker_register(FormView):
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

      def form_valid(self, form):
            # url = reverse_lazy()
            return redirect(reverse('register_ok'))
