from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Index(View):
      def get(self, request):
            return render(request, 'jobseeker/index.html')

class RecruiterIndex(View):
      def get(self, request):
            return render(request, 'recruiter/index.html')


