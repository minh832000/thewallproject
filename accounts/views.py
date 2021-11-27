from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import User
from .forms import SignUpForm, LoginForm, RecruiterRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
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
            print(self.request)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.verificationStatus = 'verified'
                  instance.set_password(form.cleaned_data['password'])
                  instance.save()
                  return render(request, 'accounts/notify_register_success.html')
            return render(request, 'accounts/register.html', {'form': form})

      def dispatch(self, request, *args, **kwargs):
            print(self.request.user)
            return super(Register, self).dispatch(request, *args, **kwargs)

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
      
      def dispatch(self, request, *args, **kwargs):
            print(self.request)
            print(self.request.user)
            print(request.path)
            return super(Login, self).dispatch(request, *args, **kwargs)

class RecruiterRegister(CreateView):
      model = UserModel
      form_class = RecruiterRegisterForm
      template_name = 'accounts/recruiter_register.html'
      success_url = reverse_lazy('accounts:register_success')

      def post(self, request, *args, **kwargs):
            form = RecruiterRegisterForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_recruiter = True
                  instance.set_password(form.cleaned_data['password'])
                  instance.save()
                  return redirect('accounts:register_success')
            return render(request, 'accounts/recruiter_register.html', {'form': form})

      def dispatch(self, request, *args, **kwargs):
            return super(RecruiterRegister, self).dispatch(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('home:index')


def settingAccount(request):
      return render(request, 'accounts/setting_account.html')


def change_password(request):
      if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                  user = form.save()
                  update_session_auth_hash(request, user)  # Important!
                  messages.success(request, 'Your password was successfully updated!')
                  return redirect('accounts:setting')
            else:
                  messages.error(request, 'Please correct the error below.')
      else:
            form = PasswordChangeForm(request.user)
      return render(request, 'accounts/setting_account.html', {
            'form': form
    })

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
      template_name = 'accounts/password/password_reset.html'
      email_template_name = 'accounts/password/password_reset_email.html'
      subject_template_name = 'accounts/password/password_reset_subject'
      success_message = "We've emailed you instructions for setting your password, " \
                        "if an account exists with the email you entered. You should receive them shortly." \
                        " If you don't receive an email, " \
                        "please make sure you've entered the address you registered with, and check your spam folder."
      success_url = reverse_lazy('home:index')

