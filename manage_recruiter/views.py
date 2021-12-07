from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from posts.models import Post
from accounts.models import User
from profiles.models import Profile
from profiles.models import RecruiterProfile
from posts.models import Post_apply

@login_required
def managePost(request):
    recruiter_profile = RecruiterProfile.objects.get(user=request.user)
    context = {
        'profile_picture_company_link': recruiter_profile.profile_picture_company.url,
        'Posts': Post.objects.filter(author_id=request.user.id).order_by('-time_create')
    }
    return render(request,'manage-posts.html', context)

def manageApplicant(request):
    post=Post.objects.filter(author_id=request.user.id)
    return render(request,'manage-candidate.html',{
        'list_job':post
    })

@login_required
def showApplicant(request):
    if request.method=='POST':
        id_post=request.POST.get('id-post')
        post=Post_apply.objects.filter(post_apply_id=id_post)
        list_applicant=[]
        for applicant in post:
            user=User.objects.get(id=applicant.user_apply_id)
            item= Profile.objects.get(user_id=user.id)
            list_applicant.append(item)
            print(list_applicant)
        return JsonResponse({'data':'success'})
