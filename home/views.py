from django.shortcuts import render
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
            profile = ProfileModel.objects.get(user=username)

            return render(request, 'JobSeeker/index.html', {
                  'user': user,
                  'profile_picture_link': profile.profile_picture.url,
            })

class RecruiterIndex(View):
      def get(self, request):
            # Get username
            username = request.user
            #print(username)

            return render(request, 'Recruiter/index.html')


