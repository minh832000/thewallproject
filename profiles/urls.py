from django.urls import path

from .import views

app_name = 'profiles'
urlpatterns = [
      path('', views.Profile.as_view(), name='profiles'),
      # path('recruiter/', views.profileRecruiter, name='profiles-recruiter')
]