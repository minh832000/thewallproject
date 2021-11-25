from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model

from profiles.models import Profile as ProfileModel
from profiles.models import RecruiterProfile as RecruiterProfileModel

UserModel = get_user_model()

class Index(View):
      def get(self, request):
            # Get username
            username = request.user
            # Check if the user is logged in
            if not request.user.is_authenticated:
                  return render(request, 'JobSeeker/index.html')

            user = UserModel.objects.get(username=username)
            try:
                  profile = ProfileModel.objects.get(user=username)
            except ProfileModel.DoesNotExist:
                  return redirect('/recruiter')

            return render(request, 'JobSeeker/index.html', {
                  'user': user,
                  'profile_picture_link': profile.profile_picture.url,
            })

class RecruiterIndex(View):
      def get(self, request):
            # Get username
            username = request.user
            # Check if the user is logged in
            if not request.user.is_authenticated:
                  return render(request, 'Recruiter/index.html')

            # Get information of the user from database
            user = UserModel.objects.get(username=username)
            try:
                  recruiter_profile = RecruiterProfileModel.objects.get(user=username)
            except RecruiterProfileModel.DoesNotExist:
                  return redirect('/')

            # Send data needed by the user
            context = {
                  'user': user,
                  'profile_picture_company_link': recruiter_profile.profile_picture_company.url,
            }
            return render(request, 'Recruiter/index.html', context)
            


