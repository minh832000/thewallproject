from django.urls import path

from .import views

app_name = 'profiles'
urlpatterns = [
      path('', views.Profile.as_view(), name='profiles'),
<<<<<<< HEAD
      path('recruiter/', views.RecruiterProfile.as_view(), name='recruiter_profile'),
=======
      path('recruiter/', views.profileRecruiter, name='profiles-recruiter')
>>>>>>> 18f55549503ca80f5eec559a3dc96184905b87e8
]