from django.contrib import admin
from .models import User, JobSeeker, Recruiter

# Register your models here.
admin.site.register(User)
admin.site.register(JobSeeker)
admin.site.register(Recruiter)