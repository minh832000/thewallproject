from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

UserModel = get_user_model()

class Profile(LoginRequiredMixin, View):
      def get(self, request):
            try:
                  user = UserModel.objects.get(username=self.request.user)
            except UserModel.DoesNotExist:
                  return render(request, 'profiles/jobseeker/profile.html', {'username': 'Unknown'})
            context = {
                  'user': user
            }
            return render(request, 'profiles/jobseekers/profile.html', context)

      def dispatch(self, request, *args, **kwargs):
            print("Data is from request")
            print(self.request.GET)
            print(self.request.user)
            return super(Profile, self).dispatch(request, *args, **kwargs)


def profileRecruiter(request):
      return render(request, 'profiles/recruiter/profile.html')