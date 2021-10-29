from datetime import date
from django import forms
from django.http.response import HttpResponse
from django.views.generic import CreateView
<<<<<<< HEAD
from django.urls import reverse
from django.views.generic.edit import FormView
=======
import pprint
import socket
>>>>>>> d50600baad7538dafedee413315fda6a319d1897

from .models import User
from .forms import JobSeekerSignUpForm

<<<<<<< HEAD
# Create your views here.
def register_ok(request):
      return render(request, 'accounts/register_success.html')
      # template_name = 'accounts/register_success.html'
      
class jobseeker_register(FormView):
=======


class RegisterJobSeeker(CreateView):
>>>>>>> d50600baad7538dafedee413315fda6a319d1897
      model = User
      form_class = JobSeekerSignUpForm
      template_name = 'accounts/jobseeker_register.html'

<<<<<<< HEAD
      def form_valid(self, form):
            # url = reverse_lazy()
            return redirect(reverse('register_ok'))
=======
      def post(self, request, *args, **kwargs):
            form = JobSeekerSignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.save()
                  return HttpResponse('Đăng ký thành công')

            

>>>>>>> d50600baad7538dafedee413315fda6a319d1897
