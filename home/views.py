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
            # Check user's account
            try:
                  user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist')
            if user.is_job_seeker:
                  try:
                        profile = ProfileModel.objects.get(user=username)
                  except ProfileModel.DoesNotExist:
                        print('User\'s Profile does not exist')
                  # Prepare data needed for user
                  context = {
                        'first_name_of_user': user.first_name,
                        'profile_picture_link': profile.profile_picture.url,
                  }
                  return render(request, 'JobSeeker/index.html', context)
            if user.is_recruiter:
                  return redirect('/recruiter')
            else:
                  return render(request, 'JobSeeker/index.html')

class RecruiterIndex(View):
      def get(self, request):
            # Get username
            username = request.user
            # Check if the user is logged in
            if not request.user.is_authenticated:
                  return render(request, 'Recruiter/index.html')

            # Get information of the user from database
            try:
                  user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                  print('User\'s account does not exist')

            if user.is_recruiter:
                  try:
                        recruiter_profile = RecruiterProfileModel.objects.get(user=username)
                  except RecruiterProfileModel.DoesNotExist:
                        print('User\'s profile does not exist')
                  # Prepare data needed for user
                  context = {
                        'user': user,
                        'profile_picture_company_link': recruiter_profile.profile_picture_company.url,
                  }
                  return render(request, 'Recruiter/index.html', context)
            if user.is_job_seeker:
                  return redirect('/')
            


