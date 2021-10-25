from django.urls import path
from . import views

urlpatterns = [
      path('listjob/', views.listJob, name='list-job'),
]