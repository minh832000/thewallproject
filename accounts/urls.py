from django.urls import path

from .import views

urlpatterns = [
      path('jobseeker_register/', views.jobseeker_register.as_view(), name='jobseeker_register'),
      path('success/', views.successView, name='register-success'),
]