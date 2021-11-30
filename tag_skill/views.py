import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import TagSkill

class SkillTag(View):
      def get(self, request):
            print(request)

      def post(self, request):
            if request.method == 'POST' and request.is_ajax():
                  key_word = request.POST.get('key_word')
                  # Initialize dict object to contain data needed for user
                  context = {}

                  # Search key word from Tag Skill Model
                  if key_word:
                        qs = TagSkill.objects.filter(name__icontains=key_word).values()
                        if qs:
                              context['is_found'] = True
                              context['list_tag_skill'] = list(qs)
                        else:
                              context['is_found'] = False
                        return JsonResponse(context, safe=False, content_type='application/json')
                  return JsonResponse({'message': 'Searching Error'})
                

