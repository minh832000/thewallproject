from django.http.response import JsonResponse
from django.shortcuts import render
from posts.models import Post
from accounts.models import User
from profiles.models import Profile
from thewallproject.posts.models import Post_apply
# Create your views here.
def managePost(request):
    Data = {'Posts': Post.objects.filter(author_id=request.user.id).order_by('-time_create')}
    return render(request,'manage-posts.html', Data)

def manageApplicant(request):
    post=Post.objects.filter(author_id=request.user.id)
    return render(request,'manage-candidate.html',{
        'list_job':post
    })

def showApplicant(request):
    if request.method=='POST':
        id_post=request.POST.get('id-post')
        post=Post_apply.objects.filter(post_apply_id=id_post)
        list_applicant=[]
        for applicant in post:
            id_user=User.objects.get(post.user_apply_id)
            # item= Profile.objects.get(user_id=)
        return JsonResponse({'data':'success'})
