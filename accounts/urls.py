from django.urls import path

from .import views

urlpatterns = [
      path('jobseeker/', views.jobseeker_register.as_view(), name='jobseeker_register'),
      path('jobseeker/ok/', views.register_ok, name='register_ok'),
]