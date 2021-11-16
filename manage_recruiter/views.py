from django.shortcuts import render
from posts.models import Post
# Create your views here.
def managePost(request):
    Data = {'Posts': Post.objects.filter(author_id=request.user.id)}
    return render(request,'manage-posts.html', Data)