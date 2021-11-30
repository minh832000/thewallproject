from django.db.models.fields import CharField
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

from accounts.models import User
from .models import Post_apply
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from fields_job.models import FieldJob
from tag_skill.models import TagSkill
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models.functions import Lower
CharField.register_lookup(Lower)

from profiles.models import Profile as ProfileModel
from profiles.models import RecruiterProfile as RecruiterProfileModel

UserModel = get_user_model()

@login_required
def listJob(request):
      # Get username of the user
      username = request.user
      # Get url of user's profile picture
      try:
            profile = ProfileModel.objects.get(user=username)
      except ProfileModel.DoesNotExist:
            print('User\'s profile does not exist')
      # Get first name of the user
      try:
            user = UserModel.objects.get(username=username)
      except UserModel.DoesNotExist:
            print('User\'s account does not exist')

      # Prepare data needed 
      context = {
            'first_name_of_user': user.first_name,
            'profile_picture_link': profile.profile_picture.url,
            'list_of_job_postings': Post.objects.filter(confirm=True).order_by('-time_create'),
      }
      return render(request, 'posts/JobSeeker/job-listing-page.html', context)

@login_required
def detailJob(request, post_id):
      post = Post.objects.get(pk=post_id)
      author = post.author_id
     
      profile =  RecruiterProfileModel.objects.get(user_id=author)
      
      # Prepare data needed
      context = {
            'post': post,
            'company': profile,
      }
      return render(request, 'posts/JobSeeker/job_description.html', context)

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
                  form.save()
                  inform='Thêm thành công'
                  return redirect('manage-post')
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
            
def editPost(request, post_id):
      post=Post.objects.get(pk=post_id)
      fieldJob=FieldJob.objects.all()
      a = PostForm()
      if request.user.id and request.user.is_recruiter:
            return render(request, 'posts/recruiter/edit_post.html',{ 
                  'f': a, 
                  'post':post,
                  'fields':fieldJob,
                  'id': post_id
                  })
      else: return redirect('accounts:login')

def saveEdit(request, post_id):
      # post = get_object_or_404(Post, pk=pk)
      if request.method == 'POST':
            fieldjob=FieldJob.objects.get(id=request.POST.get('field_job'))
            name_post=request.POST.get('name_post')
            experient=request.POST.get('experience_required')
            salary=request.POST.get('salary')
            location=request.POST.get('location')
            content=request.POST.get('content_post')
            Post.objects.update_or_create(id=post_id,
            defaults={
                  'name_post':name_post,
                  'experience_required': experient,
                  'field_job':fieldjob,
                  'salary':salary,
                  'location':location,
                  'content_post':content
            })
            return redirect('manage-post')
      return HttpResponse('không đc validate')

def applyPost(request):
      if request.method=='POST':
            post_id=request.POST.get('id-post')
            user=User.objects.get(pk=request.user.id)
            apply=Post.objects.get(id=post_id)
            p=Post_apply.objects.create(user_apply_id=user.id, post_apply_id=post_id)
            apply.user_apply_id=p.id
            apply.save()
            return JsonResponse({'data':'success'})
      return JsonResponse({})


def myApply(request):
      id_user=request.user.id
      list_apply_wait_accept=Post_apply.objects.filter(user_apply_id=id_user, status_apply='wait_accept')
      list_post_wait_accept=[]
      list_post_accepted=[]
      list_apply_accepted=Post_apply.objects.filter(user_apply_id=id_user, status_apply='accept')
      for post in list_apply_wait_accept:
            apply=Post.objects.get(id=post.post_apply_id)
            list_post_wait_accept.append(apply)

      for post in list_apply_accepted:
            apply=Post.objects.get(id=post.post_apply_id)
            list_post_accepted.append(apply)
      return render(request, 'posts/JobSeeker/my-application.html',{
            'list_apply': list_post_wait_accept,
            'list_apply_accept': list_post_accepted
      })