from django.http.response import JsonResponse
from django.shortcuts import render
from posts.models import Post
from accounts.models import User
from profiles.models import Profile
from posts.models import Post_apply
# Create your views here.
def managePost(request):
    Data = {'Posts': Post.objects.filter(author_id=request.user.id).order_by('-time_create')}
    return render(request,'manage-posts.html', Data)

def manageApplicant(request):
    post=Post.objects.filter(author_id=request.user.id)
    listpost=[]
    list_cant=[]
    for i in post:
        p=Post_apply.objects.filter(post_apply_id=i.id)
        listpost.append(p)
    print(listpost)
    arr=[]
    for i in listpost:
        for j in i:
            item= Profile.objects.get(user_id=j.user_apply_id)
            arr.append(item)
        list_cant.append(arr)
    print(list_cant)    
    return render(request,'manage-candidate.html',{
        'list_job':post,
        'list_candidate':list_cant,
        'id_post':listpost
    })

