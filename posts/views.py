from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from fields_job.models import FieldJob
# Create your views here.

def listJob(request):
      return render(request, 'posts/job_seeker/list_job.html')

def detailJob(request):
      return render(request, 'posts/job_seeker/job_description.html')

def addNewPost(request):
      fieldJob=FieldJob.objects.all()
      a = PostForm()
      return render(request, 'posts/recruiter/add_new_post.html',{ 'f': a, 'fields':fieldJob })


def savePost(request):
      if request.method == 'POST':
            g=PostForm(request.POST)
            if g.is_valid():
                  g.save()
                  return HttpResponse('thêm thành công')
            return HttpResponse('không đc validate')
