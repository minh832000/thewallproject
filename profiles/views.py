from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
class JobSeekerSignUpView(CreateView):
      model = User
      # form_class = 