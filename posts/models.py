from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    name_post = models.CharField(max_length=200, blank=False)
    time_create=models.DateTimeField(default=timezone.datetime.now())
    experience_required=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    content_post=models.CharField(max_length=1000, blank=False, null=False)
    position=models.CharField(max_length=100)
    def __str__(self):
        return self.name_post