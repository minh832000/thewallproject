from django.urls import path

from .import views

app_name = 'profiles'
urlpatterns = [
      path('', views.Profile.as_view(), name='profiles'),
<<<<<<< HEAD
      # path('recruiter/', views.profileRecruiter, name='profiles-recruiter')
=======
<<<<<<< HEAD
      path('recruiter/', views.RecruiterProfile.as_view(), name='recruiter_profile'),
=======
      path('recruiter/', views.profileRecruiter, name='profiles-recruiter')
>>>>>>> 18f55549503ca80f5eec559a3dc96184905b87e8
>>>>>>> d8baddf5b3bf1e4e2c64cb4aae46d710a4e7623b
]