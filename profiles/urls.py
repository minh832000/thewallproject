from django.urls import path

from .import views

app_name = 'profiles'
urlpatterns = [
      path('', views.Profile.as_view(), name='profiles'),
      path('recruiter/', views.RecruiterProfile.as_view(), name='recruiter_profile'),
      path('list-company/', views.CompanyListing.as_view(), name='list-company'),
      path('detail-company/<int:company_id>', views.detailCompany, name='detail-company'),
]
