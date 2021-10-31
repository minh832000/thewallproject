from django.http.response import Http404, HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from .models import User
from .forms import SignUpForm, LoginForm

class Register(CreateView):
      model = User
      form_class = SignUpForm
      template_name = 'accounts/jobseeker_register.html'
      success_url = reverse_lazy('accounts:login')

      def post(self, request, *args, **kwargs):
            form = SignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.verificationStatus = 'verified'
                  instance.set_password(form.cleaned_data['password'])
                  instance.save()
                  return super(Register, self).form_valid(form)
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

                  # user = User.objects.get(username=username, password=password)
                  user = authenticate(request, username=username, password=password)
                  if user is not None:
                        if user.is_active:
                              login(request, user)
                              return redirect('home:index')
                  raise Http404('Tài khoản không tồn tại')
            return render(request, 'accounts/sign-in.html', {'form': form})

