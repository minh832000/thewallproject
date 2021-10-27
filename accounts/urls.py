from django.urls import path

from .import views

urlpatterns = [
      path('jobseeker_register/', views.jobseeker_register.as_view(), name='jobseeker_register'),
      path('jobseeker_register/ok/', views.register_ok, name='register_ok'),
]