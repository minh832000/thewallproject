from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from django.db.models import fields

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
      readonly_fields = ('created_at',)

admin.site.register(Notification, NotificationAdmin)