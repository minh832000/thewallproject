from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request, 'jobseeker/index.html')

def recruiter_index(request):
      return render(request, 'recruiter/index.html')