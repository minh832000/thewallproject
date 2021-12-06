from django.urls import path
from . import views

urlpatterns = [
      path('post/', views.managePost, name='manage-post'),
      path('applicant/', views.manageApplicant, name='manage-applicant'),
      # path('applicant/show/', views.showApplicant, name='show-applicant')
      path('applicant/accept/', views.accept, name='accept-applicant'),
      path('applicant/refuse/', views.refuse, name='refuse-applicant'),

      
]