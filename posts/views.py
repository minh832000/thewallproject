from django.db.models import query
from django.db.models.fields import CharField
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Post
from fields_job.models import FieldJob
from tag_skill.models import TagSkill
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models.functions import Lower

CharField.register_lookup(Lower)
# Create your views here.

def listJob(request):
      Data = {'Posts': Post.objects.all().order_by('-time_create')}
      return render(request, 'posts/job_seeker/list_job.html', Data)

def detailJob(request,post_id):
      post=Post.objects.get(pk=post_id)
      return render(request, 'posts/job_seeker/job_description.html', {'post':post})

def addNewPost(request):
      fieldJob=FieldJob.objects.all()
      a = PostForm()
      print(request.user.is_recruiter)
      if request.user.id and request.user.is_recruiter:
            return render(request, 'posts/recruiter/add_new_post.html',{ 
                  'f': a, 
                  'fields':fieldJob})
      else: return redirect('accounts:login')


def savePost(request):
      # post = get_object_or_404(Post, pk=pk)
      if request.method == 'POST':
            form=PostForm(request.POST, author=request.user)
            if form.is_valid():
                  f=form.save()
                  # print(f.id)
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

def add_skill(request):
      if request.is_ajax():
            id=request.POST.get('id')
            name=request.POST.get('name')
            data = []
            item = {
                  'id':id,
                  'name':name
                  }
            data.append(item)
            res=data
            print(res)
            return JsonResponse({'data':res})
      return JsonResponse({})
     
def search_post(request):
      if request.is_ajax():
            res = None
            post=request.POST.get('post')
            qs=Post.objects.filter(name_post__unaccent__icontains=post)
            # vector=SearchVector('name_post')
            # query=SearchQuery(post)
            # qs=Post.objects.annotate(rank=SearchRank(vector, query))

            if len(qs) > 0 and len(post) >0:
                  data = []
                  for pos in qs:
                        item = {
                              'pk': pos.pk,
                              'name':pos.name_post
                        }
                        data.append(item)
                  res=data
            else:
                  res=''
            return JsonResponse({'data':res})
      return JsonResponse({})



def search(request):
      if request.method == 'POST':
            post=request.POST.get('post')
            location=request.POST.get('location')
            Data = {'Posts': Post.objects.filter(name_post__unaccent__icontains=post, location__unaccent__icontains=location)}
      return render(request, 'posts/job_seeker/list_job.html', Data)


def filter(request):
      if request.method == 'POST':
            filter=dict(request.POST)
            Data=[]
            if ("type-job" in filter):
                  for item in dict(filter)['type-job']:
                        post =  list(Post.objects.filter(type_job__unaccent__icontains=item))
                        if len(post)>0:
                              Data.extend(list(post))
            if ("location" in filter):
                  for item in dict(filter)['location']:
                        post =  list(Post.objects.filter(location__unaccent__icontains=item))
                        if len(post)>0:
                              Data.extend(list(post))
            if ("job" in filter):
                  for item in dict(filter)['job']:
                        post =  list(Post.objects.filter(field_job__field_name__unaccent__icontains=item))
                        if len(post)>0:
                              Data.extend(list(post))
            return render(request, 'posts/job_seeker/list_job.html',{'Posts': Data})
            
      