from django.urls import path
from .import views

urlpatterns = [
      path('', views.index, name='index'),
      path('jobseeker', views.index, name='jobseeker-home'),
      path('recruiter/', views.recruiterHome, name='recruiter-home'),
]