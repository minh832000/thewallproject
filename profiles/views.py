from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.forms.models import model_to_dict
import json

from .models import Profile as ProfileModel

UserModel = get_user_model()

class Profile(LoginRequiredMixin, View):
      def get(self, request):
            try:
                  user = UserModel.objects.get(username=request.user)
                  profile = ProfileModel.objects.get(user=request.user)
            except UserModel.DoesNotExist:
                  return render(request, 'profiles/jobseeker/profile.html', {'username': 'Unknown'})
            context = {
                  'user': user,
                  'profile': profile,
            }
            return render(request, 'profiles/JobSeeker/profile.html', context)

      def post(self, request, *args, **kwargs):
            if request.method == 'POST' and request.is_ajax():
                  # Get username of user
                  username = request.user
                  
                  body = json.loads(request.body)
                  if body['form'] == 'basicInformationForm':
                        try:
                              instance = ProfileModel.objects.get(user=username)
                        except ProfileModel.DoesNotExist:
                              instance = ProfileModel.objects.create(user=username)
                        # Update fields in Profile model
                        instance.full_name = body['full_name']
                        instance.phone_number = body['phone_number']
                        instance.address = body['address']
                        instance.save()

                        # Convert instance model to json
                        context = model_to_dict(instance)
                        return  JsonResponse(context, safe=False)
            return JsonResponse({'error': 'Submit error', }, safe=False)

