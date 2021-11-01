from django.urls import path

from .import views

app_name = 'accounts'
urlpatterns = [
      path('register/', views.Register.as_view(), name='register'),
      path('login/', views.Login.as_view(), name='login'),
      path('register-success', views.view_register_success, name='register_success'),
      path('recruiter/register/', views.RecruiterRegister.as_view(), name='recruiter_register'),
      path('recruiter/login/', views.RecruiterLogin.as_view(), name='recruiter_login'),
]