from django.urls import path

from notifications.views import Notification

app_name = 'notifications'
urlpatterns = [
      path('', Notification.as_view(), name='notification')      
]