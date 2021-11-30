from django.db import models
from django.utils import timezone
from accounts.models import User
from fields_job.models import FieldJob
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
class Post(models.Model):
    id                  = models.AutoField(primary_key=True)
    author              = models.ForeignKey(User,on_delete=models.CASCADE)
    field_job           = models.ForeignKey(FieldJob,on_delete=models.SET_NULL,null=True)
    tag_skill           = ArrayField(
                            models.CharField(max_length=64, null=True, blank=True),
                            size=10,
                            null=True,
                            blank=True,
                        )
    name_post           = models.CharField(max_length=200, blank=False)
    time_create         = models.DateTimeField(default=timezone.datetime.now())
    experience_required = models.CharField(max_length=100)
    salary              = models.CharField(max_length=100)
    location            = models.CharField(max_length=100)
    content_post        = RichTextField(max_length=2000, blank=False, null=False)
    type_job            = models.CharField(max_length=100, blank=False, null=False)
    confirm             = models.BooleanField(default=False)

    def __str__(self):
        return self.name_post