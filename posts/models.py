from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from accounts.models import User
from fields_job.models import FieldJob
from tag_skill.models import TagSkill
from django.conf import settings
from ckeditor.fields import RichTextField
from profiles.models import Profile
# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    field_job=models.ForeignKey(FieldJob,null=True,on_delete=models.SET_NULL)
    user_apply=models.ForeignKey('Post_apply',blank=True,null=True,on_delete=models.SET_NULL)
    name_post = models.CharField(max_length=200, blank=False)
    time_create=models.DateTimeField(default=timezone.datetime.now())
    experience_required=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    content_post=RichTextField(max_length=2000, blank=False, null=False)
    type_job=models.CharField(max_length=100, blank=False, null=False)
    confirm= models.BooleanField(default=False)
    def __str__(self):
        return self.name_post

class Post_apply(models.Model):
    id=models.AutoField(primary_key=True)
    user_apply=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    post_apply=models.ForeignKey(Post, blank=True,null=True,on_delete=models.SET_NULL)
    status_apply=models.CharField(max_length=20, blank=True,null=True, default="wait_accept")