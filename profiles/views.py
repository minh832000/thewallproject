from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

UserModel = get_user_model()

class Profile(View):
      def get(self, request):
            return render(request, 'profiles/jobseekers/profile.html')