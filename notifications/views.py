import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch.dispatcher import receiver
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.forms.models import model_to_dict

from .models import Notification as NotificationModel

class Notification(LoginRequiredMixin, View):
      def get(self, request):
            # Get username of user
            username = request.user
            # Get queryset notification
            queryset_of_notification = NotificationModel.objects.filter(receiver=username, is_seen=False).order_by('-created_at')
            # Convert queryset to list
            list_of_notification = list(queryset_of_notification.values())
            # Return list of notifications to user
            return JsonResponse({
                  'numbers_of_notifications': len(list_of_notification),
                  'list_of_notifications': list_of_notification,
            }, safe=False, content_type='application/json')