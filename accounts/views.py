from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render

from .models import User
from .forms import SignUpForm, LoginForm

class RegisterJobSeeker(CreateView):
      model = User
      form_class = SignUpForm
      template_name = 'accounts/jobseeker_register.html'
      success_url = reverse_lazy('accounts:login')

      def post(self, request, *args, **kwargs):
            form = SignUpForm(request.POST)
            if form.is_valid():
                  instance = form.save(commit=False)
                  instance.is_job_seeker = True
                  instance.save()
                  return super(RegisterJobSeeker, self).form_valid(form)
            return render(request, 'accounts/jobseeker_register.html', {'form': form})

class Login(FormView):
      form_class = LoginForm
      template_name = 'accounts/sign-in.html'

      def post(self, request, *args, **kwargs):
            form = LoginForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']

                  user = User.objects.get(username=username, password=password)
                  
                  if user is not None:
                        if user.is_active:
                              return redirect('home:index')
                  return super(Login, self).form_valid(form)
            return HttpResponse('Đăng nhập không thành công')

