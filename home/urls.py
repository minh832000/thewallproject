from django.urls import path
from .import views

app_name = 'home'
urlpatterns = [
      path('', views.index, name='index'),
      path('recruiter/', views.recruiter_index, name='recruiter_index')
]