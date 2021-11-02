from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login

from .models import User
from .forms import SignUpForm, LoginForm

UserModel = get_user_model()

def view_register_success(request):
     return render(request, 'accounts/notify_register_success.html')

class Register(CreateView):
      model = User
      form_class = SignUpForm
      template_name = 'accounts/register.html'
      success_url = reverse_lazy('accounts:register_success')

      def post(self, request, *args, **kwargs):
            form = SignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.verificationStatus = 'verified'
                  instance.set_password(form.cleaned_data['password'])
                  instance.save()
                  return render(request, 'accounts/notify_register_success.html')
            return render(request, 'accounts/register.html', {'form': form})

class Login(FormView):
      form_class = LoginForm
      template_name = 'accounts/login.html'
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
            return render(request, 'accounts/login.html', {'form': form})

class RecruiterRegister(CreateView):
      model = UserModel


class RecruiterLogin(FormView):
      model = UserModel
