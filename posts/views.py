from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from fields_job.models import FieldJob
from tag_skill.models import TagSkill
# Create your views here.

def listJob(request):
      return render(request, 'posts/job_seeker/list_job.html')

def detailJob(request):
      return render(request, 'posts/job_seeker/job_description.html')

def addNewPost(request):
      fieldJob=FieldJob.objects.all()
      # def sample_view(request):
      a = PostForm()
      # current_user = request.user
      return render(request, 'posts/recruiter/add_new_post.html',{ 
            'f': a, 
            'fields':fieldJob})


def savePost(request):
      if request.method == 'POST':
            form=PostForm(request.POST, author=request.user)
            # field = get_object_or_404(FieldJob, pk=form.field_job)
            if form.is_valid():
                  form.save()
                  return HttpResponse('thêm thành công')
            return HttpResponse('không đc validate')

def search_result(request):
      if request.is_ajax():
            res = None
            skill=request.POST.get('skill')
            qs=TagSkill.objects.filter(name__icontains=skill)
            if len(qs) > 0 and len(skill) >0:
                  data = []
                  for pos in qs:
                        item = {
                              'pk': pos.pk,
                              'name':pos.name
                        }
                        data.append(item)
                  res=data
            else:
                  res='No skill found..'
            return JsonResponse({'data':res})
      return JsonResponse({})

def add_skill(request,pk):
      if request.is_ajax():
            id=request.POST.get('id')
            tag = get_object_or_404(FieldJob, pk=id)
            post=PostForm.objects.get(pk=pk)
            post.tagskill.add(tag)
            return JsonResponse({'success'})
      return JsonResponse({})
