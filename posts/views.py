from django.shortcuts import render

# Create your views here.

def listJob(request):
      return render(request, 'posts/job_seeker/list_job.html')
