from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'accounts'
urlpatterns = [
      path('register/', views.Register.as_view(), name='register'),
      path('login/', views.Login.as_view(), name='login'),
      path('logout/', views.logout_view, name='logout'),
      path('register-success', views.view_register_success, name='register_success'),
      path('recruiter/register/', views.RecruiterRegister.as_view(), name='recruiter_register'),
      path('setting/', views.change_password, name='setting'),
      # path(r'^password/$', views.change_password, name='change_password')

      
      path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
      path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
      path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'),
         name='password_reset_complete'),
]