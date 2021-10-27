from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request, 'index.html')

def recruiterHome(request):
      return render(request, 'recruiter_home.html')