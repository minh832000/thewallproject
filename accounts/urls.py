from django.urls import path

from .import views

urlpatterns = [
      path('register/', views.RegisterJobSeeker.as_view(), name='register_jobseeker'),
      
      # path('register_recruiter/', views.register_ok, name='register_ok'),
]