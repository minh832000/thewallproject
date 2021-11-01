from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .models import User
from .forms import SignUpForm, LoginForm

def view_register_success(request):
     return render(request, 'accounts/register_success.html')

class Register(CreateView):
      model = User
      form_class = SignUpForm
      template_name = 'accounts/jobseeker_register.html'
      success_url = reverse_lazy('accounts:register_success')

      def post(self, request, *args, **kwargs):
            form = SignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.verificationStatus = 'verified'
                  instance.set_password(form.cleaned_data['password'])
                  instance.save()
                  return redirect('accounts:register_success')
            return render(request, 'accounts/jobseeker_register.html', {'form': form})
class Login(FormView):
      form_class = LoginForm
      template_name = 'accounts/sign-in.html'
      success_url = reverse_lazy('home:index')

      def post(self, request, *args, **kwargs):
            form = LoginForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']

                  user = authenticate(request, username=username, password=password)
                  if user is not None:
                        if user.is_active:
                              login(request, user)
                              return redirect('home:index')
            return render(request, 'accounts/sign-in.html', {'form': form})

