from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from accounts.models import User
from fields_job.models import FieldJob
from tag_skill.models import TagSkill
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    field_job=models.ForeignKey(FieldJob,on_delete=models.SET_NULL,null=True)
    tag_skill= ManyToManyField(TagSkill,blank=True, null=True, related_name="post_tag")
    name_post = models.CharField(max_length=200, blank=False)
    time_create=models.DateTimeField(default=timezone.datetime.now())
    experience_required=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    content_post=models.CharField(max_length=1000, blank=False, null=False)
    position=models.CharField(max_length=100)
    type_job=models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.name_post