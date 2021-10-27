from django.urls import path
from . import views

urlpatterns = [
      path('jobseeker', views.index, name='jobseeker-home'),
      path('recruiter/', views.recruiterHome, name='recruiter-home'),
]